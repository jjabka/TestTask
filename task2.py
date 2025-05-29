from datetime import datetime

input_date = input("Введите дату (ДД.ММ.ГГГГ): ")
date = datetime.strptime(input_date, '%d.%m.%Y')

days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #последние дни каждого месяца

if date.year % 400 == 0: #проверка на високосный год
    days_month[1] == 29

days_input_month = days_month[date.month - 1]
first_day = date.replace(day = 1)
last_day = date.replace(day = days_input_month)
month = date.month

print(f'Первый день месяца: {first_day.strftime("%d.%m.%Y")}')
print(f'Последний день месяца: {last_day.strftime("%d.%m.%Y")}')
print(f'Месяц: {month}')
