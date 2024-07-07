from datetime import datetime

date_str = "Jan 15, 2023 - 12:05:33"

# Преобразуем строку
date_obj = datetime.strptime(date_str, "%b %d, %Y - %H:%M:%S")

# Полное название месяца
full_month_name = date_obj.strftime("%B")

print("Полное название месяца:", full_month_name)

# Распечатаем дату в формате "15.01.2023, 12:05"
formatted_date = date_obj.strftime("%d.%m.%Y, %H:%M")
print("Дата в нужном формате:", formatted_date)
