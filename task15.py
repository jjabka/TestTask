import datetime

def check_controller_1(good):
    return 1000 <= good['weight'] <= 1100

def check_controller_2(good):
    return 950 <= good['weight'] <= 1050

def check_day(date):
    day = date.day
    if day % 2 == 0:
        return check_controller_1
    else:
        return check_controller_2

def check_quality(date, goods): 
    check_function = check_day(date)
    passed_goods = [item for item in goods if check_function(item)]
    return passed_goods


today = datetime.date.today()

goods = [
    {"name": "Подарок", "weight": 950},
    {"name": "Подставка", "weight": 800},
    {"name": "Машинка", "weight": 1060},
    {"name": "Посуда", "weight": 1105},
]

valid_goods = check_quality(today, goods)

print("Продукция, прошедшая проверку:")
for good in valid_goods:
    print(f"{good['name']} весом {good['weight']} г")
