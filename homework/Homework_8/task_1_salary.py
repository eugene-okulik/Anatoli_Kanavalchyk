import random

salary = int(input("Сумма оклада ?: "))

bonus = random.choice([True, False])

if bonus:
    random_bonus = random.randint(100, 1000)
    total_salary = salary + random_bonus
else:
    total_salary = salary


print(f"Зарплата после рассмотрения директором: ${total_salary}")
