import re
import os
from glob import glob
import fire
import glob

def clean_markdown(md_text: str) -> str:
    lines = md_text.splitlines()

    inside_italic_block = False
    italic_buffer = []
    new_lines = []

    for line in lines:
        stripped = line.rstrip()

        # --- 1️⃣ Tiêu đề đánh số (1. / 1.1 / 1.1.1 / 1.2.1.1 ...) ---
        # Regex chỉ match kiểu **1** **Tiêu đề**
        match = re.match(
            r"^_?\*\*(\d+(?:\.\d+)*)\.?\*\*_?\s+\*\*(.+?)\*\*$", stripped
        )
        if match and (stripped.startswith("**") or stripped.startswith("_**")):
            numbering = match.group(1)
            title = match.group(2).strip()
            level = numbering.count(".") + 1
            new_lines.append(f"{'#' * level} {title}")
            continue


        # ===== 🔹 Loại 2: tiêu đề in đậm không có số =====
        # Ví dụ: "**Dịch vụ nhà thông minh**"
        bold_heading = re.match(r"^_?\*\*(.+?)\*\*_?$", stripped)
        if bold_heading:
            title = bold_heading.group(1).strip()
            new_lines.append(f"### {title}")
            continue

        # ===== 🔹 Loại 3: tiêu đề trong block in nghiêng có số =====
        # Ví dụ: "_1.2.1.1._ _Đo điều kiện nhà_"
        if stripped.startswith("_"):
            italic_numbered = re.match(r"^_?(\d+(?:\.\d+)+)\.?_?\s*_?(.+?)_?$", stripped)
            if italic_numbered:
                numbering = italic_numbered.group(1)
                title = italic_numbered.group(2).strip(" *_#.")
                level = numbering.count(".") + 1
                new_lines.append(f"{'#' * level} {title}")
                continue

        # --- 3️⃣ Gom đoạn nghiêng nhiều dòng (kể cả có **bold**) ---
        if re.match(r"^_.*_$", stripped):
            text = stripped.strip("_").strip()
            italic_buffer.append(text)
            inside_italic_block = True
            continue
        else:
            if inside_italic_block:
                paragraph = " ".join(t.strip() for t in italic_buffer if t.strip())
                new_lines.append(f"_{paragraph}_")
                italic_buffer = []
                inside_italic_block = False

        match = re.match(r"^_([a-zA-Z])\)_\s*(.*)$", stripped)
        if match:
            letter = match.group(1).lower()
            rest = match.group(2).strip()       # giữ nguyên toàn bộ phần còn lại
            number = ord(letter) - ord('a') + 1 # a → 1, b → 2, ...
            new_lines.append(f"{number}. {rest}")
            continue
        match = re.match(r"^\[(\d+)\]\s*(.*)$", stripped)
        if match:
            number = match.group(1)
            rest = match.group(2)
            if rest and re.match(r"[A-ZÁÀẢÃẠÂĂĐÊÔƠƯ]", rest[0]):
                new_lines.append(f"{number}. {rest}")
                continue

        new_lines.append(stripped)

    # --- 4️⃣ Kết thúc đoạn nghiêng cuối ---
    if inside_italic_block and italic_buffer:
        paragraph = " ".join(t.strip() for t in italic_buffer if t.strip())
        new_lines.append(f"_{paragraph}_")

    # --- 5️⃣ Ghép các cụm nghiêng liền nhau (_a_ _b_ → _a b_) ---
    merged_inline = []
    italic_pattern = re.compile(r"(_[^_]+_)(\s*)(_[^_]+_)")
    for line in new_lines:
        while italic_pattern.search(line):
            line = italic_pattern.sub(
                lambda m: f"_{m.group(1).strip('_')} {m.group(3).strip('_')}_", line
            )
        merged_inline.append(line)
    new_lines = merged_inline

    # --- 6️⃣ Nối dòng nếu không kết thúc bằng dấu câu ---
    merged_lines = []
    buffer = ""
    buffer_indent = 0   # ghi nhớ indent của dòng đầu tiên trong đoạn

    processed_lines = set() 
    for i in range(len(new_lines)):
        line = new_lines[i].rstrip()

        if line in processed_lines:
            continue

        # Giữ nguyên khoảng trắng đầu dòng
        indent = len(line) - len(line.lstrip(" "))
        stripped = line.rstrip()  # chỉ xóa cuối dòng, giữ indent

        # ---- PHÁT HIỆN BẢNG MARKDOWN ----
        if "|" in line:
            j = i
            table_lines = []
            # Gom tất cả các dòng có ký tự | liên tiếp
            while j < len(new_lines) and "|" in new_lines[j]:
                table_lines.append(new_lines[j].strip())
                j += 1

            # Nếu dòng thứ hai có --- thì đây là bảng
            if len(table_lines) > 1 and "---" in table_lines[1]:
                headers = [h.strip() for h in table_lines[0].strip("|").split("|")]

                html = []
                html.append("<table border=\"1\" cellpadding=\"6\" cellspacing=\"0\">")
                html.append("<colgroup>")
                html += [f"<col/>" for _ in headers]
                html.append("</colgroup>")
                html.append("<thead>")
                html.append("<tr>")
                for h in headers:
                    html.append(f"<th>{h}</th>")
                html.append("</tr>")
                html.append("</thead>")
                html.append("<tbody>")

                for row_line in table_lines[2:]:
                    cells = [c.strip() for c in row_line.strip("|").split("|")]
                    html.append("<tr>")
                    for c in cells:
                        html.append(f"<td>{c}</td>")
                    html.append("</tr>")

                html.append("</tbody>")
                html.append("</table>")


                # Ghi HTML bảng vào kết quả
                merged_lines.append("\n".join(html))

                # Bỏ qua các dòng đã xử lý trong bảng
                processed_lines.update(range(i, j))
                continue
  # chuyển sang dòng kế tiếp sau bảng


            if not stripped.strip():
                if buffer:
                    merged_lines.append(buffer.rstrip())
                    buffer = ""
                merged_lines.append("")  # dòng trống giữ nguyên
                continue

        if stripped.startswith("`o`"):
            # loại bỏ `o` và thêm dấu *
            line = "* " + stripped[3:].lstrip()  # 3 ký tự: ` o `
            stripped = line

        # Nếu là tiêu đề thì flush buffer
        if re.match(r"^\s*#{1,6}\s", stripped):
            if buffer:
                merged_lines.append(buffer.rstrip())
                buffer = ""
            merged_lines.append(stripped)
            continue

        if not buffer:
            buffer = stripped
            buffer_indent = indent
        else:
            # Nếu dòng trước KHÔNG kết thúc bằng dấu câu thì nối liền
            if not re.search(r"[.!?;:,…)]\s*$", buffer):
                buffer += " " + stripped.lstrip()
            else:
                merged_lines.append(buffer.rstrip())
                buffer = " " * buffer_indent + stripped

    if buffer:
        merged_lines.append(buffer.rstrip())

    text = "\n".join(merged_lines)


    # Giữ nguyên indent, xử lý tiêu đề, dấu *, khoảng trắng dư...
    text = re.sub(r'(?<!\n)\n?(?=^#{1,6}\s)', r'\n\n', text, flags=re.MULTILINE)
    text = re.sub(r'(^#{1,6}\s.*?)(?!\n\n)(\n)(?!$)', r'\1\n\n', text, flags=re.MULTILINE)
    text = re.sub(r'^(\s*)-(?=\s)', r'\1*', text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    # --- Xóa dòng trống đầu file ---
    lines = text.split("\n")
    while lines and lines[0].strip() == "":
        lines.pop(0)
    text = "\n".join(lines)

    # --- 9️⃣ Thêm dấu * cho các dòng thụt lề bằng space (không tab) ---
    def add_bullet_if_indented(line: str) -> str:
        # Bỏ qua dòng trống hoặc tiêu đề
        if not line.strip() or line.lstrip().startswith(('#', '-', '*')):
            return line
        # Nếu dòng bắt đầu bằng tab hoặc không thụt lề thì giữ nguyên
        if line.startswith('\t') or not line.startswith(' '):
            return line
        # Nếu có thụt lề bằng space thì thêm dấu *
        return re.sub(r'^(\s+)(\S)', r'\1* \2', line)

    lines = text.split('\n')

    text = '\n'.join(add_bullet_if_indented(line) for line in lines)
    #text = "\n".join([line for line in text.splitlines() if "|" not in line])


    return text




def postprocess_all(root_dir: str = "./output_test"):
    # Duyệt qua từng thư mục con trong outputtestdata
    subfolders = [f.path for f in os.scandir(root_dir) if f.is_dir()]

    for folder in subfolders:
        # Tìm file Markdown trong thư mục con
        md_files = glob.glob(os.path.join(folder, "*.md"))
        if not md_files:
            continue

        md_file = md_files[0]  # Lấy file .md đầu tiên (mỗi thư mục có 1 file)
        print(f"🔹 Processing: {md_file}")

        with open(md_file, "r", encoding="utf-8") as f:
            md_text = f.read()

        # --- Hậu xử lý nội dung ---
        cleaned = clean_markdown(md_text)

        output_path = md_file

        # Nếu bạn muốn tạo file mới, giữ file gốc:
        # base = os.path.basename(md_file)
        # name, ext = os.path.splitext(base)
        # output_path = os.path.join(folder, f"{name}_cleaned{ext}")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned)

        print(f"Saved: {output_path}")

    print("Successfully processed all Markdown files!")


if __name__ == "__main__":
    fire.Fire(postprocess_all)