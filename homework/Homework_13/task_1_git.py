import os
from datetime import datetime, timedelta

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'homework', 'eugene_okulik', 'hw_13', 'data.txt')
print(file_path)


def process_dates(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split(' - ')
            number_date = parts[0].split('. ')
            number = int(number_date[0])
            date_str = number_date[1]

            # Преобразование строки
            date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
            if number == 1:
                new_date = date + timedelta(weeks=1)
                print(new_date)
            elif number == 2:
                day_of_week = date.strftime("%A")
                print(day_of_week)
            elif number == 3:
                current_date = datetime.now()
                days_ago = (current_date - date).days
                print(days_ago)


process_dates(file_path)
