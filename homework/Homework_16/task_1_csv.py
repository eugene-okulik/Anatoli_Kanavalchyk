import os
import csv
from dotenv import load_dotenv
import mysql.connector

# Загрузка переменных окружения из файла .env
base_path = os.path.dirname(__file__)
env_path = os.path.join(base_path, '.env')
load_dotenv(env_path)


# Подключение к базе данных MySQL
def connect_to_db():
    try:
        db = mysql.connector.connect(
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSW'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            database=os.getenv('DB_NAME')
        )
        return db
    except mysql.connector.Error as err:
        print(f"Ошибка подключения к базе данных: {err}")
        return None


# Путь к CSV файлу
file_path = os.path.join(base_path, 'homework', 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

# Чтение из CSV файла
data_from_csv = []
with open(file_path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        data_from_csv.append(row)

missing_data = []
conn = connect_to_db()

# Вывод отсутствующих данных
if missing_data:
    print("Данные, которых не хватает в базе данных:")
    for table_name, row in missing_data:
        print(f"Таблица: {table_name}, Данные: {row}")
else:
    print("Все данные из CSV файла присутствуют в базе данных.")
