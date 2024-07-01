"""Словарь my_dict с различными типами данных."""

# Создание словаря
my_dict = {
    'tuple': (99, 22, 61, 87, None, 'TEST', False, 12.2),
    'list': [100, 501, 126, 745, None, 'TESTING', False, 9.2],
    'dict': {
        'boolean_1': 'true',
        'text_1': 'Hi',
        'float': '9.9',
        'boolean_2': 'false',
        'text_2': 'Bye'
    },
    'set': {111, 23, 36, 77, None, 'text_22', False, 2.99}
}


print("Последний элемент кортежа:", my_dict['tuple'][-1])

# Добавляем в list еще один элемент
my_dict['list'].append('New')
# удаляем 2-ой элемент list
del my_dict['list'][1]

#  В ‘dict’ добавляем элемент с ключом ('i am a tuple',) и любым значением
my_dict['dict'][('i am a tuple',)] = 'Test_value'

# Удаляем из dict какой-нибудь элемент
del my_dict['dict']['boolean_1']

# Добавляем новый элемент в set
my_dict['set'].add('new_element')

# Удаляем элемент из set
my_dict['set'].discard(23)

print("\nОбновленный словарь my_dict:")
print(my_dict)