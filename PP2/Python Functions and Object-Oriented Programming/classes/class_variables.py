# Пример 1
class Employee:
    company = "TechCorp"           # классовая переменная
    raise_percent = 12
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def apply_raise(self):
        self.salary *= (1 + Employee.raise_percent / 100)

e1 = Employee("Азамат", 350000)
e1.apply_raise()
print(e1.salary)

# Пример 2
class Student:
    university = "KBTU"
    count = 0
    
    def __init__(self, name):
        self.name = name
        Student.count += 1

s1 = Student("Аружан")
s2 = Student("Данияр")
print(Student.count, "студентов")
print(s1.university)

# Пример 3 — константа класса
class Color:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"

print(Color.RED + "Ошибка!" + Color.RESET)

# Пример 4
class Game:
    version = "1.2.3"
    players_online = 0
    
    def __init__(self, nickname):
        self.nickname = nickname
        Game.players_online += 1

g1 = Game("Noob")
g2 = Game("Pro")
print("Игра:", Game.version, "| Онлайн:", Game.players_online)

# Пример 5
class Circle:
    PI = 3.14159
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return Circle.PI * self.radius ** 2

c = Circle(10)
print("Площадь:", round(c.area(), 2))