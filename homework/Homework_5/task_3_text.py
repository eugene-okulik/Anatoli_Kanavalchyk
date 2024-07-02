"""Распечатывание текста из списков."""

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

text = f"Students {students[0]}, {students[1]}, {students[2]} " \
       f"study these subjects: {subjects[0]}, " \
       f""f"{subjects[1]}, "f"{subjects[2]}"

print(text)
