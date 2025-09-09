import os
import shutil
from PIL import Image

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