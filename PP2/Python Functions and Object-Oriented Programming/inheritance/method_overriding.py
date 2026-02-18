# Пример 1
class Bird:
    def fly(self):
        print("Лечу!")

class Penguin(Bird):
    def fly(self):
        print("Я пингвин, я плаваю лучше...")

p = Penguin()
p.fly()

# Пример 2
class Payment:
    def process(self, amount):
        print(f"Обработка {amount} ₸")

class CardPayment(Payment):
    def process(self, amount):
        print(f"Оплата картой {amount} ₸ → успешно")

cp = CardPayment()
cp.process(25000)

# Пример 3
class Animal:
    def eat(self):
        print("Ем еду...")

class Dog(Animal):
    def eat(self):
        print("Ем кости!")

d = Dog()
d.eat()

# Пример 4
class Logger:
    def log(self, msg):
        print("[LOG]", msg)

class TimedLogger(Logger):
    def log(self, msg):
        from datetime import datetime
        print(f"[{datetime.now().strftime('%H:%M:%S')}]", msg)

tl = TimedLogger()
tl.log("Запуск сервера")

# Пример 5
class Vehicle:
    def max_speed(self):
        return 0

class SportCar(Vehicle):
    def max_speed(self):
        return 320

sc = SportCar()
print("Макс. скорость:", sc.max_speed(), "км/ч")