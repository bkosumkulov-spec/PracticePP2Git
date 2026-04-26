count = 0
while count < 100:
    count += 1
    if count == 50:
        break
    print(count)
    
password = ""
while True:
    password = input()
    if password == "exit":
        break
    print("try again")

n = 1
while True:
    if n > 20:
        break
    print(n)
    n += 2

i = 1
while i <= 10:
    if i == 7:
        break
    print(i)
    i += 1
    
i = 10
while i > 0:
    print(i)
    i -= 1
    if i == 3:
        break                