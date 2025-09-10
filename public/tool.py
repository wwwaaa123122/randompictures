import os
import re
import shutil
from PIL import Image

def rename_files(folder):
    files = os.listdir(folder)

    # 过滤掉自身 rename.py
    files = [f for f in files if f != "tool.py"]

    # 分离数字文件和非数字文件
    numeric_files = []
    non_numeric_files = []
    for f in files:
        name, ext = os.path.splitext(f)
        if name.isdigit():
            numeric_files.append((int(name), f))
        else:
            non_numeric_files.append(f)

    # 找出最大数字
    max_num = max([num for num, _ in numeric_files], default=0)

    # 从最大数字+1开始重命名非数字文件
    current_num = max_num + 1
    for f in sorted(non_numeric_files):  # 排序保证稳定性
        name, ext = os.path.splitext(f)
        new_name = f"{current_num}{ext}"
        old_path = os.path.join(folder, f)
        new_path = os.path.join(folder, new_name)

        # 避免重名覆盖
        while os.path.exists(new_path):
            current_num += 1
            new_name = f"{current_num}{ext}"
            new_path = os.path.join(folder, new_name)

        os.rename(old_path, new_path)
        print(f"{f} -> {new_name}")
        current_num += 1


if __name__ == "__main__":
    folder = os.path.dirname(os.path.abspath(__file__))
    rename_files(folder)

Image.MAX_IMAGE_PIXELS = None
def convert_images_to_webp(folder):
    # 支持的图片后缀
    exts = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')

    # 在上级目录创建 origin 文件夹
    parent_dir = os.path.abspath(os.path.join(folder, os.pardir))
    origin_dir = os.path.join(parent_dir, "origin")
    os.makedirs(origin_dir, exist_ok=True)

    for filename in os.listdir(folder):
        if filename.lower().endswith(exts):
            filepath = os.path.join(folder, filename)
            try:
                # 转换为 webp
                img = Image.open(filepath).convert("RGB")
                webp_path = os.path.splitext(filepath)[0] + ".webp"
                img.save(webp_path, "WEBP")

                # 移动原文件到 origin
                shutil.move(filepath, os.path.join(origin_dir, filename))
                print(f"✅ {filename} -> {os.path.basename(webp_path)} (源文件已移至 origin)")
            except Exception as e:
                print(f"❌ 转换失败 {filename}: {e}")

if __name__ == "__main__":
    # 修改为你要处理的目录
    folder = "./"  
    convert_images_to_webp(folder)