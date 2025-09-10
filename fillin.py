import os
import re

def rename_files_sequentially(folder):
    # 匹配文件名中的数字部分
    pattern = re.compile(r"^(\d+)(\..+)$")
    files = []

    # 收集符合规则的文件
    for name in os.listdir(folder):
        match = pattern.match(name)
        if match:
            number = int(match.group(1))
            ext = match.group(2)
            files.append((number, ext, name))

    # 按数字排序
    files.sort(key=lambda x: x[0])

    # 顺序重命名
    expected = 1
    for number, ext, old_name in files:
        new_name = f"{expected}{ext}"
        old_path = os.path.join(folder, old_name)
        new_path = os.path.join(folder, new_name)

        if old_name != new_name:
            # 如果目标文件名已经存在，先改成临时名，避免冲突
            temp_path = os.path.join(folder, f"__tmp__{expected}{ext}")
            os.rename(old_path, temp_path)
            old_path = temp_path
            new_path = os.path.join(folder, new_name)

        os.rename(old_path, new_path)
        print(f"{old_name} -> {new_name}")
        expected += 1

if __name__ == "__main__":
    target_folder = "./"  # 修改为你的目录
    rename_files_sequentially(target_folder)