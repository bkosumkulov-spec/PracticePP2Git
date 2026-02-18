class Flyer:
    def fly(self):
        print("Я лечу!")

class Swimmer:
    def swim(self):
        print("Я плаваю!")

class Duck(Flyer, Swimmer):   # наследуется от двух классов
    def quack(self):
        print("Кря-кря!")

d = Duck()
d.fly()     # Я лечу!
d.swim()    # Я плаваю!
d.quack()   # Кря-кря!