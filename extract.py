import fitz
import pymupdf4llm
from glob import glob
import os
import fire
import tempfile
import re
from PIL import Image


def transform(pdf_dir: str, output_root: str = "output_test"):
    os.makedirs(output_root, exist_ok=True)

    file_list = glob(f"{pdf_dir}/*.pdf")

    for pdf_path in file_list:
        print(f"Processing: {pdf_path}")

        # Tên gốc của file (không đuôi)
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]

        # --- Tạo thư mục riêng cho từng file PDF ---
        pdf_output_dir = os.path.join(output_root, base_name)
        os.makedirs(pdf_output_dir, exist_ok=True)

        # --- Tạo thư mục con cho ảnh ---
        images_dir = os.path.join(pdf_output_dir, "images")
        os.makedirs(images_dir, exist_ok=True)

        pdf_doc = fitz.open(pdf_path)
        md_pages = []
        image_counter = 1

        for i, page in enumerate(pdf_doc):
            # --- Lưu trang tạm ---
            with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
                temp_pdf_path = tmp.name

            new_doc = fitz.open()
            new_doc.insert_pdf(pdf_doc, from_page=i, to_page=i)
            new_doc.save(temp_pdf_path)
            new_doc.close()

            # --- Trích xuất Markdown ---
            md_page = pymupdf4llm.to_markdown(temp_pdf_path)
            os.remove(temp_pdf_path)

            # Nếu là bảng đặc biệt thì bỏ header
            if md_page.lstrip().startswith("|Col1|VIETTEL"):
                md_page = "\n".join(md_page.splitlines()[3:])

            # --- Trích xuất ảnh từ trang PDF ---
            images = page.get_images(full=True)
            for img_index, img in enumerate(images):
                xref = img[0]
                bbox = page.get_image_bbox(img)
                if bbox.y1 < 100:  # bỏ ảnh nằm trên vùng crop
                    continue

                img_filename = f"image{img_index}.png"
                img_path = os.path.join(images_dir, img_filename)
                pix = fitz.Pixmap(pdf_doc, xref)

                if pix.n < 5:  # ảnh RGB
                    pix.save(img_path)
                else:  # ảnh CMYK → chuyển sang RGB
                    pix1 = fitz.Pixmap(fitz.csRGB, pix)
                    pix1.save(img_path)
                    pix1 = None
                pix = None

                # --- Thêm placeholder ảnh vào markdown ---
                md_page += f"\n\n|<image_{image_counter}>|\n"
                image_counter += 1

            md_pages.append(md_page)

        # --- Lưu Markdown trong thư mục PDF tương ứng ---
        output_md_path = os.path.join(pdf_output_dir, f"{base_name}.md")
        full_md = f"# {base_name}\n\n" + "\n\n".join(md_pages)
        with open(output_md_path, "w", encoding="utf-8") as f:
            f.write(full_md)

        print(f"✅ Saved: {output_md_path}\n")

    print("🎉 Successfully processed all PDFs!")


if __name__ == "__main__":
    fire.Fire(transform)
