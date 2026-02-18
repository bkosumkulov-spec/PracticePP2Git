#201 leap year
# year = int(input())
# if year % 4 == 0 and year % 100 > 1 or year % 400 == 0:
#     print("YES")
# else:
#     print("NO")    

#202 Sum
# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)    

#203 Sum of numbers
# n = int(input())
# sum = 0
# for i in range(0,n):
#     x = int(input())
#     sum += x
# print(sum)    
    
# n = int(input())
# sum = 0
# numbers = list(map(int, input().split())) 
# i = 0
# while i < n:
#     sum += numbers[i]
#     i += 1
# print(sum)    

#204 Positive numbers
# n = int(input())
# count = 0
# numbers = list(map(int, input().split()))   
# for i in range(0,n):
#     if numbers[i] > 0:
#         count += 1
# print(count)

#205 Is it the power of two
# n = int(input())

# if n <= 0:
#     print("NO")
# else:
#     while n % 2 == 0:
#         n //= 2
#     print("YES" if n == 1 else "NO")

#206 Maximum number
# n = int(input("n = "))
# max = -1000000000
# for i in range(0,n):
#     x = int(input("x = "))
#     if x > max:
#         max = x
# print(max)        
        
# n = int(input())
# sequence = list(map(int, input().split()))
# max = seq[0]
# for i in range(0,n):
#     if sequence[i] > max:
#         max = sequence[i]
# print(max)

#207 Position of maximum
# n = int(input("n = "))
# seq = list(map(int, input().split()))
# max = -1000000000000000000
# pos = -1
# for i in range(0,n):
#     if seq[i] > max:
#         max = seq[i]
#         pos = i + 1   
# print(pos)   
  
# n = int(input())
# seq = list(map(int, input().split()))
# max = max(seq)
# pos = seq.index(max)
# print(pos + 1)

#208 2Power
# N = int(input())
# pow = 1
# res = []
# while N > 0:
#     res.append(str(pow))
#     N //= 2
#     pow *= 2
# print(' '.join(res))

#209 MaxToMin
# n = int(input())
# a = list(map(int, input().split()))
# mn = min(a)
# mx = max(a)
# for i in range(0,n):
#     if a[i] == mx:
#         a[i] = mn
# print(' '.join(map(str,a)))

#210 Sort
# n = int(input())
# a = list(map(int, input().split()))
# a.sort(reverse=True)
# print(' '.join(map(str, a)))
        
#211 Reverse elements from exttt{l} to exttt{r}
# n,l,r= map(int, input().split())
# if (l > n or r > n) or r < l:
#     print("SGL")
# a = list(map(int, input().split()))
# a[l-1:r] = a[l-1:r][::-1]
# print(*a)

# n,l,r= map(int, input().split())
# if (l > n or r > n) or r < l:
#     print("SGL")
# a = list(map(int, input().split()))
# b = sorted(a[l - 1:r], reverse = True)
# a[l - 1: r] = b
# print(*a)

#212 Square
# n = int(input())
# a = list(map(int, input().split()))
# for i in range(0,n):
#     a[i] *= a[i]
# print(' '.join(map(str, a)))   

#213 Is it Prime?
# def is_prime(x):
#     if x <= 1:
#         return False
#     if x == 2:
#         return True
#     if x % 2 == 0:
#         return False
#     i = 3
#     while i * i <= x:
#         if x % i == 0:
#             return False
#         i += 2
    
#     return True
# x = int(input())
# if is_prime(x):
#     print("Yes")
# else:
#     print("No")       
        
#214 Most Frequent Element
# n = int(input())
# a = list(map(int, input().split()))
# max_cnt = 0
# ans = a[0]
# for i in range(0,n):
#     count = 0
#     for j in range(0,n):
#         if a[i] == a[j]:
#             count += 1
#     if count > max_cnt:
#         max_cnt = count
#         ans = a[i]
#     elif count == max_cnt:
#         if a[i] < ans:
#             ans = a[i]            
# print(ans)                           
             
# 215 Attendance 
# n = int(input())
# surnames = set()
# for _ in range(n):
#     surname = input().strip()   
#     surnames.add(surname)
# print(len(surnames))
    
#216 Newbie    
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    is_new = True
    for j in range(i):          
        if a[j] == a[i]:
            is_new = False
            break
    print("YES" if is_new else "NO")

#217 Contacts
# from collections import Counter

# n = int(input())
# numbers = [input().strip() for _ in range(n)]
# print(sum(1 for v in Counter(numbers).values() if v == 3))     
    
#218 Strings
# n = int(input())
# seen = {}
# order = []
# for i in range(1, n + 1):
#     s = input().strip()
#     if s not in seen:
#         seen[s] = i
#         order.append(s)
# order.sort()
# for s in order:
#     print(s, seen[s])
 
#219 Aida and korean serials
# n = int(input())
# d = {}
# for _ in range(n):
#     name, k = input().split()
#     k = int(k)
#     if name in d:
#         d[name] += k
#     else: 
#         d[name] = k        
# for name in sorted(d):
#     print(name, d[name])

#220 Mongo DB
# n = int(input())
# a = []
# for i in range(n):
#     x = input()
#     a.append(x)
# print(a)    