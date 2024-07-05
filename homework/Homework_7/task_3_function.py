"""Функция."""


def extract_and_add(result):
    number = int(result.split(': ')[1])
    return number + 10


results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for res in results:
    print(extract_and_add(res))
