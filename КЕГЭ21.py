# Пробник 21 >>>  27/29
# Идем с конца
"""

f = open('Задание_27_B__g57y.txt')
n = int(f.readline())

s = 0
diff = 10e16
for i in range(n):
    x, y = [int(i) for i in f.readline().split()]
    s += max(x, y)
    tmp = abs(x-y)
    if tmp % 2 != 0:
        diff = min(diff, tmp)
if s % 2 == 0:
    print(s)
else:
    print(s-diff)""" # 27
"""
c = 0
for i in range(164925, 623594 + 1):
    if i % 2 == 0:
        if i % 3 != 0:
            c += 1
    elif i % 3 == 0:
        c += 1
print(c)""" # 25
"""a = open('Задание_24__g57s.txt').readline()
char = ''
bebra = 0
maxim = -1000000
for i in range(len(a)):
    if a[i] in '13579':
        char += a[i]
        bebra = int(char)
        maxim = max(bebra, maxim)
    else:
        char = ''
        bebra = 0
print(maxim) # 7517 """ # 24
"""
from functools import lru_cache
@lru_cache(None)
def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x % 4 != 0 and x > 4:
        return f(x - 1, y) + f(x - 3, y) + f(x - x%4, y)
    return f(x - 1, y) + f(x - 3, y)
print(f(22,2))
""" # 23
"""for i in range(10000):
    x = i
    L = 0
    M = 1
    while x > 0:
        L += 1
        M *= x % 8
        x = x//8
    if L == 3 and M == 120:
        print(i)""" # 22
"""def moves(h):
    a, b = h
    return (a+2, b), (a*2, b), (a, b+2), (a, b*2)
from functools import lru_cache
@lru_cache(None)
def f(h):
    if sum(h) >= 75:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h)):
        return 'V2'

for s in range(1, 70):
    h = 9, s
    print(s,f(h))""" # 21-19
"""f = open('Задание_17__g57v.txt')
a = [int(i) for i in f]
sr = sum(a)/ len(a)
c = 0
maxim = -10000000
for i in range(len(a) - 2):
    if (a[i] > sr and a[i+1] > sr) or (a[i] > sr and a[i+2] > sr) or (a[i+1] > sr and a[i+2] > sr):
        if '7' in str(a[i]) or '7' in str(a[i+1]) or '7' in str(a[i+2]):
            c += 1
            maxim = max(maxim, a[i] + a[i+1] + a[i+2])
print(c, maxim)
# 3574 28715""" # 17
"""def f(n):
    if n == 0:
        return 0
    if n % 3 == 0 and n % 2 != 0 and n % 5 != 0:
        return 3 * f(n//3)
    if n % 3 != 0 and n % 2 == 0 and n % 5 != 0:
        return 2 * f(n//2)
    if n % 3 != 0 and n % 2 != 0 and n % 5 == 0:
        return 5 * f(n//5)
    return 2 * n
s = 0
for i in range(100000):
    if 1000 <= f(i) <= 3000:
        if i % 2 == 0:
            s += i
print(s) # 501000""" # 16
"""for A in range(-1000,100):
    gg = True
    for k in range(1,100):
        for n in range(1,100):
            f = ((5*k + 6*n > 57) or ((k <= A) and (n < A)))
            if f == 0:
                gg = False
                break
        if gg == False:
            break
    if gg == True:
        print(A)""" # 15
"""for N in range(6, 36):
    a = int('214',N)
    b = int('165',N+1)
    if int('214',N) == int('165',N+1):
        print(N)""" # 14
"""a = 0
b = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        for N in range(1, 100):
            a = 4 + N * x + N * 4 - 28
            b = 6 + N * y + N * 6 - 22
            if a == 0 and b == 0:
                print(x,y, N)""" # 12
"""for i in range(1,100):
    k = i
    n = 1
    s = 1
    while s + n < 130:
        s *= k
        n += 1
    if n == 4:
        print(i)""" # 6
"""for N in range(1,200):
    a = str(bin(N)[2:])
    a += str(a.count('1') % 2)
    a += str(a.count('1') % 2)
    R = int(a, 2)
    if R > 103:
        print(R)
        break""" # 5
"""print('x y z|f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = (((x <= (not y)) <= (not z)) == (x and not y))
            if f == 1:
                print(x,y,z,int(f))""" # 2



