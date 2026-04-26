# Пример 1 — классика
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

d = Dog("Бобик", 4, "Овчарка")
print(d.name, d.age, d.breed)

# Пример 2
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
    
    def total(self):
        return self.salary + self.bonus

m = Manager("Айгуль", 600000, 150000)
print("Всего:", m.total())

# Пример 3
class Figure:
    def __init__(self, color):
        self.color = color

class Triangle(Figure):
    def __init__(self, color, a, b, c):
        super().__init__(color)
        self.sides = [a, b, c]

t = Triangle("Красный", 3, 4, 5)
print(t.color, t.sides)

# Пример 4 — вызов метода суперкласса
class Printer:
    def print_doc(self, text):
        print("Обычная печать:", text)

class ColorPrinter(Printer):
    def print_doc(self, text):
        super().print_doc(text)
        print("...с цветными чернилами!")

cp = ColorPrinter()
cp.print_doc("Отчёт")

# Пример 5
class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

class Smartphone(Battery):
    def __init__(self, brand, capacity, ram):
        super().__init__(capacity)
        self.brand = brand
        self.ram = ram

s = Smartphone("Xiaomi", 5000, 8)
print(s.brand, s.capacity, "mAh,", s.ram, "GB RAM")