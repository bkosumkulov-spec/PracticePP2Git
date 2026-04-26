i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

n = 1
while n <= 15:
    if n % 3 == 0:
        n += 1
        continue
    print(n)
    n += 1

i = 0
while i < 20:
    i += 1
    if i == 5 or i == 10 or i == 15:
        continue
    print(i)

count = 1
while count <= 12:
    if count % 4 != 0:
        count += 1
        continue
    print(count)
    count += 1

x = -5
while x <= 5:
    x += 1
    if x == 0:
        continue
    print(x)