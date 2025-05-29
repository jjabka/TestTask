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

summary = {}

for item in orders:
    name, kol, price = item
    total = kol * price
    if name in summary:
        summary[name] += total
    else:
        summary[name] = total

print("Общая сумма по каждому товару:")
for name, cost in summary.items():
    print(f"{name}: {cost} руб.")