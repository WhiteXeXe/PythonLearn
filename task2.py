import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task(input_filename) -> None:
    with open(input_filename, 'r') as file:
        chitalka = csv.DictReader(file)
        data = []
        for stolbec in chitalka:
            data.append(stolbec)

    js_data = json.dumps(data, ensure_ascii=False, indent=4)

    with open(OUTPUT_FILENAME, 'w') as js:
        js.write(js_data)

if __name__ == '__main__':
    # Для проверки
    task(INPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
