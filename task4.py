from datetime import datetime

start_date = input('Введите первую дату (ДД.ММ.ГГГГ ЧЧ:ММ): ')
end_date = input('Введите вторую дату (ДД.ММ.ГГГГ ЧЧ:ММ): ')

d_start = datetime.strptime(start_date, "%d.%m.%Y %H:%M")
d_end = datetime.strptime(end_date, "%d.%m.%Y %H:%M")

difference = d_end - d_start
print("Разница в днях ", difference.total_seconds() // 86400)
print("Разница в часах ", difference.total_seconds() // 3600)
print("Разница в минутах ", difference.total_seconds() // 60)
print("Разница в секундах ", difference.total_seconds())
