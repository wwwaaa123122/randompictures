import os

def rename_files(directory):
    # 获取目录下的所有文件（排除子目录）
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # 排序，确保顺序一致
    files.sort()

    # 遍历并重命名
    for index, filename in enumerate(files, start=1):
        # 获取文件后缀
        name, ext = os.path.splitext(filename)
        # 新文件名
        new_name = f"{index}{ext}"
        # 重命名
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        print(f"{filename} -> {new_name}")

if __name__ == "__main__":
    folder = "./"   # 当前目录，可以改成其他路径
    rename_files(folder)