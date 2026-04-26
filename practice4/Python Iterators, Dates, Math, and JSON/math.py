#Built-in Math Functions
# x = min(1,2,3,45,56)
# y = max(23,35,15,85,44)
# print(x + y)
# z = abs(-2345.333)
# print(z)
# r = round(23.33)
# print(r)
# print(pow(3,2))

#Math Module Functions
# import math
# x = math.sqrt(56)
# print(math.ceil(x))
# print(math.floor(x))

# y = math.pi + math.e
# print(y)

# s = math.sin(1)
# c = math.cos(2)
# print(s)
# print(c)

#Random module functions
import random 
print(random.random())

print(random.randint(100,1000))

s = ("2rfvkergfveh","23987484",2233444)
l = ["2132444",11111,"asdfghjk",[2,3]]
print(random.choice(s))
random.shuffle(l)
print(l)
