def fibo_generator():
    a = 0
    b = 1
    yield a
    yield b
    while True:
        temp = a
        a = b
        b = temp + b
        yield b


# Создаем экземпляр функции-генератора
fib_gen = fibo_generator()

# Найти пятое число Фибоначчи
for _ in range(3):  # Пропускаем первые два числа (0 и 1) и берем следующие три
    next(fib_gen)
fifth_fib = next(fib_gen)
print(f"Пятое число Фибоначчи: {fifth_fib}")

# Найти двухсотое число Фибоначчи
for _ in range(196):  # Пропускаем первые 198 чисел и берем следующие два
    next(fib_gen)
two_hundredth_fib = next(fib_gen)
print(f"Двухсотое число Фибоначчи: {two_hundredth_fib}")

# Найти тысячное число Фибоначчи
for _ in range(795):  # Пропускаем первые 797 чисел и берем следующие два
    next(fib_gen)
thousandth_fib = next(fib_gen)
print(f"Тысячное число Фибоначчи: {thousandth_fib}")

# Найти стотысячное число Фибоначчи
for _ in range(99998):  # Пропускаем первые 100000 чисел и берем следующие два
    next(fib_gen)
hundred_thousandt_fib = next(fib_gen)
print(f"Стотысячное число Фибоначчи: {hundred_thousandt_fib}")
