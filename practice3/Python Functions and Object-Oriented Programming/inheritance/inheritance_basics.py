# Пример 1
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Какой-то звук...")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} гавкает!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} мяукает!")

d = Dog("Рекс")
c = Cat("Мурка")
d.speak()
c.speak()

# Пример 2
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def move(self):
        print("Транспорт движется")

class Car(Vehicle):
    def move(self):
        print(f"{self.brand} едет по дороге")

class Boat(Vehicle):
    def move(self):
        print(f"{self.brand} плывёт по воде")

c = Car("Honda")
b = Boat("Yamaha")
c.move()
b.move()

# Пример 3 — без переопределения
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, position):
        super().__init__(name)
        self.position = position

e = Employee("Ерлан", "Разработчик")
print(e.name, e.position)

# Пример 4
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

s = Square(7)
print("Площадь квадрата:", s.area())

# Пример 5
class Device:
    def turn_on(self):
        print("Устройство включено")

class Phone(Device):
    def call(self):
        print("Звоню...")

p = Phone()
p.turn_on()
p.call()