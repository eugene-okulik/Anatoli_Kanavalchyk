import git
import os
from datetime import datetime, timedelta

# Путь к файлу в github
repo_url = 'https://github.com/eugene-okulik/Anatoli_Kanavalchyk'
file_path_in_repo = 'homework/eugene_okulik/hw_13/data.txt'
clone_dir = '/tmp/repo_clone'

# Клонирование репозитория
if os.path.exists(clone_dir):
    repo = git.Repo(clone_dir)
    repo.remotes.origin.pull()
else:
    repo = git.Repo.clone_from(repo_url, clone_dir)

full_file_path = os.path.join(clone_dir, file_path_in_repo)


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


process_dates(full_file_path)
