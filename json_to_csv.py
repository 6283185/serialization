# Напишите функцию, которая сохраняет файл JSON в CSV формате.
import json
import csv

def json_to_csv(filename: str):
    with open(f'{filename}.json', 'r') as f_inp: #f_inp = file input
        data = json.load(f_inp)
    rows = []
    for level, users in data.items():
        for id, name in users.items():
            rows.append({'level': level, 'name': name, 'id': id})
    with open(f'{filename}.csv', 'w', newline='') as res:
        csv_write = csv.DictWriter(res, fieldnames= ['level', 'name', 'id'])
        csv_write.writeheader()
        csv_write.writerows(rows)


if __name__ == '__main__':
    json_to_csv('user_data')
