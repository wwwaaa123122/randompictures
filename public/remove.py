import os
import hashlib

def file_hash(path, chunk_size=8192):
    """计算文件的SHA256哈希"""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()

def remove_duplicates(folder):
    seen = {}  # {hash: 文件路径}
    for root, _, files in os.walk(folder):
        for name in files:
            path = os.path.join(root, name)
            try:
                h = file_hash(path)
            except Exception as e:
                print(f"无法读取 {path}: {e}")
                continue

            if h in seen:
                print(f"发现重复文件：{path} -> 删除")
                os.remove(path)  # 删除重复文件
            else:
                seen[h] = path

if __name__ == "__main__":
    target_folder = "./"  # 修改为你要处理的目录
    remove_duplicates(target_folder)