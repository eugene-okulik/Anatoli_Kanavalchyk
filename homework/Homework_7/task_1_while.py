"""Программа 'Угадайка'."""

y = 10

while True:
    try:
        user_input = input('Enter something: ')
        user_input = int(user_input)
    except ValueError:
        print('Please enter a valid number')
        continue

    if user_input == y:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('Попробуйте снова')
