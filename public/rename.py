import os
import re

def rename_files(folder):
    files = os.listdir(folder)

    # 过滤掉自身 rename.py
    files = [f for f in files if f != "rename.py"]

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
