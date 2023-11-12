# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    json_Array = []
    with open(INPUT_FILENAME, encoding='utf-8') as csv_f:
        csv_Reader = csv.DictReader(csv_f)
        for row in csv_Reader:
            json_Array.append(row)

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_f:
        json_String = json.dumps(json_Array, indent=4)
        json_f.write(json_String)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
