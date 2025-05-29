person_date_time = input("Введите дату и время (ДД.ММ.ГГГГ  ЧЧ:ММ:CC): ")
data_part = person_date_time.split()
cut_time = data_part[1].split(":")
cut_time[0] = '10'
cut_time.pop(2)
new_time = ":".join(cut_time)
data_part.pop(1)
data_part.insert(1, new_time)
print(" ".join(data_part))