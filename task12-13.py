def str_decor(func):
    def wrapper(self):
        result = func(self)
        return f"<strong>{result}</strong>"
    return wrapper
class Person():
    def __init__(self, surname, name, middle_name, year):
        self.surname = surname
        self.name = name
        self.middle_name = middle_name
        self.year = year

    @str_decor
    def get_fullname(self):
        return f"{self.surname} {self.name} {self.middle_name}"
   
    def true_age(self):
        return 2025 - self.year


class newPerson(Person):
    def true_age(self):
        return ((2025 - self.year) * 365)

person = Person("Мартин", "Ева", "Александровна",2004)
print(person.get_fullname())
print(person.true_age())
person1 = newPerson("Мартин", "Саша", "Александровна", 1996)
print(person1.get_fullname())
print(person1.true_age())