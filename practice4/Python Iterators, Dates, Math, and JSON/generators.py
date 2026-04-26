# Python Generators

#yield
# def my_generator():
#     yield 1
#     yield 2
#     yield 3
# for value in my_generator():
#     print(value)

#generator expressions
# gen_x = (x for x in range(5))     
# print(gen_x) 
# print(list(gen_x))

# gen_x = sum(x for x in range(10))
# print(gen_x)

# Create generator
# def count_to_n(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1
# for num in count_to_n(5):
#     print(num)

# gen = (count_to_n(5))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# Python Iterators
#next(),iter()
# my_tuple = ("zzz", "dddddd", 10000)
# simba = iter(my_tuple)
# print(next(simba))
# print(next(simba))
# print(next(simba))

# Loop through iterator
# my_tuple = ("123456765",00000000,"asdfghjhgf")
# for x in my_tuple:
#     print(x)

#Create an iterator
# class My_number:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a 
#         self.a += 1
#         return x
# my_class = My_number()
# myiter = iter(my_class)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))