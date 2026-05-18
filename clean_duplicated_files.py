import os
import sys
from pathlib import Path


def find_files_with_same_name(directory):
    # 收集所有文件的名称（不包括扩展名）和它们的完整路径
    file_dict = {}
    for root, _, files in os.walk(directory):
        for file in files:
            name_without_ext = os.path.splitext(file)[0]
            ext=os.path.splitext(file)[1]
            if ext in ['.docx', '.doc', '.pdf']:
                if name_without_ext in file_dict:
                    file_dict[name_without_ext].append(os.path.join(root, file))
                else:
                    file_dict[name_without_ext] = [os.path.join(root, file)]
    return file_dict

def delete_duplicate_files(file_dict):
    to_delete = []
    # 删除具有重复名称但不同扩展名的文件
    for files in file_dict.values():
        if len(files) > 1:  # 如果找到多个文件具有相同的名称（不包括扩展名）
            for file in files:
                if file.endswith('.pdf') :
                    for f2 in files:
                        if f2.endswith('.doc') or f2.endswith('.docx'):
                            to_delete.append(f2)
    for file in to_delete:
        if Path(file).exists():
            Path(file).unlink()

def main(directory):
    file_dict = find_files_with_same_name(directory)
    delete_duplicate_files(file_dict)

if __name__ == "__main__":
    main(sys.argv[1])
