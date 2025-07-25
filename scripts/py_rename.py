import os
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
PY_FOLDER = ROOT / "python"

def normalize_filename(filename):
    # 如果已符合命名規則 s{題號}_{題目}.py，則不更改
    if re.match(r'^s\d+_[a-zA-Z0-9_]+\.py$', filename):
        return None

    # 嘗試解析格式：3550. Smallest Index With Digit Sum Equal to Index.py
    match = re.match(r'^(\d+)\.\s+(.*)\.py$', filename)
    if not match:
        return None

    number = match.group(1)
    title = match.group(2)

    # 將標題轉換成小寫並改成用底線連接單字
    title_snake = '_'.join(word.lower() for word in title.split())

    new_name = f's{number}_{title_snake}.py'
    return new_name

def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        if not filename.endswith('.py'):
            continue
        old_path = os.path.join(directory, filename)
        new_filename = normalize_filename(filename)
        if new_filename and new_filename != filename:
            new_path = os.path.join(directory, new_filename)
            print(f'Renaming: {filename} → {new_filename}')
            os.rename(old_path, new_path)

# 使用範例：將 'target_directory' 替換成你的目錄路徑
rename_files_in_directory(PY_FOLDER)
