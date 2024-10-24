import json

# TODO решите задачу
def task(a) -> float:
    total = 0

    for item in a:
        prod = item["score"] * item["weight"]
        total += prod

    return round(total, 3)

with open('input.json', 'r') as file:
    data = json.load(file)

print(task(data))




