#301 Valid Number
# n = int(input())
# while n != 0:
#     is_true = True
#     if (n % 10) % 2 != 0:
#         is_true = False 
#         break
#     n = n // 10
# print("Valid" if is_true else "Not valid") 

#302 Is a number Usual
# def isUsual(num: int) -> bool:
#     while num % 2 == 0:
#         num //= 2
#     while num % 3 == 0:
#         num //= 3
#     while num % 5 == 0:
#         num //= 5
#     return num == 1
# n = int(input())
# if isUsual(n):
#     print("Yes")
# else:
#     print("No")    

#303 String calculator with functions
# triplets = {
#     "ZER": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOU": 4,
#     "FIV": 5, "SIX": 6, "SEV": 7, "EIG": 8, "NIN": 9
# }

# num_to_triplet = {v: k for k, v in triplets.items()}

# def parse_number(s, pos):
#     triplet = s[pos:pos+3]
#     return triplets.get(triplet, 0), pos + 3

# s = input().strip()
# i = 0
# n = len(s)

# a, i = parse_number(s, i)
# op = s[i]
# i += 1
# b, i = parse_number(s, i)

# if op == '+':
#     res = a + b
# elif op == '-':
#     res = a - b
# elif op == '*':
#     res = a * b
# else:
#     res = 0

# if res == 0:
#     print("ZER")
# else:
#     result = ""
#     while res > 0:
#         digit = res % 10
#         result = num_to_triplet[digit] + result
#         res //= 10
#     print(result)  
    
#304            
# class stringhandler:
#     def getstring(s):
#         s.text = input()  
#     def printstring(s):
#         print(s.text.upper())              
# handler = stringhandler()
# handler.getstring()
# handler.printstring()
        
#305 
# class Shape:
#     def area(self):
#         return 0
# class Square(Shape):
#     def __init__(self,length):
#         self.length = length
#     def area(self):
#         return self.length * self.length
# a = int(input())
# sq = Square(a)
# print(sq.area())    
    
        
#306 
# class Shape():
#     def area(self):
#         return 0
# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length = length 
#         self.width = width
#     def area(self):
#         return self.length * self.width 
# a,b = map(int, input().split())
# q = Rectangle(a,b)  
# print(q.area())        

#307
# import math
# class Point():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def show(self):
#         print(f"({self.x}, {self.y})")
#     def move(self,new_x, new_y):
#         self.x = new_x
#         self.y = new_y
#     def dist(self, other_point):
#         dx = self.x - other_point.x
#         dy = self.y - other_point.y
#         return math.sqrt(dx**2 + dy**2)
# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
# x3, y3 = map(int, input().split())
# p1 = Point(x1,y1)
# p1.show()
# p1.move(x2,y2)
# p1.show()
# p2 = Point(x3, y3)
# distance = p1.dist(p2)
# print(f"{distance:.2f}")

#308 
# class Account:
#     def deposit(self, amount):
#             self.deposit = amount 
#     def withdraw(self, amount):
#         self.withdraw = amount
#         if self.deposit < self.withdraw:
#             print("Insufficient Funds")
#         else:
#             print(self.deposit - self.withdraw)    
# a,b = map(int,input().split())
# acc = Account()
# acc.deposit(a)
# acc.withdraw(b)

#309 
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         pi = 3.14159
#         return pi * self.radius * self.radius
# a = int(input())
# pi = 3.14159
# circ = Circle(a)
# circs = circ.area()
# print(f"{circs:.2f}")

class Person:
    



                           
        
        
        
            

      
    