orders = [
    ["Косметика", 2, 500],
    ["Еда", 5, 1200],
    ["Обувь", 1, 300],
    ["Косметика", 3, 450],
    ["Обувь", 4, 800],
    ["Еда", 2, 1100],
    ["Штаны", 6, 150],
    ["Куртки", 1, 2000],
    ["Обувь", 2, 350],
    ["Штаны", 10, 100],
    ["Обувь", 1, 850],
    ["Куртки", 7, 90],
]

seen = []
list1 = []
list2 = []
flag = True 

for item in orders:
    name = item[0]
    if name not in seen:
        seen.append(name)
        if flag:
            list1.append(name)
        else:
            list2.append(name)
        flag = not flag

print("Уникальные товары (группа 1):", list1)
print("Уникальные товары (группа 2):", list2)


for item in list2:
    if item not in list1:
        list1.append(item)

for item in list1:
    if item not in list2:
        list2.append(item)

set1 = set(list1)
set2 = set(list2)

union = set1 | set2   #Объединение
intersection = set1 & set2 #Пересечение

print("Обновлённый список 1:", list1)
print("Обновлённый список 2:", list2)
print("Множество 1:", set1)
print("Множество 2:", set2)
print("Объединение:", union)
print("Пересечение:", intersection)