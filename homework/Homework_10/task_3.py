from functools import wraps


def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


def operation_selector(func):
    def wrapper(first, second):
        if first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif second > first:
            return func(first, second, '/')
        elif first < 0 or second < 0:
            return func(first, second, '*')

    return wrapper


calc = operation_selector(calc)


def create_price_dict(price_list):
    return {item: int(price_str[:-1]) for line in price_list.split('\n') if line.strip() for item, price_str in
            [line.rsplit(' ', 1)]}


PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

# Cловарь с ценами
price_dict = create_price_dict(PRICE_LIST)

print("Словарь с ценами:")
print(price_dict)


def main():
    first = float(input("Введите первое число: "))
    second = float(input("Введите второе число: "))

    result = calc(first, second)

    print(f"Результат операции: {result}")


if __name__ == "__main__":
    main()
