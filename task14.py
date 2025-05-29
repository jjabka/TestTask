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

sorted_by_name = sorted(orders, key=lambda x: x[0])
print("Сортировка по товару:")
for item in sorted_by_name:
    print(item)

sorted_by_sum = sorted(orders, key=lambda x: x[1] * x[2])
print("Сортировка по сумме (кол-во * цена):")
for item in sorted_by_sum:
    print(item)