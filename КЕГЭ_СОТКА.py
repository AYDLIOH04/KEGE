"""
for i in range(1, 128):
    s = bin(i)[2:]
    a = '0' * (8 - len(s)) + s
    ans = ''
    for j in a:
        if j == '1':
            ans += '0'
        else:
            ans += '1'
    ans = bin(int(ans, 2) + 1)[2:]
    if int(ans, 2) == 156:
        print(i)""" # 5
"""
for i in range(1, 1000):
    k = i
    n = 1000
    s = -1000
    while s+n < 500:
        n = n + k*5
        s = s + n
    if s == 500:
        print(i)""" # 6
"""a = 2.15 * 1024 * 1024 * 1024
b = 2 * 12000 * 16
print((a/b)//60)""" # 7
"""
a = '1' + '2' * 22
while '000' in a or '222' in a:
    if '000' in a:
        a = a.replace('000', '2', 1)
    else:
        a = a.replace('222', '0', 1)
print(a)""" # 12
"""for A in range(1, 100):
    gg = True
    for k in range(1, 100):
        for n in range(1, 100):
            f = (5*k + 6*n > 57) or ((k <= A) and (n < A))
            if f == 0:
                gg = False
                break
        if gg == False:
            break
    if gg:
        print(A)""" # 15
"""from sys import setrecursionlimit
setrecursionlimit(2000)
def f(n):
    if n < -1000:
        return 1
    if n > 1:
        return -f(n-1) - f(n-3)
    return -f(n-1)
print(f(14))
""" # 16
"""f = open('Задание_17__iob5 (1).txt')
a = [int(i) for i in f]

c = 0
maxim = -10000000
n = len(a)
for i in range(n - 1):
    if (a[i] + a[i+1]) % 2 == 0 and (a[i]*a[i+1]) % 2 != 0:
        c += 1
        maxim = max(maxim, a[i] + a[i+1])
print(c, maxim)""" # 17
"""def moves(h):
    a, b = h
    return (a+1, b), (a, b+1), (a+b*2, b), (a, b+a*2)

from functools import lru_cache
@lru_cache(None)
def f(h):
    if sum(h) >= 84:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'

for s in range(1, 78):
    h = 8, s
    print(s, (f(h)))""" # 19-21
"""for i in range(1, 1000):
    x = i
    L = 0
    M = 0
    while x > 0:
        L += 1
        if x % 2 == 0:
            M += (x%10)
        x //= 10
    if L == 3 and M == 0:
        print(i)""" # 22
"""def g(s,f):
    if s == f:
        return 1
    if s > f or s == 15:
        return 0
    return g(s+1, f) + g(s*2, f)
print(g(3, 10) * g(10, 45))""" # 23
"""a = open('Задание_24__iob7.txt').readline()
dlina, c, symb = 0, 1, ''
for i in range(len(a) - 1):
    if a[i] == a[i+1]:
        c += 1
        if c > dlina:
            dlina = c
            symb = a[i]
    else:
        c = 1
print(symb, dlina)""" # 24
"""def count_div(n):
    c = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                c += 1
            if i != n//i and (n//i) % 2 == 0:
                c += 1
    return c

counter = 0
for i in range(135792, 139448 + 1):
    if count_div(i) == 6:
        counter += 1
print(counter)""" # 25
"""
k15 = 0
k5 = 0
k3 = 0
nk = 0

f = open('Задание_27_B__iobc.txt')
maxim = 0

for i in range(int(f.readline())):
    x = int(f.readline())
    if x % 15 == 0:
        maxim = max(maxim, k15*x, k5*x, k3*x, nk*x)
        k15 = max(k15, x)
    elif x % 5 == 0:
        maxim = max(maxim, k15 * x, k3 * x)
        k5 = max(k5, x)
    elif x % 3 == 0:
        maxim = max(maxim, k15 * x, k5 * x)
        k3 = max(k3, x)
    else:
        maxim = max(maxim, k15*x)
        nk = max(nk, x)
print(maxim)""" # 27







