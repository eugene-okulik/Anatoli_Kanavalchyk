"""Работа со срезами."""

result1 = "результат операции: 42"
result2 = "результат операции: 514"
result3 = "результат работы программы: 9"

# Извлечение чисел и прибавление 10
num1 = int(result1[result1.index(': ') + 1:]) + 10
num2 = int(result2[result2.index(': ') + 1:]) + 10
num3 = int(result3[result3.index(': ') + 1:]) + 10


# Вывод результатов
print(num1)  # Вывод: 52
print(num2)  # Вывод: 524
print(num3)  # Вывод: 19
