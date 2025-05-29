# 9. Создайте класс. Пусть в нем будут поля Фамилия, Имя, Год рождения.
#  10. Создайте метод, который выводит ФИО.
#  11. Создайте метод, который вычисляет возраст в годах.

class Person():
    def __init__(self, surname, name, middle_name, year):
        self.surname = surname
        self.name = name
        self.middle_name = middle_name
        self.year = year

    def get_fullname(self):
        return f"{self.surname} {self.name} {self.middle_name}"
   
    def true_age(self):
        return 2025 - self.year


person = Person("Мартин", "Ева", "Александровна", 2004)
print(person.get_fullname())
print(person.true_age())