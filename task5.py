from datetime import datetime

start_date = input('Введите начальную дату (ДД.ММ.ГГГГ ЧЧ:ММ): ')
end_date = input('Введите конечную дату (ДД.ММ.ГГГГ ЧЧ:ММ): ')
checked = input('Введите проверяемую дату (ДД.ММ.ГГГГ ЧЧ:ММ): ')

d_start = datetime.strptime(start_date, "%d.%m.%Y %H:%M")
d_end = datetime.strptime(end_date, "%d.%m.%Y %H:%M")
d_check = datetime.strptime(checked, "%d.%m.%Y %H:%M")

inside = d_start <= d_check <= d_end

print("Дата внутри интервала." if inside else "Дата вне интервала.")
