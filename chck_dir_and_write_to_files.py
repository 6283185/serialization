# Напишите функцию, которая получает на вход директорию и
# рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
#
# Пример:
# test/users/names.txt
# Результат в json для names.txt:
# {
# "name": names.txt
# "parent": users,
# "type": "file"
# "size": 4096
# }
import os
import json
import csv
import pickle

def file_walker(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            result.append({
                "name": file,
                "parent": os.path.basename(root),
                "type": "file",
                "size": file_size
            })
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            dir_size = get_directory_size(dir_path)
            result.append({
                "name": dir,
                "parent": os.path.basename(root),
                "type": "directory",
                "size": dir_size
            })
    save_as_json(result)
    save_as_csv(result)
    save_as_pickle(result)

def get_directory_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size

def save_as_json(data):
    with open("result.json", "w") as file:
        json.dump(data, file, indent=4)

def save_as_csv(data):
    with open("result.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "parent", "type", "size"])
        writer.writeheader()
        writer.writerows(data)

def save_as_pickle(data):
    with open("result.pickle", "wb") as file:
        pickle.dump(data, file)




if __name__ == '__main__':
    file_walker("C:\python_learn")