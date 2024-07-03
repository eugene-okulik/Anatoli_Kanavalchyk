"""Распечатывание текста из списков."""

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

text = f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}"

print(text)
