import os
import glob

def merge_markdown_files(root_dir: str = "./output_test"):
    output_file = os.path.join(root_dir, "answer.md")

    md_files = sorted(glob.glob(os.path.join(root_dir, "*", "*.md")))

    with open(output_file, "w", encoding="utf-8") as out:
        # Ghi tiêu đề đầu file
        out.write("### TASK EXTRACT\n")

        for idx, md_path in enumerate(md_files, 1):
            print(f"Merging ({idx}/{len(md_files)}): {md_path}")
            with open(md_path, "r", encoding="utf-8") as f:
                content = f.read().strip()

            out.write(content)
            out.write("\n\n")  # cách nhau 1 dòng trống

    print(f"\nDone! All markdown files merged into: {output_file}")


if __name__ == "__main__":
    merge_markdown_files()
