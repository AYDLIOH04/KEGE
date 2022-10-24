# Cython++
# include <iostream>
import abc
import configparser
import difflib
import time

"""for n in range(100, 1000):
    mv = [i for i in str(n)]
    mv.sort()
    a = mv[2] + mv[1]
    if mv[0] == '0':
        b = mv[1] + mv[0]
    else:
        b = mv[0] + mv[1]
    if abs(int(b) - int(a)) == 58:
        print(n)
"""


def timer(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end - start)

    return wrapper


# Задание 5
"""for N in range(10000,99999 + 1):
    s = [int(i) for i in str(N)]
    a = s[0] + s[2] + s[4]
    b = s[1] + s[3]
    arr = []
    arr.append(a)
    arr.append(b)
    arr.sort()
    ans = int(str(arr[0]) + str(arr[1]))
    if ans == 723:
        print(N)"""  # 3
"""from itertools import product
for i in product('12456B', repeat=4):
    l = ''.join(i)
    s = [int(j, 12) for j in l]
    a = s[0] + s[2]
    b = s[1] + s[3]
    if a < b: # сортируем
        a, b = b, a
    if (a == int('1', 12) and b == int('15', 12)) or (a == int('11', 12) and b == int('5', 12)):
        print(l)"""  # 5
"""for N in range(1, 10000):
    a = bin(N)[2:]
    if N % 2 == 0:
        a = a + '00'
    else:
        a = a + '11'
    ans = int(a, 2)
    if ans < 115:
        print(N)"""  # 7
"""for N in range(1, 1000):
    s = bin(N)[2:]
    ss = s + s[-1]
    sss = ss + str(int(s.count('1') % 2 != 0)) + '0'
    ans = int(sss, 2)
    if ans < 160:
        print(N)"""  # 8
"""@timer
def f():
    for N in range(1000, 10000000):
        s = bin(N)[2:]
        ss = s[::-1]
        ans = int(ss, 2)
        if ans == 23:
            print(N)
f()"""  # 9
"""for N in range(256):
    print()
    print(N)
    s = bin(N)[2:]
    print(s)
    ss = '0' * (8 - len(s)) + s
    print(ss)
    sss = ss[:2] + ss[6:]
    print(sss)
    print()
    if int(sss, 2) == 10 and N < 130:
        print(N)
"""  # 10
"""masiv = set()
for N in range(10, 2501):
    a = bin(N)[2:]
    s = a.replace('0', '')
    masiv.add(s)
print(masiv)
print(len(masiv))"""  # 11
"""for N in range(1,1000):
    a = bin(N)[2:]
    b = ['1']
    for i in range(1, len(a)):
        if a[i] == '1':
            b.append('0')
        else:
            b.append('1')
    s = int(''.join(b), 2)
    if N + s > 123:
        print(N)"""  # 12
"""for N in range(1, 100):
    a = bin(N)[2:]
    s = a + str(int(a.count('1') > a.count('0')))
    ans = int(s, 2)
    if ans > 100:
        print(ans)"""  # 13
"""masiv = set()
for N in range(1, 100):
    a = bin(N)[2:]
    s = a + str(a.count('1') % 2)
    ss = s + str(s.count('1') % 2)
    ans = int(ss, 2)
    if 210 <= ans <= 260:
        masiv.add(ans)
print(masiv)
print(len(masiv))"""  # 14
"""maxim = 0
minim = 0
for N in range(100, 999):
    a = [int(i) for i in str(N)]
    a.sort()
    a.reverse()
    maxim = int(str(a[0]) + str(a[1]))

    if a[-1] != 0:
        minim = int(str(a[-1]) + str(a[-2]))
    else:
        if a[-2] != 0:
            minim = int(str(a[-2]) + str(a[-1]))

    if maxim - minim == 14:
        print(N)
"""  # 15

"""4 6 2 5 3 30
4 3 8 2 11 12
6 3 11 10 1 27
2 8 11 4 3 10
5 2 10 4 4 1
3 11 1 3 4 2
30 12 27 10 1 2

maxim = -10e16
minim = 10e16

a = [[0 for j in range(7)] for i in range(7)]
for i in range(7):
    a[i] = [int(j) for j in input().split()]
    a[i].insert(i, 0) # Вставляю нулик перед итым элементом

for i1 in range(1, 7):
    for i2 in range(1, 7):
        for i3 in range(1, 7):
            for i4 in range(1, 7):
                for i5 in range(1, 7):
                    for i6 in range(1, 7):
                        if i1 != i2 and i1 != i3 and i1 != i4 and i1 != i5  \
                                    and i2 != i3 and i2 != i4 and i2 != i5 \
                                    and i3 != i4 and i3 != i5  \
                                    and i4 != i5:
                            s6 = a[0][i1] + a[1][i2] + a[2][i3] + a[3][i4] + a[4][i5]
                            s7 = a[0][i1] + a[1][i2] + a[2][i3] + a[3][i4] + a[4][i5] + a[5][i6]
                            if i5 == 6:
                                if a[0][i1] > 0 and  a[1][i2] > 0 and  a[2][i3] > 0 and a[3][i4] > 0 and a[4][i5] > 0:
                                    maxim = max(maxim, s6)
                                    minim = min(minim, s6)
                            if i6 == 6:
                                if a[0][i1] > 0 and a[1][i2] > 0 and a[2][i3] > 0 and a[3][i4] > 0 and a[4][i5] > 0 and a[5][i6] > 0:
                                    maxim = max(maxim, s7)
                                    minim = min(minim, s7)

print(minim, maxim)"""  # ДИЧЬ

# 14
"""def perevod(num, CC): # до 16 СС
    s = ''
    while num > 0:
        l = str(num % CC)
        if l == '10':
            l = 'A'
        elif l == '11':
            l = 'B'
        elif l == '12':
            l = 'C'
        elif l == '13':
            l = 'D'
        elif l == '14':
            l = 'E'
        elif l == '15':
            l = 'F'
        s = l + s
        num //= CC
    return s"""  # ПЕРЕВОД
"""def perevodik(n, CC):
    s = []
    while n > 0:
        s.append(n%CC)
        n //= CC
    return s

for N in range(2, 36):
    a = N**25 - 2*N**13 + 10
    b = perevodik(a, N)[::-1]
    if sum(b) == 75:
        print(N)"""  # сумма разрядов 75
"""for N in range(5, 37):
    for x in range(-300, 300):
        if (x**2 - int('30', N) * x + int('240', N)) == 0:
            if int('30', N)**2 - 4 * int('240', N) == 0:
                print(N, x)
"""  # 14 Кратный корень
"""minim = 10e16
maxim = -10e16
for x in range(1, 100):
    for y in range(1, 100):
        a = ((3 + 2 * 4**x) * 4**x + 3 + 4**y)
        summa = 0
        while a > 0:
            summa += a % 4
            a //= 4
        maxim = max(maxim, summa)
        minim = min(minim, summa)
print(minim, maxim)"""  # Max and Min
"""
def perevod(num, CC):
    s = ''
    while num > 0:
        s = str(num % CC) + s
        num //= CC
    return s

c, minim, maxim = 0,0,0
for i in range(1, 10000):
    x = i
    s = perevod(x, 9)
    if len(s) == 3 and s.count('3') >= 1:
        xx = i*3
        ss = perevod(xx, 9)
        if len(ss) == 3:
            if c == 0:
                minim = x
            c += 1
            maxim = x
ans = minim + maxim
print(perevod(ans, 9))
"""  # 14.6
"""x = 16**int('25', 8) + 4**int('24', 16) - 8**(int('43', 8) - int('1B', 16)) - 2**(int('110101', 2) + int('13', 8)) + 31
a = perevod(x, 16)
ans = [0]*16
print(x, a)
for i in a:
    ans[int(i, 16)] += 1
print(ans)
ans = [i for i in ans if i != 0]
print(ans)
print(ans[0] + ans[-1])"""  # 14.7
"""x = 2**51 + 2**40 + 2**35 + 2**17 - 2**5
a = hex(x)[2:]
ans = []
for i in a:
    if i not in ans:
        ans.append(i)
print(len(ans))"""  # 14.8
"""a = 3456
ans = []
for i in range(2, 11):
    x = perevod(a, i)
    if all(int(j) % 2 == 0 for j in x):
        ans.append(i)
print(ans, sum(ans))"""  # 14.11
"""maxim = 0
char = 0
a = 456
for i in range(2, 11):
    x = perevod(a, i)
    if len([j for j in x if int(j) % 2 != 0]) >= maxim:
        maxim = len([j for j in x if int(j) % 2 != 0])
        char = i
print(char)"""  # 14.12

# 15
"""P = [i for i in range(192, 256)]
Q = [i for i in range(256) if i % 2 == 0]
A = set()
for x in range(256):
    f = ((x not in A) <= ((x in P) or (x not in Q)))
    if f == 0:
        A.add(x)
print(len(A))"""  # 2
"""P = set(i for i in range(2, 21, 2))
Q = set(i for i in range(3, 31, 3))
A = set()
for x in range(1, 40):
    f = ((x in P) <= (x in A)) or ((x not in A) <= (x not in Q))
    if f == 0:
        A.add(x)
print(A, len(A))"""  # Множество
"""c = 0
for R in range(1, 2000):
    gg = True
    for A in range(1, 2000):
        for x in range(1, 2000):
            f = ((((x & 54 == 0) or (x & 45 == 0)) <= (x & A == 0)) or (x & R == 0))
            if f == 0:
                gg = False
                break
        if gg == False:
            break
    if gg == True:
        c += 1
print(c)

"""  # x, A, R
"""for A in range(1, 1000):
    gg = True
    for x in range(1, 1000):
        f = ((x & A == 0) or ((x & 69 == 4) <= (x & 118 == 6)))
        if f == 0:
            gg = False
            break
    if gg == True:
        print(A)"""  # 5
"""for A in range(1, 1000):
    gg = True
    for x in range(1, 1000):
        f = (x & A != 0) and (x & 58 == 0) and (x & 22 == 0)
        if f == 1:
            gg = False
            break
    if gg == True:
        print(A)"""  # 6
"""D = [155, 177]
B = [111, 130]
nimnim = 100000000
lena = 400
for A1 in range(1, lena):
    for A2 in range(A1+1, lena):
        gg = True
        for x in range(1, lena):
            x += 0.1
            f = (D[0] <= x <= D[1]) <= ((not(B[0] <= x <= B[1]) and (not(A1 <= x <= A2))) <= (not(D[0] <= x <= D[1])))
            if f == 0:
                gg = False
                break
        if gg == True:
            nimnim = min(nimnim, A2-A1)
print(nimnim)
"""  # 7
"""c = 0
for A in range(1000):
    gg = True
    for x in range(200):
        for y in range(200):
            f = (((x-10)*(x+1) <= 0) and (x*x > A)) or ((y*y <= A) and ((y-10)*(y+1) > 0))
            if f == 1:
                gg = False
                break
        if gg == False:
            break
    if gg == True:
        c += 1
print(c)"""  # 8
"""maxim = -100000000
nimnim = 100000000
for A1 in range(-200, 200):
    for A2 in range(A1+1, 200):
        gg = True
        for x in range(-200, 200):
            f = ((A1 <= x <= A2) <= (x**2 + 10*x <= 144)) and ((x**2 + 6*x <= 112) <= (A1 <= x <= A2))
            if f == 0:
                gg = False
                break
        if gg == True:
            maxim = max(maxim, A2-A1)
            nimnim = min(nimnim, A2-A1)
print(nimnim, maxim)"""  # 9
"""A1, A2 = 30, 50
B1, B2 = 40, 46
C2 = 61
for N in range(1, 61):
    c = 0
    for x in range(1, 100):
        f = ((not(B1 <= x <= B2)) <= (not(A1 <= x <= A2))) and ((not(N <= x <= C2)) <= (B1 <= x <= B2))
        if f == 1:
            c += 1
    if c > 25:
        print(N,c)"""  # 10
"""for A in range(1, 1000):
    gg = True
    for x in range(1, 100):
        for y in range(1, 100):
            f = (50 > x) and (144 >= 4*y - 3*x) and (A**2 < (x-25)**2 + (y - 25)**2)
            if f == 1:
                gg = False
                break
        if gg == False:
            break
    if gg == True:
        print(A)
"""  # 11
"""for A in range(1, 500):
    for B in range(1, 500):
        gg = True
        for x in range(1, 500):
            for y in range(1, 500):
                f = (y <= ((x - 4)**2 + 2 + abs((x - 2)**2 - 16) )) == ((y <= 2*x**2 - 12*x + A) or (y <= -4*x + B))
                if f == 0:
                    gg = False
                    break
            if gg == False:
                break
        if gg == True:
            print(A,B, A+B)"""  # 12

# 16
"""def f(n):
    if n < 0: return -n
    if n % 2 == 0: return 2*n + 1 + f(n-3)
    return 4*n + 2*f(n-4)
print(f(33))"""  # 1
"""def f(n):
    if n == 1: return 1
    return 3*f(n-1) - g(n) - n + 5

def g(n):
    if n == 1: return 1
    return f(n-1) + 3 * g(n-1) - 3*n
print(f(5) + g(5))"""  # 2
"""def f(n):
    global c
    c += 1
    if n >= 1:
        c += 1
        f(n-1)
        f(n-3)
        c += 1
c = 0
f(40)
print(c)"""  # 3
"""def f(n):
    global c
    c += 1
    if n >= 1:
        c += 1
        f(n-1)
        f(n//3)
        c += 1
c = 0
f(280)
print(c)"""  # 4
"""def f(n):
    global c
    c += 1
    if n >= 1:
        c += 1
        f(n-1)
        f(n//2)
c = 0
f(140)
print(c)"""  # 5
"""def f(n):
    global c
    c += n + 1
    if n > 1:
        c += n+5
        f(n-1)
        f(n-2)

for n in range(1, 100000):
    c = 0
    f(n)
    if c > 1000000:
        print(n, c)"""  # 6
"""def f(n):
    global c
    c += 2*n + 1
    if n > 1:
        c += 3*n - 8
        f(n-1)
        f(n-4)

for n in range(1, 100000):
    c = 0
    f(n)
    if c > 5000000:
        print(n, c)"""  # 7
"""def f(n):
    global c
    c += n*n
    if n > 1:
        c += 2*n + 1
        f(n-2)
        f(n//3)
for n in range(1, 1000):
    c = 0
    f(n)
    if c > 3200000:
        print(n, c)"""  # 8
"""def f(n):
    if n <= 1: return n
    if n > 1 and n % 3 == 0: return n + f(n/3)
    return -10000

for n in range(1, 500):
    if f(n) > 100:
        print(n)"""  # 9
"""def f(n):
    if n < 3: return n+1
    if n >= 3 and n % 2 == 0: return f(n-2) + n-2
    return -1000000000

c = 0
for n in range(1, 1000):
    if 10000 <= f(n) <= 99999:
        c += 1
print(c)"""  # 10

# 17
"""f = open('17-n1.txt')
a = [int(i) for i in f]

c = 0
maxim = -10000000000
for i in range(len(a) - 3):
    if a[i]% 2 != a[i+1]% 2 != a[i+2]% 2 != a[i+3]% 2:
        c += 1
        maxim = max(maxim, a[i]+a[i+1]+a[i+2]+a[i+3])
print(c, maxim) """  # 1
"""def perevodik(n, CC):
    s = ''
    while n > 0:
        s = str(n%CC) + s
        n //= CC
    return s

f = open('17-n2.txt')
a = [int(i) for i in f]

c = 0
ans = -10e16
for i in range(len(a)):
    if perevodik(a[i], 5)[-1] == '3' and perevodik(a[i], 9)[-1] == '5' and perevodik(a[i], 8)[-1] != '7':
        c += 1
        ans = max(ans, a[i])
print(c, ans)"""  # 2
"""f = open('17-n3.txt')
a = [int(i) for i in f]

c, ans = 0, -10000000

for i in range(len(a) - 2):
    if bin(a[i])[2:].count('1') >= 3 and bin(a[i + 1])[2:].count('1') >= 3 \
   and bin(a[i])[2:].count('0') >= 1 and bin(a[i + 1])[2:].count('0') >= 1 \
    or bin(a[i])[2:].count('1') >= 3 and bin(a[i + 2])[2:].count('1') >= 3 \
   and bin(a[i])[2:].count('0') >= 1 and bin(a[i + 2])[2:].count('0') >= 1 \
    or bin(a[i+1])[2:].count('1') >= 3 and bin(a[i + 2])[2:].count('1') >= 3 \
   and bin(a[i+1])[2:].count('0') >= 1 and bin(a[i + 2])[2:].count('0') >= 1:
        c += 1
        ans = max(a[i], a[i+1], a[i+2], ans)
print(c, ans)"""  # 3
"""f = open('17-n4.txt')
a = [int(i) for i in f]

c = 0
ans = 0
for i in range(len(a) - 2):
    arr = [a[i], a[i+1], a[i+2]]
    arr.sort()
    if arr[0]**2 + arr[1]**2 == arr[2]**2:
        c += 1
        ans += arr[2]
print(c, ans)"""  # 4
"""f = open('17-n4.txt')
a = [int(i) for i in f]

c, ans = 0, 10e16
for i in range(len(a) - 1):
    t = (a[i] + a[i+1])
    if 100 <= t <= 999 and int(str(t)[-1]) > int(str(t)[-2]):
        c += 1
        ans = min(ans, t)
print(c, ans)
"""  # 5
"""def perevodchik(n, CC):
    s = ''
    while n > 0:
        s = str(n%CC) + s
        n //= CC
    return s

f = open('17-n4.txt')
a = [int(i) for i in f]
c = 0
ans = -10000000
for i in range(len(a) - 1):
    t = perevodchik(a[i]+a[i+1], 7)
    if t == t[::-1]:
        c += 1
        ans = max(ans, int(t))
print(c, ans)"""  # 6
"""def perevodchik(n, CC):
    s = ''
    while n > 0:
        s = str(n%CC) + s
        n //= CC
    return s

f = open('17-n5.txt')
a = [int(i) for i in f]
b = [int(i) for i in a if i % 107 == 0]

c = 0
ans = 100000000000
for i in range(len(a) - 1):
    if (a[i] > max(b) or a[i+1] > max(b)) and (perevodchik(a[i], 7).count('36') + perevodchik(a[i+1], 7).count('36') > 0):
        c += 1
        ans = min(ans, a[i]+a[i+1])
print(c, ans)"""  # 7
"""f = open('17-n5.txt')
a = [int(i) for i in f]
b = [int(i) for i in a if i % 51 == 0]
summ = 0
for i in b:
    summ += sum(int(j) for j in str(i))
c = 0
ans = -100000000000000000
for i in range(len(a) - 1):
    if a[i] < summ or a[i+1] < summ:
        c += 1
        ans = max(ans, a[i]+a[i+1])
print(c, ans)"""  # 8
"""f = open('17-n5.txt')
a = [int(i) for i in f]
b = [int(i) for i in a if i % 35 == 0]
summ = 0
for i in b:
    summ += sum(int(j) for j in str(i))
c = 0
ans = 100000000000000000

for i in range(len(a) - 1):
    if (a[i] > summ and a[i+1] % 256 == int('EF', 16)) and (a[i+1] <= summ and a[i] % 256 != int('EF', 16)) \
    or (a[i+1] > summ and a[i] % 256 == int('EF', 16)) and (a[i] <= summ and a[i+1] % 256 != int('EF', 16)):
        c += 1
        ans = min(ans, a[i]+a[i+1])
print(c, ans)"""  # 9
"""f = open('17-n6.txt')
a = [int(i) for i in f]
c11, minim11 = 0, 100000000000
c17, maxim17 = 0, -100000000000
for i in range(len(a)):
    if a[i] % 11 == 0:
        c11 += 1
        minim11 = min(minim11, a[i])
    if a[i] % 17 == 0:
        c17 += 1
        maxim17 = max(maxim17, a[i])
if c11 > c17:
    print(c11, minim11)
else:
    print(c17, maxim17)"""  # 10

"""from itertools import product
c = 0
for i in product('ГЕОРИЙ', repeat=7):
    s = ''.join(i)
    if s.count('Г') == 2 and s.count('Е') == 1 and s.count('О') == 1 and s.count('Р') == 1 and s.count('И') == 1 and s.count('Й') == 1:
        if s.count('ГГ') == 0:
            c += 1
print(c)
"""  # ГейОргий
"""from itertools import product
c = 0
for i in product('АДЖИК', repeat=6):
    s = ''.join(i)
    if s.count('А') == 2 and s.count('Д') == 1 and s.count('Ж') == 1 and s.count('И') == 1 and s.count('К') == 1:
        gg = True
        for j in range(len(s)-1):
            if s[j] == s[j-1]:
                gg = False
        if gg == True:
            c += 1
print(c)"""

"""f = open('18 ГРОБ.txt')
n = 1000
a = [int(f.readline()) for i in range(n)]
c, maxim = 1, 0
indS, indE = 0, 0
for i in range(n - 1):
    if a[i] < a[i+1]:
        c += 1
        maxim = max(c, maxim)
    else:
        if c >= maxim:
            indE = i
            indS = i - (c - 1)
        c = 1
print(maxim, a[indS:indE+1])

a = a
b = [1]*n
for i in range(1, n):
    bmax = 0
    for j in range(i):
        if a[i] > a[j]: bmax = max(bmax, b[j])
    b[i] = bmax + 1
print(max(b))
"""  # ГРОБ 18 (какое ахуенное решения Я придумал)
"""from itertools import product
c = 0
for i in product('12345', repeat=4):
    s = ''.join(i)
    if s[1] in '234' and s[-1] != '2':
        gg = 1
        for j in range(len(s) - 1):
            if int(s[j]) % 2 == int(s[j + 1])% 2: gg = 0
        if gg == 1:
            c += 1
            print(s)
print(c)"""  # Числа рядомстоящие разной четности

# 19-21
"""def moves(h):
    a, b = h
    return (a*2, b), (a, b*2), (a+1, b), (a, b+1)

from functools import lru_cache
@lru_cache(None)
def f(h):
    if sum(h) >= 69:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h)):
        return 'V2'


for s in range(1, 65):
    h = 6, s
    print(s,f(h))"""  # 1 >>> 16, 28 30, 27
"""def moves(h):
    a, b = h
    return (a+3, b), (a, b+3), (a*2, b), (a, b*2)
from functools import lru_cache
@lru_cache(None)
def f(h):
    if sum(h) >= 62:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'

for s in range(1, 60):
    h = 7, s
    print(s, f(h))
 """  # 2 >>> 14, 13, 20 22
"""def moves(h):
    a, b = h
    return (a+1, b), (a, b+1), (a*2, b), (a, b*2)

from functools import lru_cache
@lru_cache(None)
def f(h):
    if sum(h) >= 61:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'

for s in range(1, 60):
    h = 10, s
    print(s, f(h))"""  # 3 >>> 13, 20 24, 0
"""from functools import lru_cache

def moves(h):
    if h % 2 != 0:
        return [h*3]
    return h+1, h+3


@lru_cache(None)
def f(h):
    if h >= 51:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' for x in moves(h)):
        return 'V2'

for s in range(1, 60):
    print(s, f(s))"""  # 4 >>> 7, 12 14, 2
"""def moves(h):
    return h+1, h*2, h*3

from functools import lru_cache

@lru_cache(None)
def f(h):

    if 43 <= h <= 72:
        return 'END'
    if h > 72:
        return 'gg'

    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' or f(x) == 'gg' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' or f(x) == 'gg' for x in moves(h)):
        return 'V2'

for s in range(1, 50):
    if f(s) == 'V2':
        print(s, f(s))"""  # 5 >>> 14, 3, 12 39
"""def moves(h):
    a, b = h
    c = []
    if a > 1:
        c.append((a - 1, b))
        c.append(((a + 1)//2, b))
    if b > 1:
        c.append((a, b - 1))
        c.append((a, (b+1)//2))
    return c

from functools import lru_cache

@lru_cache(None)
def f(h):
    if sum(h) <= 32:
        return 'END'

    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h)):
        return 'V2'

for s in range(23, 200):
    h = 10, s
    if f(h) == 'P1':
        print(s, f(h))"""  # 6 >>> 45, 46 90, 48
"""def moves(h):
    if h >= 5:
        if h % 2 == 0:
            return h//2, h-1, h-2, h-3, h-4, h-5
        return h-1, h-2, h-3, h-4, h-5
    if h == 4:
        return h//2, h-1, h-2, h-3, h-4
    if h == 3:
        return h-1, h-2, h-3
    if h == 2:
        return h//2, h-1, h-2
    if h == 1:
        return [h-1]

from functools import lru_cache
@lru_cache(None)
def f(h):
    if h < 10:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h)):
        return 'V2'

for s in range(10, 100):
    if f(s) == 'V2':
        print(s, f(s))"""  # 7 >>> 15, 17 30, 21
"""def moves(h):
    a, b = h
    return (a+1, b), (a, b+1), (a*2, b), (a, b*3)

from functools import lru_cache
@lru_cache(None)
def f(h):
    if sum(h) >= 30:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'

for k in range(1, 200):
    s = 7
    if k + s <= 29:
        h = k, s
        if f(h) == 'P2':
            print(k, s, f(h))
"""  # 8 >>> 45, 2 6, 8
"""def moves(h):
    a, b = h
    return (a+2, b), (a, b+2), (a*3, b), (a, b*3)

from functools import lru_cache
@lru_cache(None)
def f(h):
    if sum(h) >= 45:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'

for s in range(1, 100):
    k = 13
    if k + s <= 43:
        h = k, s
        if f(h) == 'V2':
            print(k, s, f(h))"""  # 9 >>> 16, 7 11, 1
"""def moves(h):
    a, b = h
    c = []
    if a > 0:
        c.append((a - 1, b))
        c.append((a//2, b))
    if b > 0:
        c.append((a, b - 1))
        c.append((a, b//2))
    return c

from functools import lru_cache
@lru_cache(None)
def f(h):
    if sum(h) <= 18:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'

for s in range(1, 200):
    for k in range(1, 200):
        if k + s >= 19:
            h = k, s
            if f(h) == 'V2' and k == s:
                print(k, s, f(h))"""  # 10 >>> 13, 14 27, 14

# Задание 22
"""c = 0
for j in range(10, 100):
    n = j
    i = 0
    while n > 0:
        i = i + n % 9
        n = n // 9
    if i % 8 > 0:
        c += 1
print(c)"""  # 1
"""c = 0
minim = 100000
maxim = -1000000
for i in range(1, 10000):
    x = i
    a = 0
    b = 1
    while x > 0:
        a = a + 1
        if x % 12 != 0:
            b = b * (x % 12)
        x = x // 12
    if a == 2 and b == 10:
        print(i)
        c += 1
        minim = min(minim, i)
        maxim = max(maxim, i)
print()
print(c, minim, maxim)       
        
        """  # 2
"""for i in range(1, 1000):
    x = i
    L = 0
    M = 1
    while x > 0:
        L = x % 8 * M + L
        x = x // 8
        M = M * 10
    if sum(int(j) for j in str(L)) == 15:
        print(i)
        break
"""  # 3
"""for i in range(3, 100):
    x = i
    L = 3*x - 6
    M = 3*x + 99
    while L != M:
        if L > M:
            L = L - M
        else: M = M - L
    if M == 21:
        print(i)
"""  # 4
"""for i in range(10000, 100000):
    x = i
    a, b = 0, 0
    while x > 0:
      y = x % 10
      if y > 3:
        a = a + 1
      else:
        b = b - 1
      if y < 8:
        b = b + 1
      x = x // 10
    if a == 2 and b == 1:
        print(i)"""  # 5
"""c = 0
maxim = -100000000
minim = 100000000
for i in range(1, 10000):
    x = i
    K = x - 1
    P = 100
    S = 340
    while P < S:
        K = K + 1
        S = S - 2 * K
        P = P + K
    K = K - x
    if K == 5:
        print(i)
        c += 1
        maxim = max(maxim, i)
        minim = min(minim, i)

print(c, minim, maxim)
"""  # 6
"""for i in range(1, 10000):
    x = i
    L = 0
    M = 10
    while x > 5:
      L = L + 1
      if x % 8 < M:
        M = x % 8
      x = x // 8
    if L == 2 and M == 4:
        print(i)"""  # 7
"""c = 0
for j in range(1, 10000):
    x = j
    P = 0
    S = 10*(x - x % 15)
    i = 2
    while i < 20:
        S = S - 2*i
        P = P + i
        i = i + 2
    if S == 270 and P == 90:
        c += 1
        print(j)
print()
print(c)"""  # 8
"""for i in range(1, 100000):
    x = i
    S = 1
    A = 11
    while x // 7 > 0:
      if x % 7 < 4:
        S = S + A
      else:
        S = S + (x % 7)
      x = x // 7
    if S == 26:
        print(i)"""  # 9
"""for i in range(1, 50):
    x = i
    S = 0
    while x > 0:
      if x % 2 > 0:
        S = S + (x % 7)
      else:
        S = S - (x % 7)
      x = x // 7
    if S == 1:
        print(i)"""  # 10

# 23
"""def g(s, f):
    if s == f:
        return 1
    if s < f:
        return 0
    return g(s-1, f) + g(s-3, f) + g(s//3, f)

print(g(22, 2))"""  # 1
"""def g(s, f, d):
    if s > f:
        return 0
    if s == f:
        if d == 7:
            return 1
        return 0
    d += 1
    return g(s+1, f, d) + g(s+4, f, d) + g(s*2, f, d)

print(g(3, 27, 0))"""  # 2 Кол-во программ из 7 команд
"""minim = 10000
from functools import lru_cache
@lru_cache(None)
def g(s, d):
    if s > 111:
        return 0
    if s == 111:
        global minim
        if d < minim:
            minim = d
        return 1
    d += 1
    return g(s+1, d) + g(s+5, d) + g(s*3, d)
g(1, 0)
print(minim) # минимальная длина

from functools import lru_cache
@lru_cache(None)
def f(s, d):
    if s > 111:
        return 0
    if s == 111:
        global minim
        if d == minim:
            return 1
        return 0
    d += 1
    return f(s+1, d) + f(s+5, d) + f(s*3, d)
print('ans >>>' ,f(1, 0))"""  # 3 Кол-во программ с минимальной длиной
"""from sys import setrecursionlimit
from functools import lru_cache
setrecursionlimit(4000)
@lru_cache(None)
def g(s, f, d):
    if s > f:
        return 0
    if s == f:
        if d == 8:
            return 1
        return 0
    d += 1
    return g(s+1, f, d) + g(s+5, f, d) + g(s*3, f, d)

for i in range(1000, 1024 + 1):
    if g(1, i, 0) > 0:
        print(g(1, i, 0), i)"""  # 4 Кол-во чисел на [1000, 1024] может быть получено из числа 1, состоящих из 8 команд
"""from functools import lru_cache
@lru_cache(None)
def g(s,f):
    if s > f:
        return 0
    if s == f:
        return 1
    return g(s+2, f) + g(s+4, f) + g(s+5, f)

for i in range(31, 100):
    if g(31, i) == 1001:
        print(i)"""  # 5 Определите число, для получения которого из числа 31 существует 1001 программа.
"""from functools import lru_cache
@lru_cache(None)
def f(s, d):
    if s > 80:
        return 0
    if s == 80:
        if d <= 5:
            return 1
        return 0
    d += 1
    if s % 4 == 0:
        return f(s + 1, d) + f(s * 2, d)
    return f(s+1, d) + f(s*2, d) + f(s + (s % 4), d)

c = 0
for i in range(1, 100):
    if f(i, 0) > 0:
        print(i)
        c += 1
print(c)"""  # 6 Кол-во чисел -> 80 за не более 5 команд (ГРОБ)
"""def f(s, g):
    if s > g or s == 32:
        return 0
    if s == g:
        return 1

    return f(s+3, g) + f(s*2, g)

print(f(1, 16) * f(16, 41))"""  # 7
"""def g(s, f):
    if s > f or s == 43:
        return 0
    if s == f:
        return 1
    return g(s+2, f) + g(s+(s-1), f) + g(s+(s+1), f)
print(g(7, 63))"""  # 8
"""def g(s, f):
    if s > f:
        return 0
    if s == f:
        return 1
    return g(s+2, f) + g(s+3, f)

print(g(3, 12) * g(12, 25))"""  # 9
"""from functools import lru_cache
@lru_cache(None)
def g(s, f, d):
    if s > f:
        return 0
    if s == f:
        if d == 5:
            return 1
        return 0
    d += 1
    return g(s+2, f, d) + g(s+3, f, d) + g(s*2, f, d)

c = 0
for i in range(11, 500):
    if g(10, i, 0) > 0:
        print(i)
        c += 1
print(c)"""  # 10

# 24
"""
a = open('24-n1.txt').readline()

c = 0
for i in range(len(a) - 4):
    if a[i] != a[i+1] and a[i+1] != a[i+2] and a[i+2] != a[i+3] and a[i+3] != a[i+4]:
        c += 1
print(c)
"""  # 1 >>> 4904
"""a = open('24-n2.txt').readline()

c = 0
ind = ''
for i in range(len(a) - 2):
    if a[i] <= a[i+1] <= a[i+2]:
        c += 1
        ind = i
print(c, ind)
"""  # 2 >>> 72 148
"""a = open('24-n3.txt').readline()
arr = []
for i in range(len(a)):
    arr.append(ord(a[i]))
c = 1
for i in range(len(arr) - 1):
    if arr[i] >= arr[i+1]:
        c += 1
    else:
        c = 1
print(c)"""  # НЕДОДЕЛАНО
"""
a = open('24-n4.txt').readline()

lmin = 0
rmin = 0
maxim = -10e16
for i in range(1, len(a) - 1):
    if a[i-1] > a[i] < a[i+1]:
        rmin = i
        maxim = max(maxim, rmin - lmin)
        lmin = rmin
print(maxim)
"""  # 4 >>> 29
"""
a = open('24-n5.txt').readline()
c = 0
for i in range(1,len(a) - 1):
    if a[i-1] != 'J' and a[i:i+4] == 'BOSS' and a[i+4] != 'J':
        c += 1
print(c)
"""  # 5 >>> 2198
"""# 6
f = open('24-n6.txt')
alp = {}
c = 0
for j in range(1000):
    gg = False
    a = f.readline()
    for i in range(1, len(a) - 1):
        if a[i-1] == 'A' and a[i+1] == 'R':
            gg = True
            try: alp[a[i]] += 1
            except KeyError: alp[a[i]] = 1
    if gg == True:
        c += 1
print(c, max(alp, key=alp.get), max(alp.values()))"""  # 6 >>> 784 N 79
'''
# 1 Способ 
a = open('24-n7.txt').readline()
c = 1
maxim = 0
for i in range(len(a) - 1):
    try:
        if int(a[i]) + int(a[i+1]) >= 10:
            c += 1
            maxim = max(maxim, c)
        else:
            c = 1
    except ValueError: pass
print(maxim)

# 2 способ
a = open('24-n7.txt').readline()
a = a.replace('\n', '') 
c = 1
maxim = 0
for i in range(len(a) - 1):
    if int(a[i]) + int(a[i+1]) >= 10:
        c += 1
        maxim = max(maxim, c)
    else:
        c = 1
print(maxim)
'''  # 7 >>> 26
"""a = open('24-n8.txt').readline()
c = 0
for i in range(len(a) - 2):
    if (a[i] == a[i+2]):
        c += 1
for i in range(len(a) - 4):
    if (a[i] == a[i + 4] and a[i + 1] == a[i + 3]):
        c += 1
print(c)"""  # 8 >>> 39716
"""a = open('24-n8.txt').readline()
# a = 'srgauquulrrvbentglsfkq zpswym o rcpuwd qbkgdefxvptgpzqblwetjz'
#                         21       28       35
# Без цел.дел. прога учитывает повторы и центральные элементы строки 
c = 0
for i in range(len(a)):
    if a[i] == a[len(a) - 1 - i]:
        c += 1
print(c//2) """  # 9 >>> 19351
"""# Громоздское решение
a = open('24-n9.txt').readline()
lena = [0]*4
# 0 > 7
# 1 > 8
# 2 > 9
# 3 > 10
c = 0
for i in range(len(a)):
    for j in range(6, 10):
        try:
            if a[i] == 'A' and a[i+j] == 'F':
                c += 1
                lena[j-6] += 1
        except IndexError: pass

maxim = -10000
ans = 0
for i in range(4):
    if lena[i] > maxim:
        ans = i+7
        maxim = lena[i]
print(c, ans, maxim)"""  # 10 >>> 3703 10 3696

# 25
"""for i in range(87921, 88187 + 1):
    s = [int(j) for j in str(i)]
    pr = 1
    for l in s:
        pr *= l
    if sum(s) % 14 == 0 and pr % 18 == 0 and pr != 0:
        print(i, sum(s), pr)
# 87999 42 40824
# 87922 28 2016
# 87931 28 1512
# 88129 28 1152"""  # 1
"""def count_div(n):
    c = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            c += 1
            if i != n//i:
                c += 1
    return c

for i in range(120000, 130000 + 1):
    s = [int(j) for j in str(i)]
    if all(m < 3 for m in s) and sum(s) % 10 == 0:
        print(i, count_div(i))
# 121222 2
# 122122 30
# 122212 4
# 122221 6"""  # 2
"""def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
c = 0
for i in range(194441, 196000 + 1):
    c += 1
    if is_prime(i) and i % 100 == 93:
        print(c, i)"""  # 3
"""def find_divv(n):
    masiv = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            masiv.append(i)
            if i != n//i:
                masiv.append(n//i)
    masiv.sort()
    return masiv, len(masiv)

maxim = 0
a = []
c = 0
for i in range(394480, 394540 + 1):
    c += 1

    if find_divv(i)[1] > maxim:
        a = []
        maxim = find_divv(i)[1]

    if find_divv(i)[1] == maxim:
        a.append([c, find_divv(i)[0][-1], find_divv(i)[0][-2]])

print(maxim)
for i in a:
    print(*i)"""  # 4
"""def find_div(n):
    a = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.append(i)
            if i != n//i:
                a.append(n//i)
    a.append(1)
    a.sort()
    return a

nedo = 0
izb = 0
for i in range(2, 10000 + 1):
    if i == sum(find_div(i)):
        a = ','.join([str(j) for j in find_div(i)])
        print(i, a)
    elif i > sum(find_div(i)):
        nedo += 1
    else:
        izb += 1
print(izb, nedo)"""  # 5
"""def f(n):
    summ = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            summ += i
            if i != n//i:
                summ += n//i
    return summ

for i in range(2, 10000):
    M = f(i)
    N = f(M)
    if N == i and M > i:
        print(i, M)"""  # 6
"""def sqr3(n):
    c = 0
    maxim = 0
    for i in range(2, int(n**(1/3)) + 1):
        if n % i == 0 and i % 2 != 0:
            if n % i**3 == 0 and i**3 != n:
                c += 1
                maxim = max(maxim, i**3)
    if c >= 4:
        return c, maxim
    return 0, 0

for i in range(228_224, 531_135+1):
    t = sqr3(i)
    if t[0] > 0:
        print(i, *t)"""  # 7
"""def f(n):
    even = 0
    odd = 0
    minim = 10000000000000
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
            if i > 1000:
                minim = min(minim, i)

            if i != n//i:
                if n//i % 2 == 0:
                    even += 1
                else:
                    odd += 1
                if n//i > 1000:
                    minim = min(minim, n//i)

    if odd == even and odd >= 70 and even >= 70:
        return minim
    return 0

for i in range(326_496, 649_633):
    t = f(i)
    if t > 0:
        print(i, t)"""  # 8
"""def OTA(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    if len(ans) == 3:
        if ans[0] % 10 == ans[1] % 10 == ans[2] % 10 \
                and ans[0] != ans[1] and ans[0] != ans[2] and ans[1] != ans[2]:
            return ans[2] - ans[0]
    return 0
c = 0
maxim = 0
ans = 0
for i in range(536792, 604298 + 1):
    t = OTA(i)
    if t != 0:
        c += 1
        if t > maxim:
            maxim = t
            ans = i
print(c, ans)"""  # 9 ОТА
"""def find_div(n):
    mass = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            mass.add(i)
            mass.add(n//i)
    mass = sorted(mass)
    if len(mass) > 1:
        for j in range(len(mass) - 1):
            if mass[j] + 100 != mass[j + 1]:
                return 0
        return max(mass)
    return 0

for i in range(862346, 1056242):
    t = find_div(i)
    if t > 0:
        print(i, t)
"""  # 10 разность 100

# 26
"""f = open('input.txt')
n, S = [int(i) for i in f.readline().split()]
a = [int(i) for i in f]
a.sort()
a.reverse()
c = 0
summ = 0
sum_mas = 0
for i in range(n):
    if a[i] + summ <= S:
        summ += a[i]
        sum_mas = summ
        if i == n-1:
            c += 1
    else:
        for j in range(i+1, n):
            if a[j] + summ <= S:
                summ += a[j]
                a[j] = 0
        c += 1
        summ = a[i]
print(c, sum_mas)
f.close()"""  # Cудно с грузами
"""f = open('input.txt')
n = int(f.readline())
a = [int(i) for i in f]
a.sort()
MEDIANA = a[n//2]
SRZ = sum(a)/len(a)
k = 0
for i in range(n):
    if SRZ <= a[i] <= MEDIANA:
        k += 1
print(k)
f.close()
"""  # Кол-во чисел между СРЗНАЧ и МЕДИАНОЙ

# 27
"""
f = open('input.txt')
n = int(f.readline())
ans = 0
a = [int(i) for i in f]
for i in range(n):
    mult = a[i]
    for j in range(i+1, n):
        mult *= a[j]
    if mult > ans:
        ans = mult
print(ans)
f.close()

ans = 0
f = open('input.txt')
n = int(f.readline())
min_mult = 100000000000
c = 0
mult = 1
g = 1
for i in range(n):
    x = int(f.readline())
    if x == 0:
        mult = 1
        c = 0
        g = 1
    else:
        if x < 0:
            c += 1
        mult *= x
        if c % 2 == 0:
            ans = mult
        else:
            if mult// min_mult > ans:
                ans = mult// min_mult
            if g == 1:
                min_mult = mult
                g = 0
print(ans)
f.close()"""  # 1
"""# 27A
f = open('27-a2.txt')
n = int(f.readline())
a = [int(f.readline()) for i in range(n)]
minim = 10e16
for i in range(n):
    for j in range(i+5, n):
        minim = min(minim, (a[i]**2 + a[j]**2))
print(minim)


# 27B
f = open('input.txt')
line = []
n = int(f.readline())
for i in range(5):
    line.append(int(f.readline()))

minim = 100000000000000000000
ans = 100000000000000000000
for i in range(5, n):
    if line[0]**2 < minim:
        minim = line[0]**2
        
    x = int(f.readline())
    if x**2 + minim < ans:
        ans = x**2 + minim

    del line[0]
    line.append(x)
print(ans)
f.close()
"""  # 2
"""
f = open('input.txt')
n = int(f.readline())
a = [int(i) for i in f]
ans = 0
for i in range(n):
    for j in range(i+5, n):
        if (a[i] + a[j]) % 2 != 0 and (a[i] * a[j]) % 13 == 0:
            ans += 1
print(ans)
f.close()



f = open('input.txt')
n = int(f.readline())
ans = 0
k_nechet = 0
k_chet = 0
nekr_nechet = 0
nekr_chet = 0

line = []
for i in range(5):
    line.append(int(f.readline()))

for i in range(5, n):
    t = line[0]
    if t % 13 == 0:
        if t % 2 == 0:
            k_chet += 1
        else:
            k_nechet += 1
    else:
        if t % 2 == 0:
            nekr_chet += 1
        else:
            nekr_nechet += 1


    x = int(f.readline())
    if x % 13 == 0:
        if x % 2 == 0:
            ans += k_nechet + nekr_nechet
        else:
            ans += k_chet + nekr_chet
    else:
        if x % 2 == 0:
            ans += k_nechet
        else:
            ans += k_chet

    line.append(x)
    del line[0]
print(ans)
f.close()"""  # 3
"""f = open('input.txt')
n = int(f.readline())
s = 0
for i in range(n):
    s += max([int(i) for i in f.readline().split()])
print('максм', s)
f.close()

f = open('input.txt')
n = int(f.readline())
ans = 0

arr = [-10000000000000000] * 8
arr[0] = 0

for i in range(n):
    new_arr = [-10000000000000000] * 8
    a = [int(i) for i in f.readline().split()]
    for t in a:
        for j in range(8):
            ost = (t + arr[j]) % 8
            if t + arr[j] > new_arr[ost]:
                new_arr[ost] = t + arr[j]
    arr = new_arr[:]
print('ответ', arr[0])
f.close()
"""  # 4
'''
f = open('input.txt')
n = int(f.readline())
s = 0
diff = 1000000000000000
for i in range(n):
    x, y = [int(j) for j in f.readline().split()]
    s += min(x, y)
    t = abs(x - y)
    if t < diff and t % 8 != 0:
        diff = t
if s % 8 == 2:
    s += diff
print(s)
f.close()

f = open('input.txt')
n = int(f.readline())
s = 0
diff = 1000000000000000
for i in range(n):
    x, y = [int(j) for j in f.readline().split()]
    s += max(x, y)
    t = abs(x - y)
    if t < diff and t % 16 != 0:
        diff = t
if s % 16 == 10:
    s -= diff
print(s)
f.close()'''  # 5
"""# Для проверки
f = open('input.txt')
n = int(f.readline())
MAX = 0
MIN = 0
for i in range(n):
    x = [int(j) for j in f.readline().split()]
    x.sort()
    MAX += x[1] + x[2]
    MIN += x[0] + x[1]
print(MAX, MIN)
f.close()

# Макс кратное 4
f = open('input.txt')
n = int(f.readline())
arr = [-10000000000000] * 4
arr[0] = 0
for i in range(n):
    a = [int(i) for i in f.readline().split()]
    new_arr = [-10000000000000] * 4
    for t in a:
        for l in a:
            for j in range(4):
                if t != l:
                    elem = t + l + arr[j]
                    ost = elem % 4
                    if elem > new_arr[ost]:
                        new_arr[ost] = elem
    arr = new_arr[:]
print(arr[0], arr[0] % 4 == 0)
f.close()

# Мин кратное 6
f = open('input.txt')
n = int(f.readline())
arr = [10000000000000] * 6
arr[0] = 0
for i in range(n):
    a = [int(i) for i in f.readline().split()]
    new_arr = [10000000000000] * 6
    for t in a:
        for l in a:
            for j in range(6):
                if t != l:
                    elem = t + l + arr[j]
                    ost = elem % 6
                    if elem < new_arr[ost]:
                        new_arr[ost] = elem
    arr = new_arr[:]
print(arr[0], arr[0] % 6 == 0)"""  # 6

# 2 вариант
'''a = open('24.txt').readline().rstrip().split('000')
maxim = 0
for i in range(len(a)):
    if len(a[i]) + 4 > maxim:
        maxim = len(a[i]) + 4
print(maxim)
open('24.txt').close()'''  # 24
"""
def f(n):
    arr = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            arr.append(i)
            if i != n//i:
                arr.append(n//i)
    arr.sort()
    b = 0
    if len(arr) >= 2:
        b = arr[-1] - arr[0]
    return b

c = 0
for i in range(860000 + 1, 900000):
    M = f(i)
    if M % 100 == 30 and M != 0:
        print(i, M)
        c += 1
        if c == 5:
            break
print()"""  # 25
"""
f = open('27-A.txt')
n = int(f.readline())
a = [int(i) for i in f]
minim = 10000000
dlina = 0
for i in range(n):
    for j in range(i+1, n):
        summ = sum(a[i:j+1])
        if summ % 321 == 0:
            if summ < minim:
                minim = summ
                dlina = j - i + 1
                srez = a[i:j+1]
print(minim, dlina, srez)
f.close()
"""  # 27A
"""f = open('27-B.txt')
n = int(f.readline())
k = 321
max_ps = [-10000000000]*k
ind_ps = [-1000]*k
ind_ps[0] = -1
max_ps[0] = 0

s = 0
minim = 1000000000000
dlina = 0
for i in range(n):
    x = int(f.readline())
    s += x
    ost = s % k
    if s - max_ps[ost] < minim:
        minim = s - max_ps[ost]
        dlina = i - ind_ps[ost]
    if s > max_ps[ost]:
        max_ps[ost] = s
        ind_ps[ost] = i
print(minim, dlina)
f.close()"""  # 27B
# 8 вариант
'''a = open('24_8var.txt').readline().rstrip().split('Z')
print(a)
maxim = 0
for i in range(len(a) - 1):
    t = len(a[i]) + 1 + len(a[i+1])
    if t > maxim:
        maxim = t
print(maxim)'''  # 24
"""
def f(n):
    arr = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            arr.append(i)
            if i != n//i:
                arr.append(n//i)
    b = 0
    arr.sort()
    if len(arr) >= 2:
        b = arr[-1] - arr[0]
    return b
c = 0
for i in range(850000 + 1, 900000):
    M = f(i)
    if M % 11 == 0 and M != 0:
        print(i, M)
        c += 1
        if c == 6:
            break
"""  # 25
'''f = open('27Б_срезовая.txt')
n = int(f.readline())
ans = 0
diff = 1000000000000000000000000
for i in range(n):
    x, y = [int(j) for j in f.readline().split()]
    ans += max(x, y)
    c = abs(x - y)
    if c % 37 != 0:
        diff = min(diff, c)

if ans % 37 != 0:
    print(ans)
    print('COOL')
else:
    print(ans - diff)
f.close()'''  # 27AB

"""def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x+2, y) + f(x+5, y)

for x in range(5, 1000):
    if f(5, x) == 34:
        print(x)
"""

# 25 EZ
"""def find(n):
    arr = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            arr|= {i, n//i}
    return sorted(arr)

for i in range(210235, 210300 + 1):
    t = find(i)
    if len(t) == 4:
        print(i, t)
"""
"""def find(n):
    mass = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            mass |= {i, n//i}
    return sorted(mass)

for i in range(489421, 489440 + 1):
    t = find(i)
    if len(t) == 4:
        print(i, t)"""
"""def find(n):
    mass = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            mass |= {i, n//i}
    return sorted(mass)

for i in range(20789, 35672 + 1):
    t = find(i)
    if len(t) == 5:
        print(t)"""
"""def find(n):
    mass = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            mass |= {i, n//i}
    ans = [i for i in sorted(mass) if i % 2 == 0]
    return ans

for i in range(110203, 110245):
    t = find(i)
    if len(t) == 4:
        print(t)"""
"""def find(n):
    mass = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            mass |= {i, n//i}
    ans = [i for i in sorted(mass) if i % 2 != 0]
    return ans

for i in range(95632, 95650 + 1):
    t = find(i)
    if len(t) == 6:
        print(t)"""
"""def cnt(n):
    c = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            c += 1
            if i != n//i:
                c += 1
    return c

ans = 0
maxim = 0
for i in range(120115, 120200 + 1):
    t = cnt(i)
    if t > maxim:
        maxim = t
        ans = i
print(maxim, ans)"""
"""for s1 in '0123456789':
    for s2 in '0123456789':
        N = '12345' + s1 + '7' + s2 + '8'
        if int(N) % 23 == 0:
            print(N, int(N)//23)"""  # Досрок
"""def M(n):
    Msum = 0
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            Msum = i + n//i
            break
    return Msum

c = 0
for i in range(7000000+1, 7010000):
    t = M(i)
    if t % 10 == 8:
        print(i, t)
        c += 1
        if c == 5:
            break

print()


c = 0
for n in range(7000000 + 1, 7010000):
    mass = set()
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            mass |= {d, n//d}
            break
    m = 0
    if len(mass) > 0:
        m = max(mass) + min(mass)
    if m % 10 == 8:
        print(n, m)
        c += 1
        if c == 5:
            break"""

# VAR 2
"""f = open('zxc.txt')
a = [int(i) for i in f]
c = 0
maxim = 0
for i in range(len(a) - 2):
    if (a[i+1] % 2 != 0 and 100 <= a[i+1] <= 999) and not(a[i] % 2 != 0 and 100 <= a[i] <= 999) and not((a[i+2] % 2 != 0 and 100 <= a[i+2] <= 999)):
        c += 1
        maxim = max(maxim, a[i]+a[i+1]+a[i+2])
print(c, maxim)
f.close()"""  # 17
"""def moves(h):
    return h+1, h * 2

from functools import lru_cache
@lru_cache(None)
def f(h):
    if 50 <= h <= 70:
        return 'END'
    if h > 70:
        return 'GG'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' or f(x) == 'GG' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' or f(x) == 'GG' for x in moves(h)):
        return 'V2'

for s in range(1, 100):
    print(s,f(s))
"""  # 19-21
"""def f(x,y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x+3, y) + f(x*3, y)
c = 0
for s in range(4, 100, 2):
    if f(3, s) != 0:
        c += 1
print(c)"""  # 23
"""a = open('24 (3).txt').readline()
maxim = 0
c = 1
for i in range(len(a) - 1):
    if a[i] == 'Q' and a[i+1] == 'W':
        c = 1
    else:
        c += 1
        maxim = max(maxim, c)
print(maxim)
open('zxc.txt').close()"""  # 24
"""def neprime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

def S(n):
    mass = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            mass |= {i, n//i}
    return sum([i for i in mass if neprime(i)])

c = 0
for i in reversed(range(912673)):
    if i % 2 != 0:
        t = S(i)
        if t != 0 and i % t == 0:
            print(i, t)
            c += 1
            if c == 5:
                break"""  # 25
"""f = open('zxc.txt')
n, k = [int(i) for i in f.readline().split()]
a = [int(i) for i in f]
a.sort()
a.reverse()
c = 0
last = 0
s = 0

for i in range(n):
    if s + a[i] <= k:
        s += a[i]
        last = s
        if i == n - 1:
            c += 1
        continue

    for j in range(i+1, n):
        if s + a[j] <= k:
            s += a[j]
            last = s
            a[j] = 0
    c += 1
    s = a[i]
print(c, last)"""  # 26
"""f = open('zxc.txt')
n = int(f.readline())
a = [int(i) for i in f]
ans = 0

for i in range(n):
    s = 0
    for j in range(20):
        t = i + j
        if t >= n:
            break
        s += a[t]
        if s % 39 == 0:
            ans += 1
print(ans)"""  # 27

"""import itertools
s = 'АВИКНСТ'; s1 = '0123456'
A = itertools.product(s1, repeat=4)
n = 0
for a1 in A :
    if a1[0] != '0' and a1[0] != '2' and (a1[3] == '0' or a1[3] == '2') : n += 1
    if a1[0] == '4' and a1[1] == '2' and a1[2] == '3' and a1[3] == '0': break
print(n)"""  # 8 НИКА

# VAR 3
"""f = open('zxc.txt')

a = [int(i) for i in f]
c = 0
maxim = 0
for i in a:
    if str(i).count('0') > 0 and sum([int(i) for i in str(i)]) == 5:
        c += 1
        maxim = max(maxim, i)
print(c, maxim)
"""  # 17
"""def moves(h):
    return h + 1, h * 2
from functools import lru_cache
@lru_cache(None)
def f(h):
    if h > 45:
        return 'GG'
    if 30 <= h <= 45:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' or f(x) == 'GG' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' or f(x) == 'GG' for x in moves(h)):
        return 'V2'

for s in range(1, 100):
    print(s, f(s))"""  # 19-21
"""for i in range(1, 100000000000):
    x = i
    a = 0; b = 1
    while x > 0:
     a = a + 1
     b = b + (x % 100)
     x = x // 10
    if a == 4 and b == 153:
        print(i)"""  # 22
"""def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x+1,y) + f(x*2,y) + f(x*2 + 1, y)
print(f(10, 65)*f(65, 100))"""  # 23
"""a = open('zadanie_24 (1).txt').readline()
maxim = 0
c = 1
for i in range(len(a) - 1):
    if a[i] != a[i+1]:
        c += 1
        maxim = max(maxim, c)
    else:
        c = 1
print(maxim)"""  # 24
"""def find(n):
    mass = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            mass |= {i, n//i}
    return sorted(mass)


for i in range(78920, 92430 + 1):
    t = find(i)
    if len(t) == 5:
        print(t)"""  # 25
"""f = open('zxc.txt')
n, k = [int(i) for i in f.readline().split()]
perviy = []
poslednyi = []

for i in range(n):
    x = int(f.readline())
    if 310 <= x <= 320:
        perviy.append(x)
    else:
        poslednyi.append(x)

perviy.sort()
perviy.reverse()
poslednyi.sort()


counter = 0
obsum = 0

for i in range(len(perviy)):
    if obsum + perviy[i] <= k:
        obsum += perviy[i]
        counter += 1
        print(counter, obsum, 1)

lst = 0
for i in range(len(poslednyi)):
    if obsum + poslednyi[i] <= k:
        obsum += poslednyi[i]
        counter += 1
        print(counter, obsum, 2)
        lst = i
razn = k - obsum

if razn > 0:
    for i in range(lst+1, len(poslednyi)):

print()
print(counter, obsum)"""  # 26 не добил
"""f = open('zxc.txt')

# НЕЭФФ
# n = int(f.readline())
# a = [int(i) for i in f]
# min_sum = 10000000000000
# for i in range(n):
#    for j in range(i+1, n):
#        for k in range(j+1, n):
#            for l in range(k+1, n):
#                t = a[i] + a[j] + a[k]  + a[l]
#                if t % 9 == 0 and t < min_sum:
#                    min_sum = t
# print(min_sum)

# ЭФФ
ost = [[10e10, 10e10, 10e10, 10e10],
           [10e10, 10e10, 10e10, 10e10],
           [10e10, 10e10, 10e10, 10e10],
           [10e10, 10e10, 10e10, 10e10],
           [10e10, 10e10, 10e10, 10e10],
           [10e10, 10e10, 10e10, 10e10],
           [10e10, 10e10, 10e10, 10e10],
           [10e10, 10e10, 10e10, 10e10],
           [10e10, 10e10, 10e10, 10e10]]



n = int(f.readline())

for i in range(n):
    x = int(f.readline())
    t = ost[x % 9]
    if x < max(t):
        t.append(x)
        t.sort()
        t.reverse()
        del t[0]

mass = ost[0] + ost[1] + ost[2] + ost[3] + ost[4] + ost[5] + ost[6] + ost[7] + ost[8]

min_sum = 10000000000000000000000
from itertools import combinations
for i in combinations(mass, 4):
    if sum(i) < min_sum and sum(i) % 9 == 0:
        min_sum = sum(i)
print(min_sum)
f.close()"""  # 27 EFF + neEFF

# VAR 4
"""def perevod(n):
    s = ''
    while n > 0:
        s = str(n%7) + s
        n //= 7
    return s

f = open('zxc.txt')

a = [int(i) for i in f]
c = 0
maxim = 0

for i in range(len(a) - 1):
    t = perevod(a[i] + a[i+1])
    if t == t[::-1]:
        c += 1
        maxim = max(maxim, int(t))
print(c, maxim)"""  # 17
"""def moves(h):
    return h+1, h*2

from functools import lru_cache
@lru_cache(None)
def f(h):
    if h > 30:
        return 'GG'
    if 20 <= h <= 30:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' or f(x) == 'GG'  for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' or f(x) == 'GG' for x in moves(h)):
        return 'V2'

for s in range(1, 100):
    print(s, f(s))"""  # 19-21
"""for i in range(1, 100000):
    c = 0
    x = i
    a = 3*x + 71
    b = 3*x - 87
    while a != b:
        if a > b:
            a -= b
            c += 1
            if c == 10000:
                break
        else:
            b -= a
    if c == 10000:
        continue
    if a == 158:
        print(i)"""  # 22
"""mass = set()

from itertools import product
for i in product('01', repeat = 11):
    s = 3
    for j in i:
        if j == '0':
            s = s + 1
        else:
            s = s*2 + 1
    mass.add(s)
print(len(mass), mass)"""  # 23 (ГРОБ)
"""a = open('24 (4).txt').readline()
c = 5
maxim = 0
for i in range(len(a) - 5):
    if a[i] == a[i+3] and a[i+1] == a[i+4] and a[i+2] == a[i+5]:
        c = 5
    else:
        c += 1
        maxim = max(maxim, c)
print(maxim)
"""  # 24
"""def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def f(n):
    mass = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            mass |= {i, n//i}
    arr = [i for i in mass if prime(i)]

    if len(arr) == 0:
        return 0
    return sum(arr)//len(arr)

c = 0
for i in range(650001, 700000):
    t = f(i)
    if t % 37 == 23:
        print(i, t)
        c += 1
        if c == 4:
            break
"""  # 25
"""f = open('zxc.txt')
n = int(f.readline())
a = [int(i) for i in f]
a.sort()
c = 0
minim = 1000000000000000000000000000
for i in range(n):
    for j in range(i+1, i+102):
        if j >= n:
            break
        if (a[i] + a[j]) % 10 == 0:
            c += 1
            minim = min(minim, (a[i] + a[j])/2)
print(c, minim)
"""  # 26
"""f = open('zxc.txt')
n = int(f.readline())

min_ps = [10e100] * 69
index_ps = [-10e100] * 69
min_ps[0] = 0
index_ps[0] = -1

s = 0
dlina = 1000000000000000000000000
maxim = 0

for i in range(n):
    x = int(f.readline())
    s += x
    ost = s % 69
    if s - min_ps[ost] > maxim:
        maxim = s - min_ps[ost]
        dlina = i - index_ps[ost]
    if s - min_ps[ost] == maxim:
        dlina = min(dlina, i - index_ps[ost])
    if s < min_ps[ost]:
        min_ps[ost] = s
        index_ps[ost] = i
print(maxim, dlina)
"""  # 27

# VAR 5
"""c = 0
minim = 100000000000000000000000
for i in range(2*10**5, 4*10**5 + 1):
    if i % 7 == 0 and i % 13 != 0 and i % 29 != 0 and i % 43 != 0 and i % 101 != 0:
        c += 1
        minim = min(minim, i)
print(c, minim*10**5)"""  # 17
"""def moves(h):
    a, b = h
    return (a+1,b), (a*3, b), (a,b+1), (a, b*3)

from functools import lru_cache
@lru_cache(None)
def f(h):
    if sum(h) >= 49:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'


for s in range(1, 50):
    h = 5, s
    print(s,f(h))"""  # 19-21
"""for i in range(1, 10000):
    x = i
    a = 1
    while x > 0:
     a *= x % 7
     x = x // 7
    if a == 48:
        print(i)
        break"""  # 22
"""def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x+1, y) + f(x*3, y)

print(f(1, 22) * f(22, 70))"""  # 23
"""f = open('zxc.txt')
a = [i for i in f]
c = 0
for string in a:
    if string.count('E') > string.count('A'):
        c += 1
print(c)"""  # 24
"""def find(n):
    mass = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            mass |= {i, n//i}
    return sorted(mass)
a = 123456789
b = 223456789
a1 = int(123456789**0.25)
a2 = int(223456789**0.25)
for i in range(a1, a2 + 1):
    t = i**4
    T = find(t)
    if a <= t <= b:
        if len(T) == 3:
            print(T[-1])"""  # 25
"""f = open('zxc.txt')
n = int(f.readline())
neskid = []
skid = []
for i in range(n):
    x = int(f.readline())
    if x > 50:
        skid.append(x)
    else:
        neskid.append(x)
skid.sort()
SUM = sum(neskid)
last = 0

for i in range(len(skid)//2):
    SUM += skid[i]*0.75
    last = skid[i]

SUM += sum(skid[len(skid)//2:])

print(int(SUM-0.1)+1, last)"""  # 26
"""f = open('zxc.txt')
n = int(f.readline())
a = [-1000000000000000000000] * 3
a[0] = 0

for i in range(n):
    x = [int(i) for i in f.readline().split()]
    a_new = [-1000000000000000000000] * 3
    for j in x:
        for l in a:
            ost = (j + l) % 3
            a_new[ost] = max(a_new[ost], j + l)
    a = a_new[:]
print(a[0])"""  # 27

# VAR 6
"""f = open('zxc.txt')

a = [int(i) for i in f]
c = 0
maxim = 0
for i in a:
    if i % 3 == 0:
        c += 1
        maxim = max(maxim, i)
print(maxim, c)
"""  # 17
"""def moves(h):
    return h+1, h+2, h+3, h*2

from functools import lru_cache
@lru_cache(None)
def f(h):
    if h >= 34:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'
for s in range(1, 100):
    print(s,f(s))"""  # 19-21
"""for i in range(1, 1000):
    x = i
    k = x % 5
    a = 0
    b = 0
    while x > 0:
        d = x % 5
        if d == k:
            a += 1
        b += d
        x //= 5
    if a == 3 and b == 10:
        print(i)"""  # 22
"""def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x+2, y) + f(x+3, y) + f(x*4, y)
print(f(1, 16))"""  # 23
"""f = open('zxc.txt')

ans = 0
for string in f:
    mass = [1000000000000] * 100
    if string.count('E') < 20:
        for j in range(len(string)):
            ans = max(ans, j - mass[ord(string[j]) - 65])
            mass[ord(string[j]) - 65] = min(mass[ord(string[j]) - 65], j)
print(ans)"""  # 24
"""def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

last = 0
for i in range(3, 1_000_000 + 1):
    if prime(i):
        if i - last > 90:
            print(last, i)
        last = i"""  # 25
"""c = 0
minim = 10e100

f = open('zxc.txt')
n = int(f.readline())
a = []
b = set()
for i in range(n):
    x = int(f.readline())
    a.append(x)
    b.add(x)


for i in range(n):
    for j in range(i + 1, n):
        for l in range(j + 1, n):
            t = a[i] + a[j] + a[l]
            if t % 3 == 0 and t/3 in b:
                c += 1
                minim = min(minim, t/3)
print(c, int(minim))"""  # 26
"""f = open('zxc.txt')
n = int(f.readline())

sMAX = 0
sMIN = 0
m1 = 10e100 # нечетное нечетное
m2 = 10e100 # четное нечетное
m3 = 10e100 # нечетное четное
for i in range(n):
    a = [int(i) for i in f.readline().split()]
    if a[1] % 2 != 0:
        x = max(a)
        y = min(a)
        sMAX += x
        sMIN += y
        if x % 2 == y % 2 == 1:
            m1 = min(m1, x+y)
        elif x % 2 == 0 and y % 2 != 0:
            m2 = min(m2, x+y)
        elif x % 2 != 0 and y % 2 == 0:
            m3 = min(m3, x+y)


if sMAX % 2 == 0 and sMIN % 2 != 0:
    print(sMIN + sMAX)
elif sMAX % 2 == 0 and sMIN % 2 == 0:
    print(sMIN + sMAX - min(m2, m1+m3))
elif sMAX % 2 != 0 and sMIN % 2 != 0:
    print(sMAX + sMIN - min(m3, m1+m2))
elif sMAX % 2 != 0 and sMIN % 2 == 0:
    print(sMAX + sMIN - min(m1, m2+m3))"""  # 27

# VAR 7
"""P1, P2 = 6, 45
Q1, Q2 = 18, 52
minim = 100000000000000000000000
for A1 in range(1, 100):
    for A2 in range(A1+1, 100):
        g = True
        for x in range(1, 100):
            x += 0.1
            f = ((Q1 <= x <= Q2) == (P1 <= x <= P2)) or ((not(A1 <= x <= A2)) <= ((P1 <= x <= P2) and (not(Q1 <= x <= Q2))))
            if f == 0:
                g = False
                break
        if g:
            minim = min(minim, A2-A1)
print(minim)"""  # 15
"""from functools import lru_cache
@lru_cache(None)
def f(a, b):
    if a == 0:
        return b
    return f(a//10, 10*b + (a % 10))

for i in range(1, 1000):
    print(i,f(i, 0))

print("1392781243"[::-1])"""  # 16
"""c = 0
maxim = 0

a = [int(i) for i in open('zxc.txt')]
minim_chet = min([i for i in a if i % 2 == 0])
for i in range(len(a) - 1):
    if ((a[i] % 5 == 0) + (a[i+1] % 5 == 0)) == 1 and (abs(a[i] - a[i+1]) < minim_chet):
        c += 1
        maxim = max(maxim, abs(a[i] - a[i+1]))
print(c, maxim)"""  # 17
"""def moves(h):
    if h % 2 != 0:
        return h+1, h+2, h*2
    return h+1, h+2

from functools import lru_cache
@lru_cache(None)
def f(h):
    if h >= 26:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'
    if any(f(x) == 'V2' or f(x) == 'V1' or f(x) == 'END' for x in moves(h)):
        return 'P3'

for s in range(1, 50):
    print(s,f(s))"""  # 19-21
"""maxim = 0
for i in range(1, 100000):
    x = i
    a = 1; b = 0
    while x > 0:
     d = x%10
     a *= d
     if d > 5:
        b += d
     x //= 10
    if a == 8820:
        maxim = max(maxim, b)
print(maxim)"""  # 22
"""def f(x, y, g):
    if x > y:
        return 0
    if x == y:
        if g <= 2:
            return 1
        return 0
    return f(x+1, y, g) + f(x*2, y, g+1)
print(f(1, 12, 0))"""  # 23
"""a = ('*' + open('Новый текстовый документ (2).txt').readline() + '*').split('D')
c = 0
for i in a:
    if '*' in i:
        print(i)
        continue
    if len(i) >= 8 and i.count('C') >= 2:
        c += 1
print(c)"""  # 24
"""def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d |= {i, n//i}
    return sorted(d)
c = 0
for k in range(1, 1000):
    t = 9000000 + k
    if len(f(t)) < 3:
        print(k)
        c += 1
        if c == 5:
            break"""  # 25
"""f = open('zxc.txt')
n = int(f.readline())
a = [int(i) for i in f]
c = 0

for i in range(n):
    s = 0
    for j in range(i, n):
        s += a[j]
        if j - i > 100:
            if s % 1111 == 0:
                c += 1
print(c)
f.close()
"""  # НЕЭФФ 27
"""f = open('zxc.txt')
n = int(f.readline())

ans = 0
line = [0]
k = [0]*1111
s = 0

for i in range(100):
    x = int(f.readline())
    s += x
    line.append(s)

for i in range(100, n):
    k[line[0] % 1111] += 1
    x = int(f.readline())
    s += x
    ans += k[s % 1111]
    
    del line[0]
    line.append(s)
print(ans)
f.close()"""  # ЕФФ 27

"""print(int('4444', 5))
print(int('1000', 5))

print(int('22222', 3))
print(int('10000', 3))

# 242 - 125
c = 0
for n in range(125, 242 + 1):
    t = hex(n)[2:]
    if t[-1] == 'd':
        c += 1
        print(t)
print()
print(c)"""

"""a = [int(i) for i in open('zxc.txt')]

c = 0
minim = 10e100

for i in range(len(a) - 1):
    if (a[i] % 7 == 0 or a[i+1] % 7 == 0) and (str(a[i+1])[-1] == '3' or str(a[i])[-1] == '3'):
        c += 1
        minim = min(minim, a[i] + a[i+1])
print(c, minim)"""

"""from itertools import product
c = 0
k = 0
for i in product('0123456', repeat = 7):
    s = ''.join(i)
    if s[0] not in '035' and (('22' in s) + ('44' in s)) <= 1:
        c += 1
print(c)"""  # 8 задачка

"""a = open('24 (8).txt').readline()
a = a.replace('AB', '1')
a = a.replace('AC', '1')

for i in range(1, 10000):
    if a.count('1' * i) == 0:
        break
    print(i)"""

# VAR 8
"""a = [int(i) for i in open('zxc.txt')]

c = 0
maxim = 0
for i in range(len(a) - 2):
    if (a[i+1] > 0 and a[i+1] % 10 == 9) and not(a[i] > 0 and a[i] % 10 == 9) and not(a[i+2] > 0 and a[i+2] % 10 == 9):
        c += 1
        maxim = max(maxim, a[i] + a[i+1] + a[i+2])
print(c, maxim)"""  # 17
"""def moves(h):
    m = []
    if h % 2 == 0:
        m += [h // 2]
    elif h > 2:
        m += [h-2]
    if h % 3 == 0:
        m += [h//3]
    elif h > 3:
        m += [h-3]
    return m

from functools import lru_cache
@lru_cache(None)
def f(h):
    if h == 1:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if any(f(x) == 'P1' for x in moves(h)):
        return 'V1'
for s in range(1, 40):
    print(s,f(s))"""  # 19-21
"""for i in range(1, 100000):
    x = i
    s = 0
    while x > 0:
        s = s + x % 9
        x //= 3
    if s == 17:
        print(i)"""  # 22
"""def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    return f(x-8, y) + f(x//2, y)
print(f(102, 43) * f(43, 5))"""  # 23
"""a = open('24 (9).txt').readline()
c = 0
d = {}

for i in range(len(a) - 4):
    if a[i] == 'C' and a[i+1] == 'B' and a[i+2] not in 'ABF' and a[i+3] == 'B' and a[i+4] == 'C':
        c += 1
        if a[i+2] not in d:
            d[a[i+2]] = 1
        else:
            d[a[i + 2]] += 1
print(max(d, key=d.get), c)"""  # 24
"""def sum_div(n):
    d = set()
    d.add(0)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d |= {i, n//i}
    return sum(d), max(d)

c = 0
for i in range(520001, 620001):
    t = sum_div(i)
    if t[0] != 0 and str(t[0]) == str(t[0])[::-1]:
        print(i, t[1])
        c += 1
        if c == 5:
            break"""  # 25
"""f = open('zxc.txt')
n = int(f.readline())

d = {}

for i in range(n):
    ryad, mesto = [int(i) for i in f.readline().split()]
    if ryad not in d:
        d[ryad] = [mesto]
    else:
        d[ryad].append(mesto)
        d[ryad].sort()

ryad_ans = 0
mesto_mass = []
mesto_ans = 0
for ryad in d:
    mass = d[ryad]
    for i in range(len(mass) - 1):
        if mass[i+1] - mass[i] == 3:
            if ryad > ryad_ans:
                ryad_ans = ryad
                mesto_mass.append(mass[i] + 1)
                mesto_ans = min(mesto_mass)
    mesto_mass = []
print(ryad_ans, mesto_ans)"""  # 26
"""f = open('zxc.txt')
n = int(f.readline())
from math import *
obs = []
a = []

for n in range(n):
    x = [int(i) for i in f.readline().split()]
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            a.append(lcm(x[i], x[j]))

print(a)"""  # 27

# VAR 9
"""for i in range(1, 1000000):
    s = i
    s = (s + 1) // 7
    n = 36
    c = 0
    while s < 2050:
        s = s * 2
        n = n + 3
        c += 1
        if c == 1000:
            break
    if n == 66:
        print(i)"""  # 6
"""from itertools import product
c = 0
for i in product('АНДРЕЙ', repeat=6):
    s = ''.join(i)
    if s.count('А') >= 1 and s.count('Й') <= 1:
        c += 1
        print(s)
print()
print(c)"""  # 8
"""for i in range(1, 100):
    for j in range(1, 100):
        for l in range(1, 100):
            s = '0'  + '2'*j +'3'*l + '1'*i
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '30', 1)
                s = s.replace('02', '101', 1)
                s = s.replace('03', '202', 1)
            if s.count('1') == 20 and s.count('2') == 10 and s.count('3') == 70:
                print(i)"""  # 12
"""def moves(h):
    a, b = h
    return (a+1, b), (a+b, b), (a, b+1), (a, b+a)

from functools import lru_cache
@lru_cache(None)
def f(h):
    if sum(h) >= 67:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2'  for x in moves(h)):
        return 'V2'

for s in range(1, 100):
    h = 9, s
    print(s,f(h))
"""  # 19-21
"""for i in range(1, 1000):
    x = i
    m = 0
    s = 0
    while x > 0:
     d = x % 8
     s += d
     if d > m:
        m = d
     x = x // 8
    if m == 4 and s == 10:
        print(i)"""  # 22
"""def f(x, y):
    if x > y or x == 15:
        return 0
    if x == y:
        return 1
    return f(x+1, y) + f(x+2, y) + f(x*3, y)

print(f(2, 11) * f(11, 16))"""  # 23
"""d = {}

a = open('24 (10).txt').readline()

for i in range(len(a) - 2):
    if a[i] == a[i+1]:
        if a[i+2] not in d:
            d[a[i+2]] = 1
        else:
            d[a[i + 2]] += 1
print(max(d, key=d.get))
print(d)"""  # 24
"""
print(*[2*i**2 for i in [7283, 7297, 7307, 7309]])
"""  # 25
"""f = open('zxc.txt')
n = int(f.readline())
k = 0
s = 0
diff = []

new = 0
for i in range(n):
    x = sorted([int(i) for i in f.readline().split()])
    s += x[0]
    if x[0] % 2 == 0: k += 1
    if x[0] % 2 != x[1] % 2:
        diff.append(x[1] - x[0])
    if x[1] - x[0] == 27:
        print(x)
    if x[1] - x[0] == 47:
        print(x)
print(sorted(diff))
k -= 2
print(s, k, n-k)
print(s+27+47)"""  # 27

# VAR 10

"""a = [int(i) for i in open('zxc.txt')]

c = 0
gipo = []

for i in range(len(a) - 2):
    mass = sorted([a[i], a[i+1], a[i+2]])
    if mass[2]**2 == mass[1]**2 + mass[0]**2:
        c += 1
        gipo.append(mass[2])
print(c, sum(gipo))"""  # 17
"""def moves(h):
    return h+1, h*2, h*3


from functools import lru_cache
@lru_cache(None)
def f(h):
    if h > 60:
        return 'GG'
    if 36 <= h <= 60:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' or f(x) == 'GG' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' or f(x) == 'GG' for x in moves(h)):
        return 'V2'
for s in range(1, 100):
    if f(s) == 'V2':
        print(s,f(s))
"""  # 19-21
"""for i in range(1, 10000):
    x = i
    a = x - 61
    b = 3*x - 138
    c = 0
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
        c += 1
        if c == 1000:
            break
    if a == 45:
        print(i)"""  # 22
"""ans = []

from itertools import product

for i in product([0,1], repeat=15):
    s = 1
    for j in i:
        if j == 1:
            s = s * 2
        else:
            s = s * 2 + 1
    ans.append(s)
print(ans)
print(len(ans))"""  # 23
"""f = open('24 (11).txt')
a = [i for i in f]
maxim = 0

for i in a:
    i = i.replace('XYZ', '1')
    c = 0
    for j in i:
        if j == '1':
            c += 1
            maxim = max(maxim,c)
        else:
            c = 0
print(maxim*3)"""  # 24
"""def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find(n):
    arr = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            arr |= {i, n//i}
    mass = sorted([i for i in arr if prime(i)])
    if len(mass) > 1:
        return mass[-1] - mass[0]
    return 0

c = 0
for i in range(450001, 470001):
    M = find(i)
    if M % 29 == 11:
        print(i, M)
        c += 1
        if c == 4:
            break"""  # 25
"""from bisect import bisect
f = open('zxc.txt')
n = int(f.readline())
a = sorted([int(i) for i in f])

c = 0
minim = 10**10
for i in range(n):
    for j in range(i+1, n):
        s = a[i] + a[j]
        if s % 2 == 0 and bisect(a, s/2) >= n//2 and bisect(a, s/2) <= 3*n//4 :
            c += 1
            minim = min(minim, s/2)
print(c, int(minim))"""  # 26
"""f = open('zxc.txt')
n = int(f.readline())

a = [-10**100] * 70
a[0] = 0

for i in range(n):
    x = [int(i) for i in f.readline().split()]
    a_new = [-10**100] * 70
    X = [x[0] + x[1], x[1] + x[2], x[0] + x[2]]
    for t in X:
        for j in a:
            ost = (t + j) % 70
            a_new[ost] = max(a_new[ost], t + j)
    a = a_new[:]

maxim = 0
for i in range(70):
    if ((i % 7 == 3) + (i % 10 == 5)) == 1:
        maxim = max(maxim, a[i])
print(maxim)"""  # 27

# VAR 11

"""def perevod(n):
    s = ''
    while n > 0:
        s = str(n%3) + s
        n //= 3
    return s


def f(n):
    if n == 0:
        return  0
    if n % 3 != 0:
        return f(n-1) + 1
    return f(n/3)

print(perevod(1200000000))
print(perevod(1600000000))
print('10222222222222222222'.count('2')*2 + 1)"""  # 16
"""a = [int(i) for i in open('zxc.txt')]
t = [i for i in a if i % 2 != 0]
sr_nechet = sum(t)/len(t)


c = 0
maxim = 0
for i in range(len(a) - 2):
    if ((a[i] < sr_nechet) + (a[i+1] < sr_nechet) + (a[i+2] < sr_nechet)) == 1 and \
        a[i] % 3 != a[i+1] % 3 and a[i] % 3 != a[i+2] % 3 and a[i+1] % 3 != a[i+2] % 3:
        c += 1
        maxim = max(maxim, a[i]+a[i+1]+a[i+2])
print(c, maxim)"""  # 17
"""def moves(g):
    h, s = g
    if s >= h:
        return (h*2, s-h), (h+1, s-1), (h+2, s-2)
    if s >= 2:
        return (h + 1, s - 1), (h + 2, s - 2)
    if s >= 1:
        return (h + 1, s - 1)


from functools import lru_cache
@lru_cache(None)
def f(h):
    if h[0] >= 41:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'
    if any(f(x) == 'V2' for x in moves(h)):
        return 'P3'
    if all(f(x) == 'P3' or f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V3'

for s in range(1, 50):
    print(s, f((s, 50-s)))"""  # 19-21
"""def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x+1, y) + f(x*10 + 1, y)
print(f(1, 333))"""  # 23
"""a = open('24 (12).txt').readline()
a = a.replace('A', '1')
a = a.replace('B', '1')

a = a.split('1')
maxim = 0

for i in range(len(a) - 3):
    if len(a[i] + a[i+1] + a[i+2] + a[i+3]) + 3 > maxim:
        maxim = len(a[i] + a[i+1] + a[i+2] + a[i+3]) + 3
print(maxim)"""  # 24.1
"""a = 'A' + open('24 (12).txt').readline() + 'A'

index = []
for i in range(len(a)):
    if a[i] in 'AB':
        index.append(i)

maxim = 0
for i in range(len(index) - 4):
    maxim = max(maxim, abs(index[i] - index[i+4]) - 1)
print(maxim)"""  # 24.2
"""def f(n):
    c = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                c += 1
            if i != n//i and n//i % 2 == 0:
                c += 1
    return c

a = 950000000
A = []
c = 0
for i in range(a + 1, a + a):
    if f(i) % 2 != 0:
        A.append(i - a)
        c += 1
        if c == 5:
            break
    if i % 1000 == 0:
        print(i)
print(A)"""  # 25
"""f = open('zxc.txt')
n = int(f.readline())


a = [int(i) for i in f]
count = 0

for i in range(n):
    mult = 1
    for j in range(i, n):
        mult *= a[j]
        if mult % 980_869 != 0:
            count += 1
print(count)
f.close()"""  # 27A
"""f = open('zxc.txt')
n = int(f.readline())
c = 0
ind89 = 0
ind103 = 0
ind107 = 0

for i in range(1, n + 1):
    x = int(f.readline())
    if x % 89 == 0:
        ind89 = i
    if x % 103 == 0:
        ind103 = i
    if x % 107 == 0:
        ind107 = i

    c += i - min(ind89, ind103, ind107)
print(c)
f.close()
# 89 103 107"""  # 27B

# VAR 12

"""def f(n):
    if n < 14:
        return n**3 + n**2 + 1
    if n % 3 == 0:
        return f(n-1) + 2*n**2 - 3
    return f(n-2) + 3*n + 6

c = 0
for i in range(1, 1000+1):
    t = f(i)
    if all([int(i) % 2 != 0 for i in str(t)]):
        c += 1
print(c)"""  # 16
"""a = [int(i) for i in open('zxc.txt')]

mass = []

for i in range(len(a)):
    if ((a[i] % 7 == 0) + (a[i] % 13 == 0) + (a[i] % 17 == 0) + (a[i] % 19 == 0)) == 2:
        mass.append(a[i])
print(len(mass), sum(mass))"""  # 17
"""def moves(h):
    a, b = h
    return (a+1, b), (a, b+1), (a*2, b), (a, b*2)


from functools import lru_cache
@lru_cache(None)
def f(h):
    if sum(h) >= 61:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'

for s in range(1, 100):
    h = 7, s
    if f(h) == 'V2':
        print(s, f(h))"""  # 19-21
"""for i in range(1, 1000):
    x = i
    L = 0; M = 0
    while x > 0:
        L = L + 1
        if x % 2 == 1:
            M = M + (x % 10)
        x = x // 10
    if L == 3 and M == 8:
        print(i)"""  # 22
"""def f(x, y):
    if x < y or x == 23:
        return 0
    if x == y:
        return 1
    return f(x-2, y) + f(x-3, y) + f(x//2, y)
print(f(50, 30) * f(30, 18))"""  # 23
"""a = open('zadanie_24 (2).txt').readline()

c = 1
maxim = 1
char = ''
for i in range(len(a) - 1):
    if a[i] == a[i+1]:
        c += 1
        if c > maxim:
            maxim = c
            char = a[i]
    else:
        c = 1
print(maxim, char)"""  # 24
"""def count_div(n):
    c = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            c += 1
            if i != n//i:
                c += 1
    return c

for i in range(248015, 251575 + 1):
    t = count_div(i)
    if i % 2 != 0 and t % 2 != 0:
        print(i, t, int(i**0.5))"""  # 25
"""f = open('zxc.txt')
n = int(f.readline())

s = 0
diff = 10**100

for i in range(n):
    x, y = sorted([int(i) for i in f.readline().split()])
    s += x
    if y - x < diff and (y - x) % 13 != 0:
        diff = y - x

if s % 13 == 0:
    s += diff
print(s)"""  # 27

# VAR 13

"""def f(n):
    if n == 0:
        return 3
    if n <= 15:
        return f(n-1)
    if n < 100:
        return 2.5 * f(n-3)
    return 3.3*f(n-2)

print(f(100))"""  # 16
"""a = [int(i) for i in open('zxc.txt')]

c = 0
minim = 10**100

for i in a:
    if (i % 4 == 0 or i % 7 == 0) and i % 13 != 0 and i % 17 != 0 and i % 21 != 0 and i % 23 != 0:
        c += 1
        minim = min(minim, i)
print(c, minim)"""  # 17
"""def moves(h):
    a, b = h
    return (a+1, b), (a, b+1), (a*2, b), (a, b*2)

from functools import lru_cache
@lru_cache(None)
def f(h):
    if sum(h) >= 81:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'

for s in range(1, 100):
    h = 13, s
    print(s, f(h))"""  # 19-21
"""for i in range(81, 1000):
    x = i
    s = 0
    while x > 0:
        s = s + x % 9
        x = x // 3
    if s == 17:
        print(i)"""  # 22
"""def f(x, y):
    if x > y or x == 10 or x == 11:
        return 0
    if x == y:
        return 1
    return f(x+1, y) + f(x+2, y) + f(x*3, y)

print(f(1, 8)*f(8,38))"""  # 23
"""a = open('zadanie_24 (3).txt').readline()
c = 5
maxim = 5
for i in range(len(a) - 5):
    if a[i] == a[i+3] and a[i+1] == a[i+4] and a[i+2] == a[i+5]:
        c = 5
    else:
        c += 1
        maxim = max(maxim, c)
print(maxim)"""  # 24
"""def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(7178551, 7178626 + 1):
    if prime(i):
        print(i)"""  # 25
"""f = open('zxc.txt')
V, K, N = [int(i) for i in f.readline().split()]

a = [int(i) for i in f]
a.sort()
a.reverse()
ans = []
vibor = [V]*K
l = 0
for i in range(N):
    for j in range(l, K+l):
        if vibor[j % K] - a[i] >= 0:
            vibor[j % K] = vibor[j % K] - a[i]
            l = j + 1
            break
    else:
        ans.append(a[i])
print(sum(ans), len(ans))"""  # 26
"""f = open('zxc.txt')

n = int(f.readline())

ost = [[-10**100, -10**100, -10**100, -10**100],
       [-10**100, -10**100, -10**100, -10**100],
       [-10**100, -10**100, -10**100, -10**100],
       [-10**100, -10**100, -10**100, -10**100],
       [-10**100, -10**100, -10**100, -10**100],
       [-10**100, -10**100, -10**100, -10**100]]

for i in range(n):
    x = int(f.readline())
    ost[x % 6].append(x)
    ost[x % 6].sort()
    del ost[x % 6][0]

ans = ost[0] + ost[1] + ost[2] + ost[3] + ost[4] + ost[5]

from itertools import combinations
maxim = 0
for i in combinations(ans, 4):
    if sum(i) % 6 == 0:
        maxim = max(maxim, sum(i))
print(maxim)"""  # 27

# VAR 14

"""P = {1, 2, 3, 4, 5, 6}
Q = {3, 5, 15}

A = set()

for x in range(1, 100):
    f = (x not in A) <= (((x not in P) and (x in Q)) or (x not in Q))
    if f == 0:
        A.add(x)
print(A)"""  # 15
"""def f(n):
    if n < 2:
        return 1
    if n % 2 == 0:
        return f(n/2) + 1
    return f(n-3) + 3

c = 0
for i in range(1, 100000 + 1):
    if f(i) == 12:
        c += 1
print(c)"""  # 16
"""def perevod(n):
    s = ''
    while n > 0:
        s = str(n%8) + s
        n //=  8
    return s


a = [int(i) for i in open('zxc.txt')]

c = 0
maxim = 0
for t in a:
    if perevod(t)[-1] == '7':
        if len(perevod(t)) == 1:
            c += 1
            maxim = max(maxim, t)
        elif (perevod(t)[-2] + perevod(t)[-1]) != '27':
            c += 1
            maxim = max(maxim, t)

print(c, maxim)"""  # 17
"""def moves(h):
    return h+2, h*3
from functools import lru_cache
@lru_cache(None)
def f(h):
    if h >= 50:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h)):
        return 'V2'

for s in range(1, 50):
    print(s,f(s))"""  # 19-21
"""for i in range(1, 10000):
    x = i
    m = 0
    s = 0
    while x > 0:
        d = x % 6
        s += d
        if d > m:
            m = d
        x //= 6
    if m == 5 and s == 16:
        print(i)"""  # 22
"""f = open('24 (13).txt')
T = [i for i in f]
maxim = 0
char = ''
for a in T:
    c = 1
    for j in range(len(a) - 1):
        if a[j] == a[j+1]:
            c += 1
            if c > maxim:
                maxim = c
                char = a

        else:
            c = 1

m = 0
ans = chr(10000)
for j in set(char):
    if char.count(j) > m and j < ans:
        m = char.count(j)
        ans = j

print(ans, sum([i.count(ans) for i in T]))"""  # 24
"""a = 100_000_000
b = 300_000_000
for m in range(0, 50, 2):
    for n in range(1, 50, 2):
        N = 2**m * 7**n
        if a <= N <= b:
           print(N, m+n)"""  # 25
"""f = open('zxc.txt')
n = int(f.readline())

mass = [[] for i in range(20)]
for i in range(n):
    x = int(f.readline())
    mass[(x-1)//500].append(x)
    mass[(x-1)//500].sort()

S = 0
last = 0
for a in mass:
    for t in range(len(a)//2):
        S += a[t]*0.5
        last = a[t]*0.5

print(int(S), int(last))"""  # 26
"""f = open('zxc.txt')
n = int(f.readline())
a = [int(i) for i in f]

m = 10**100
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for l in range(j+1, len(a)):
            for k in range(l+1, len(a)):
                s = a[i]+a[j]+a[l]+a[k]
                if s % 9 != 0:
                    m = min(m, s)
print(m)"""  # 27A
"""f = open('zxc.txt')
n = int(f.readline())

ost = [
    [10**100, 10**100, 10**100, 10**100],
    [10**100, 10**100, 10**100, 10**100],
    [10**100, 10**100, 10**100, 10**100],
    [10**100, 10**100, 10**100, 10**100],
    [10**100, 10**100, 10**100, 10**100],
    [10**100, 10**100, 10**100, 10**100],
    [10**100, 10**100, 10**100, 10**100],
    [10**100, 10**100, 10**100, 10**100],
    [10**100, 10**100, 10**100, 10**100]
]



for i in range(n):
    x = int(f.readline())
    ost[x % 9].append(x)
    ost[x % 9].sort(reverse=1)
    del ost[x % 9][0]


t = ost[0] + ost[1] + ost[2] + ost[3] + ost[4] + ost[5] + ost[6] + ost[7] + ost[8]

from itertools import combinations
m = 10**100
for i in combinations(t, 4):
    if sum(i) % 9 != 0:
        m = min(sum(i), m)
print(m)"""  # 27B

# VAR 15 ДОСРОК
"""
for n in range(1, 1000):
    N = bin(n)[2:]
    if n % 2 == 0:
        N = '10' + N
    else:
        N = '1' + N + '01'
    R = int(N, 2)

    if R > 441:
        print(n)"""  # 5
"""for i in range(1, 1000000):
    s = i
    s = (s - 21) // 10
    n = 1
    while s > 0:
        n *= 2
        s -= n 
    if n == 32:
        print(i)"""  # 6
"""def f(n):
    if n < 3:
        return 2
    if n % 2 == 0:
        return f(n-2) + f(n-1) - n
    return f(n-1) - f(n-2) + 2*n
print(f(32))"""  # 16
"""a = [int(i) for i in open('zxc.txt')]
t = min([i for i in a if i % 21 == 0])
c = 0
m = 0

for i in range(len(a) - 1):
    if ((a[i] % t == 0) or (a[i] % t == 0)):
        c += 1
        m = max(m, a[i]+a[i+1])
print(c, m)"""  # 17
"""def moves(h):
    a, b = h
    return (a+1, b), (a*2, b), (a, b+1), (a, b*2)

from functools import lru_cache
@lru_cache(None)
def f(h):
    if sum(h) >= 231:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'

for s in range(1, 220):
    h = 17, s
    print(s,f(h))"""  # 19-21
"""for i in range(1, 1000000):
    x = i
    Q = 8
    P = 10
    K1 = 0
    K2 = 0
    while x <= 100:
        K1 = K1 + 1
        x = x + P
    while x >= Q:
        K2 = K2 + 1
        x = x - Q
    L = x + K1
    M = x + K2
    if L == 12 and M == 19:
        print(i)"""  # 22
"""def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x+2, y) + f(x*2, y)

print(f(1, 18) * f(18, 52))"""  # 23
"""a = open('24 (14).txt').readline()
a = a.replace('AB', '1')
a = a.replace('CB', '1')
a = a.replace('A', ' ')
a = a.replace('B', ' ')
a = a.replace('C', ' ')
a = a.split()
print(len(max(a, key=len)))"""  # 24
"""for s1 in '0123456789':
    for s2 in '0123456789':
        S = int('12345' + s1 + '7' + s2 + '8')
        if S % 23 == 0:
            print(S, S//23)"""  # 25
"""f = open('zxc.txt')
n = int(f.readline())

dict = {}

for i in range(n):
    ryad, mesto = [int(i) for i in f.readline().split()]
    if ryad not in dict:
        dict[ryad] = [mesto]
    else:
        dict[ryad].append(mesto)
    dict[ryad].sort()

max_ryad = 0
last_mesto = 0
for key in dict:
    a = dict[key]
    for i in range(len(a) - 1):
        if a[i+1] - a[i] == 14:
            if key > max_ryad:
                max_ryad = key
                last_mesto = a[i] + 1
print(max_ryad, last_mesto)"""  # 26
"""f = open('zxc.txt')
n = int(f.readline())

a = [int(i) for i in f]

m = 10**100
for i in range(n):
    s = 0
    for j in range(n):
        s += a[j] * min(abs(j - i), n - abs(j - i))
    if s < m:
        m = s
print(m * 3)"""  # 27A
"""f = open('zxc.txt')
n = int(f.readline())
a = [int(i) for i in f]

s = [0]*n
for i in range(n//2):
    s[0] += a[i]

for i in range(1, n):
    s[i] = s[i-1] - a[i-1] + a[(i-1 + n//2) % n]

cost = 0
for i in range(n):
    cost += a[i] * min(i, n-i)

m = cost
for i in range(1, n):
    cost = cost - s[i] + s[(i + n//2) % n]
    if cost < m:
        m = cost
print(m * 3)"""  # 27B

# VAR 16
"""P1, P2 = 10, 20
Q1, Q2 = 25, 55
m = 0
for A1 in range(1, 100):
    for A2 in range(A1+1, 100):
        g = True
        for x in range(1, 100):
            f = (A1 <= x <= A2) <= ((P1 <= x <= P2) or (Q1 <= x <= Q2))
            if f == 0:
                g = False
                break
        if g:
            m = max(m, A2-A1)
print(m)"""  # 15
"""def f(n):
    if n < 2:
        return 1
    if n % 3 == 0:
        return f(n/3) - 1
    return f(n-1) + 7

for n in range(1, 10000000):
    if f(n) == 111:
        print(n)"""  # 16
"""c = 0
m = 10**100
a = [int(i) for i in open('zxc.txt')]

for i in range(len(a) - 1):
    t = a[i] + a[i+1]
    if (100 <= t <= 999) and (str(t)[-1] > str(t)[-2]):
        c += 1
        m = min(m, t)
print(c, m)"""  # 17
"""def moves(h):
    return h+1, h*2, h*3


from functools import lru_cache
@lru_cache(None)
def f(h):
    if 43 <= h <= 72:
        return 'END'
    if h > 72:
        return 'GG'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' or f(x) == 'GG' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' or f(x) == 'GG' for x in moves(h)):
        return 'V2'

for s in range(1, 50):
    print(s,f(s))"""  # 19-21
"""for i in range(1, 1000):
    x = i
    a = 3*x - 112
    b = 3*x + 58
    c = 0
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
        c += 1
        if c == 10000:
            break
    if a == 34:
        print(i)"""  # 22
"""from  itertools import product

ans = set()
for i in product('01', repeat=15):
    num = 2
    for t in i:
        if t == '0':
            num = num + 2
        else:
            num = num*2 + 1
    ans.add(num)
print(len(ans))"""  # 23
"""a = [i for i in open('24 (16).txt')]

m = 0
for S in a:
    c = 0
    S = S.replace('XYZ', '1')
    for j in range(len(S)):
        if S[j] in 'XYZ' and c == 0:
            c = 1
        elif S[j] == '1':
            c += 3
        elif S[j] in 'XYZ' and c > 0:
            c += 1
            m = max(m, c)
            c = 0
        else:
            m = max(m, c)
            c = 0
print(m)"""  # 24
"""def F(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d |= {i, n//i}
    if len(d) == 0:
        return 0
    return sum(d)//len(d)

c = 0
for i in range(550001, 600000):
    t = F(i)
    if t % 31 == 13:
        print(i, t)
        c += 1
        if c == 5:
            break
"""  # 25
"""f = open('zxc.txt')
n = int(f.readline())
a = [int(i) for i in f]
a.sort()

c = 0
m = 0
for i in range(n):
    for j in range(i+101, n):
        s = a[i] + a[j]
        if s % 2 == 0:
            c += 1
            m = max(m, s)
print(c, m/2)"""  # 26
"""f = open('zxc.txt')
n = int(f.readline())
a = [[int(i) for i in f.readline().split()] for j in range(n)]
from itertools import product
m = 0
for i in product([0, 1], repeat=n):
    S1 = 0
    S2 = 0
    for l in range(n):
        S1 += a[l][i[l]]
        S2 += a[l][(i[l] + 1) % 2]
    if abs(S1-S2) % 5 == 0:
        m = max(m, abs(S1-S2))
print(m)"""  # 27A
"""f = open('zxc.txt')
n = int(f.readline())
dm = [-10**100]*5
dm[0] = 0
for i in range(n):
    x = [int(i) for i in f.readline().split()]
    dm_new = [-10**100]*5
    A = [x[0]-x[1], x[1]-x[0]]
    for j in A:
        for k in range(5):
            ost = (j + dm[k]) % 5
            dm_new[ost] = max(dm_new[ost], j + dm[k])
    dm = dm_new[:]
print(dm[0])"""  # 27B

# VAR 17

"""for A in range(1, 100):
    g = True
    for x in range(1, 100):
        for y in range(1, 100):
            f = (2*x + 7*y > 14) or (x + y < A)
            if f == 0:
                g = False
                break
        if g == False:
            break
    if g:
        print(A)"""  # 15
"""def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + f(n-1)
    return 2*f(n-2)

print(f(20))
"""  # 16
"""a = [int(i) for i in open('zxc.txt')]
c = 0
m = 0
for t in a:
    if t % 6 == 0 and t % 5 != 0 and t % 13 != 0 and t % 18 != 0 and t % 22 != 0:
        c += 1
        m = max(m, t)
print(c, m)"""  # 17
"""def moves(h):
    a, b = h
    return (a+1, b), (a*2, b), (a, b+1), (a, b*2)

from functools import lru_cache
@lru_cache(None)
def f(h):
    if sum(h) >= 55:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'

for s in range(1, 100):
    h = 5, s
    print(s,f(h))"""  # 19-21
"""for i in range(1, 100000):
    x = i
    Q = 9
    L = 0
    while x >= Q:
        L = L + 1
        x = x - Q
    M = x
    if M < L:
        M = L
        L = x
    if M == 5 and L == 4:
        print(i)
"""  # 22
"""def f(x, y):
    if x > y or x == 6 or x == 12:
        return 0
    if x == y:
        return 1
    return f(x+1, y) + f(x*2, y) + f(x+3, y)
print(f(3, 13) * f(13, 16))"""  # 23
"""a = open('zadanie_24 (4).txt').readline()
c = 1
m = 1
for i in range(len(a) - 1):
    if a[i] != a[i+1]:
        c += 1
        m = max(m, c)
    else:
        c = 1
print(m)
"""  # 24
"""def f(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d |= {i, n//i}
    return sorted(d)

for i in range(174701, 174772 + 1):
    t = f(i)
    if len(t) == 2:
        print(t[0], t[1])"""  # 25
"""f = open('zxc.txt')
n = int(f.readline())
a = [int(i) for i in f]

m = 0
ans = []
for i in range(n):
    for j in range(i+1, n):
        t = a[i]+a[j]
        if a[i] > a[j] and t % 126 == 0:
            if t > m:
                m = t
                ans = a[i], a[j]
print(ans)

f = open('zxc.txt')
n = int(f.readline())

s = [0]*126

m = 0
ans = []
for i in range(n):
    x = int(f.readline())
    ost = x % 126
    dop = (126 - ost) % 126
    if s[dop] > x:
        if s[dop] + x > m:
            m = s[dop] + x
            ans = s[dop], x
    s[ost] = max(s[ost], x)
print(ans)"""  # 27AB

# VAR 18
"""a = [int(i) for i in open('zxc.txt')]
c = 0
m = 0
for i in range(len(a) - 2):
    if 10 <= a[i+1] <= 99 and a[i+1] % 2 == 0:
        c += 1
        m = max(m, a[i] + a[i+1] + a[i+2])
print(c, m)"""  # 17
"""def moves(h):
    return h+1, h*2


from functools import lru_cache
@lru_cache(None)
def f(h):
    if h > 45:
        return 'GG'
    if 25 <= h <= 45:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' or f(x) == 'GG' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' or f(x) == 'GG' for x in moves(h)):
        return 'V2'

for s in range(1, 26):
    print(s, f(s))"""  # 19-21
"""for i in range(1, 1000):
    x = i
    a = 5*x + 345
    b = 5*x - 807
    c = 0
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
        c += 1
        if c == 10000:
            break
    if a == 96:
        print(i)"""  # 22
"""from itertools import product
mass = set()
for i in product([0, 1], repeat=13):
    n = 2
    for t in i:
        if t == 0:
            n += 3
        else:
            n = 2*n + 1
    mass.add(n)
print(len(mass))
"""  # 23
"""a = [i.rstrip() for i in open('zxc.txt')]
m = 0
c = 0
for i in a:
    s = set(i)
    for j in s:
        t = i.split(j)[1:-1]
        for l in t:
            if len(l) != 0:
                if l.count('R') < 30 and j != 'R':
                    print(j, l)
                    c += 1
                    m = max(m, len(l)+1)

print(m, c) """  # 24
"""f = open('zxc.txt')
n = int(f.readline())
a = [int(i) for i in f]
b = set(a)
c = 0
m = 0
for i in range(n):
    for j in range(i+1, n):
        sr = (a[i]+a[j])//2
        if a[i] % 2 != 0 and a[j] % 2 != 0 and sr in b:
            c += 1
            m = max(m, sr)
print(c, m)"""  # 26
"""f = open('zxc.txt')
n = int(f.readline())
a = [int(i) for i in f]
c = 0
for i in range(n):
    s = 0
    for j in range(i, n):
        s += a[j]
        if s % 71 == 0:
            c += 1
print(c)"""  # 27A

# VAR 19
"""m = 10**100
ans = 0
for i in range(100, 1000):
    s = '1'*i
    while '111' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '11', 1)
    if s.count('1') < m:
        m = s.count('1')
        ans = i
print(ans)"""  # 12
"""a = 343**5 - 7**9 + 48
c = 0
while a > 0:
    if a % 7 == 6:
        c += 1
    a //= 7
print(c)
"""  # 14
"""for A in range(1, 100):
    g = True
    for x in range(1, 100):
        f = (90 % A == 0) and ((x % A != 0) <= ((x % 15 == 0) <= (x % 20 != 0)))
        if f == 0:
            g = False
            break
    if g:
        print(A)"""  # 15
"""def f(n):
    if n == 0:
        return 0
    if n % 3 == 0:
        return n + f(n-3)
    return n + f(n - (n % 3))
print(f(22))"""  # 16
"""def moves(h):
    a, b = h
    return (a+1, b), (a*4, b), (a, b+1), (a, b*4)


from functools import lru_cache
@lru_cache(None)
def f(h):
    if sum(h) >= 91:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h)):
        return 'V2'

for s in range(1, 100):
    h = 5, s
    print(s,f(h))"""  # 19-21
"""for i in range(1, 1000):
    x = i
    a = 1
    while x > 0:
     a *= x % 11
     x = x // 11
    if a == 120:
        print(i)"""  # 22
"""def f(x, y):
    if x > y or x == 10 or x == 11:
        return 0
    if x == y:
        return 1
    return f(x+1, y) + f(x+2, y) + f(x*3, y)

print(f(1,8) * f(8, 27))"""  # 23
"""d = {}
a = open('24 (19).txt').readline()

for i in range(len(a) - 1):
    if a[i] == 'A':
        if a[i+1] not in d:
            d[a[i+1]] = 1
        else:
            d[a[i + 1]] += 1
print(max(d, key=d.get))"""  # 24
"""def f(n):
    d = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if n//i - i <= 100:
                d.append(n//i - i)
    return d

for i in range(1000000, 2000000 + 1):
    t = f(i)
    if len(t) >= 3:
        print(i)
  """  # 25
"""f = open('zxc.txt')
n, k = [int(i) for i in f.readline().split()]

posl = []
s = 0
c = 0
for i in range(n):
    x = int(f.readline())
    if 200 <= x <= 210:
        s += x
        c += 1
    else:
        posl.append(x)

posl.sort()
vibor = []
for i in range(len(posl)):
    if posl[i] + s <= k:
        s += posl[i]
        vibor.append(posl[i])
        c += 1
    else:
        break

for a in posl:
    for b in vibor:
        if a > b and s - b + a <= k:
            s = s - b + a
print(c, s)"""  # 26

"""a = [int(i) for i in open('zxc.txt')]
t = max([i for i in a if i % 11 == 0])
c = 0
m = 10**100

for i in range(len(a) - 1):
    if a[i] > t or a[i+1] > t:
        c += 1
        m = min(m, a[i]+a[i+1])
print(c, m)"""  # 17
"""def moves(h):
    a, b = h
    return (a+3, b), (a, b+3), (a*2, b), (a, b*2)


from functools import lru_cache
@lru_cache(None)
def f(h):
    if sum(h) >= 300:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h)):
        return 'V2'
    if any(f(x) == 'V2' for x in moves(h)):
        return 'P3'

for s in range(1, 300):
    h = 20, s
    if f(h) == 'P3':
        print(s,f(h))"""  # 19-21
"""f = open('zxc.txt')
n, k = [int(i) for i in f.readline().split()]

a = [int(i) for i in f]
m = 0
mS = 0
for i in range(n):
    s = 0
    c = 0
    for j in range(i, n):
        if s + a[j] <= k:
            s += a[j]
            c += 1
            if c > m:
                m = c
                mS = s
        else:
            break
print(m, mS)"""  # 27A
"""
m = 10**100
def f(x, y, g):
    global m
    if x > y:
        return 0
    if x == y:
        if g < m:
            m = g
        return 1
    return f(x+2, y, g+1) + f(x*2, y, g+1)

print(f(1,100, 0))
print(m)
"""  # 23
"""a = open('24 (20).txt').readline()
m = 0
c = 1
i = 0
while i < len(a) - 1:
    if a[i] == a[i+1] == 'B' or a[i] == a[i+1] == 'D':
        c += 1
        m = max(m, c)
        i += 2
    else:
        c = 1
        i += 1

print(m)"""  # 24

# VAR 20
"""c = 0
from itertools import product
for i in product('ОДЕКЛН', repeat=8):
    s = ''.join(i)
    g = True
    if s.count('О') == 3 and s.count('Д') == 1 and s.count('Е') == 1 and s.count('К') == 1 and s.count('Л') == 1 and s.count('Н') == 1:
        for j in range(len(s) - 1):
            if s[j] == s[j+1]:
                g = False
        if g:
            c += 1
print(c)"""  # 8
"""def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return f(n/2) + 1
    return f(n-1) + n

for n in range(1, 10000):
    if f(n) == 19:
        print(n)"""  # 16
"""x = [int(i) for i in open('zxc.txt')]
k = 0
m = 0

for i in range(len(x) - 2):
    a, b, c = x[i], x[i+1], x[i+2]
    sa, sb, sc = bin(a)[2:], bin(b)[2:], bin(c)[2:]
    if ((sa.count('1') == 2 and sa.count('0') >= 1) + (sb.count('1') == 2 and sb.count('0') >= 1) + (sc.count('1') == 2 and sc.count('0') >= 1)) >= 2:
        k += 1
        m += max(a,b,c)
print(k, m)"""  # 17
"""def moves(h):
    return h+1, h+2, h*3


from functools import lru_cache
@lru_cache(None)
def f(h):
    if h >= 65:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'

for s in range(1, 100):
    print(s, f(s))"""  # 19-21
"""for i in range(1, 100000):
    x = i
    k = x % 8
    a = 0
    b = 0
    while x > 0:
        d = x % 8
        if d == k:
            a += 1
        b += d
        x //= 8
    if a == 3 and b == 20:
        print(i)
"""  # 22
"""def f(x, y):
    if x > y or x == 12:
        return 0
    if x == y:
        return 1
    return f(x+1, y) + f(x+3, y) + f(x*2, y)

print(f(3,8) * f(8, 21))"""  # 23
"""a = open('24 (21).txt').readline()
a = a.replace('XYZ', '1')
a = a.replace('X', ' ')
a = a.replace('Y', ' ')
a = a.replace('Z', ' ')
a = a.split()
print(3*len(max(a, key=len)))"""  # 24
"""def prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def f(n):
    S = 0
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d |= {i, n//i}
    S = sum([i for i in d if prime(i)])
    return S

c = 0
for i in range(250001, 260001):
    t = f(i)
    if t != 0 and t % 17 == 0:
        print(i, t)
        c += 1
        if c == 5:
            break"""  # 25
"""t1 = time.time()
f = open('zxc.txt')
n = int(f.readline())

a = [int(i) for i in f]
b = set(a)
c = 0
m = 10**100

for i in range(n):
    for j in range(i+1, n):
        t = a[i] + a[j]
        sr = t//2
        if t % 2 == 0 and ((sr + 5 in b) or (sr - 5 in b)):
            c += 1
            m = min(m, t//2)
print(c, m)"""  # 26

# Частичные суммы (выбор из пары, тройки)
"""f = open('zxc.txt')
n = int(f.readline())
a = [int(i) for i in f]

k = [0]*10
k[0] = 1
for i in range(n):
    x = a[i]
    k = [k[t] + k[(t - x % 10) % 10] for t in range(10)]
    
print(k[5])"""  # 1 Сумма % 10 == 5
"""f = open('zxc.txt')
n = int(f.readline())
s = [0]

for i in range(n):
    pair = [int(x) for x in f.readline().split()]
    s = [a+b for a in s for b in pair]
    s = {x % 3: x for x in sorted(s)}.values()
print(max(x for x in s if x % 3 == 0))"""  # 2 Сумма % 3
"""f = open('zxc.txt')
n = int(f.readline())
s = 0
diff = 10**20
for i in range(n):
    tr = [int(x) for x in f.readline().split()]
    tr = [tr[0] + tr[1], tr[0] + tr[2], tr[1] + tr[2]]
    tr.sort()
    s += tr[2]
    if (tr[2] - tr[1]) % 5 != 0: diff = min(diff, tr[2] - tr[1])
    if (tr[2] - tr[0]) % 5 != 0: diff = min(diff, tr[2] - tr[0])
print(s if s % 5 != 0 else s-diff)"""  # 3.1 Из тройки выбрать 2 числа. Сумма % 5 != 0
"""f = open('zxc.txt')
n = int(f.readline())
s = [0]
for i in range(n):
    tr = [int(x) for x in f.readline().split()]
    tr = [tr[0]+tr[1], tr[0]+tr[2], tr[2]+tr[1]]
    s = [a + b for a in s for b in tr]
    s = {x % 5: x for x in sorted(s)}.values()
print(max(x for x in s if x % 5 != 0))"""  # 3.2
"""f = open('zxc.txt')
n = int(f.readline())

#s[0] - сумма меньших, s[1] - сумма больших

s = [[0, 0]]
for i in range(n):
    pair = [int(x) for x in f.readline().split()]
    if pair[0] % 2 != 0:
        pair.sort()
        # Формирование различных подмножеств
        s = s + [[a1 + pair[0], a2 + pair[1]] for a1, a2 in s] + [pair]

ans = []
for a1, a2 in s:
    if a1 % 2 == 0 and a2 % 2 != 0:
        ans.append(a1 + a2)
print(max(ans))"""  # 4.1 Выбрать пары, первое число в паре - нч, сумма больших - нч, меньших - ч. Макс сумма?
"""f = open('zxc.txt')
n = int(f.readline())

#s[0] - сумма меньших, s[1] - сумма больших

s = [[0, 0]]
for i in range(n):
    pair = [int(x) for x in f.readline().split()]
    if pair[0] % 2 != 0:
        pair.sort()
        # Формирование различных подмножеств
        s = s + [[a1 + pair[0], a2 + pair[1]] for a1, a2 in s] + [pair]
        s = list({(x[0] % 2, x[1] % 2): x for x in sorted(s, key=sum)}.values())

ans = []
for a1, a2 in s:
    if a1 % 2 == 0 and a2 % 2 != 0:
        ans.append(a1 + a2)
print(max(ans))
"""  # 4.2 ЭФФ

"""f = open('zxc.txt')
n = int(f.readline())
s = [0]
M = 0  # Сумма всех чисел
       # Чтобы найти сумму невыбранных чисел, будем вычитать сумму выбранных
       # У меня ЕГЭ через 2 дня... Кому я это вообще пишу?
for i in range(n):
    pair = [int(x) for x in f.readline().split()]
    M += sum(pair)
    s = [a + b for a in s for b in pair]
    s = {x % 5: x for x in sorted(s)}
"""

# VAR 21

"""for n in range(1, 2022):
    s1 = sum([int(i) for i in str(n) if int(i) % 2 == 0])
    s2 = 0
    for i in range(len(str(n))):
        if i % 2 != 0:
            s2 += int(str(n)[i])
    R = abs(s1-s2)
    if R == 11:
        print(n)"""  # 5
"""c = 0
for i in range(1, 1000000):
    s = i
    s = 3 * (s // 10)
    n = 1
    while s < 221:
     s = s + 13
     n = n * 2
    if n == 256:
        print(i)
        c += 1
print()
print(c)
"""  # 6
"""for i in range(201, 300):
    s = '1'*i
    while '111' in s or '222' in s:
        s = s.replace('111', '22', 1)
        s = s.replace('222', '1', 1)
    if s.count('1') == 0:
        print(i)"""  # 12
"""a = 4**34 + 5*4**22 + 4**13 + 2*4**9 + 82
print(hex(a))
d = set()
while a > 0:
    d.add(a%16)
    a//= 16
print(len(d))"""  # 14
"""for a in range(1, 1000):
    g = True
    for x in range(1, 1000):
        f = (x & 105 == 0) <= ((x & 58 != 0) <= (x & a != 0))
        if f == 0:
            g = False
            break
    if g:
        print(a)"""  # 15
"""def f(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return f(n/2)
    return 1 + f(n-1)

c = 0
for n in range(1, 901):
    if f(n) == 9:
        c += 1
print(c)"""  # 16
"""a = [int(i) for i in open('zxc.txt')]
c = 0
m = 0

for i in range(len(a) - 1):
    t = a[i] + a[i+1]
    if (a[i] % 5 == 0 or a[i+1] % 5 == 0) and t % 7 == 0:
        c += 1
        m = max(m, t)
print(c, m)"""  # 17
"""def moves(h):
    return h+1, h*3


from functools import  lru_cache
@lru_cache(None)
def f(h):
    if h >= 64:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h)):
        return 'V2'


for s in range(1, 100):
    print(s,f(s))"""  # 19-21
"""for i in range(1, 1000):
    x = i
    a = 7*x + 27
    b = 7*x - 33
    c = 0
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
        c += 1
        if c == 100000:
            break
    if a == 10:
        print(i)
"""  # 22
"""def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x+1, y) + f(x*3, y)

print(f(2, 26) * f(26, 87))"""  # 23
"""a = open('24 (22).txt').readline()
a = a.split('D')
m = 0
for i in range(len(a) - 1):
    m = max(m, len(a[i] + a[i+1]) + 1)
print(m)"""  # 24
"""def M(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d |= {i, n//i}
    mass = sorted(d)
    if len(d) < 5:
        return 0
    return mass[0]*mass[1]*mass[2]*mass[3]*mass[4]

c = 0
for i in range(500_000_001, 501_000_001):
    t = M(i)
    if 0 < t < i:
        print(t)
        c += 1
        if c == 5:
            break """  # 25
"""f = open('zxc.txt')
n = int(f.readline())
a = [int(i) for i in f]
m = 0
for i in range(n):
    s = 0
    Knech = 0
    for j in range(i, n):
        s += a[j]
        if a[j] % 2 != 0:
            Knech += 1
        if Knech % 10 == 0:
            m = max(m, s)
print(m)"""  # 27A
"""f = open('zxc.txt')
n = int(f.readline())
ps = [10**100]*10
ps[0] = 0
k = 0
s = 0
m = 0

for i in range(n):
    x = int(f.readline())
    s += x
    if x % 2 != 0:
        k += 1
    ost = k % 10
    if s - ps[ost] > m:
        m = s - ps[ost]
    if s < ps[ost]:
        ps[ost] = s
print(m)"""  # 27B

# VAR 24

"""for n in range(10, 1000):
    N = bin(n)[2:]
    N = N + N[1] + N[0]
    R = int(N, 2)
    if R > 90:
        print(n)"""  # 5
"""D = set()
for i in range(1, 10000000):
    d = i
    n = 27
    s = 12
    while s <= 2019:
        s += d
        n += 16
    if n == 171:
        print(i)
        D.add(i)
print()
print(len(D))"""  # 6
"""s = '563' * 121
while '56' in s or '3333' in s:
    s = s.replace('56', '3', 1)
    s = s.replace('3333', '3', 1)
print(s)"""  # 12
"""a = 9**7 + 3**21 - 19

c = 0
while a > 0:
    if a % 3 == 2:
        c += 1
    a //= 3
print(c)"""  # 14
"""for A in range(1, 100):
    g = True
    for x in range(1, 100):
        for y in range(1, 100):
            f = (3*x + 5*y < A) or (x >= y) or (y > 8)
            if f == 0:
                g = False
                break
        if g == False:
            break
    if g:
        print(A)"""  # 15
"""def f(n):
    if n < 4:
        return n-1
    if n % 3 == 0:
        return n + 2*f(n-1)
    return f(n-2) + f(n-3)

print(f(25))"""  # 16
"""a = [int(i) for i in open('zxc.txt')]

c = 0
m = 0
for i in range(len(a)):
    if a[i] % 5 == 0 and a[i] % 6 != 0 and a[i] % 10 != 0 and a[i] % 15 != 0 and a[i] % 16 != 0:
        c += 1
        m = max(m, a[i])
print(c, m)"""  # 17
"""def moves(h):
    a, b = h
    return (a+1, b), (a, b+1), (a*2, b), (a, b*2)


from functools import lru_cache
@lru_cache(None)
def f(h):
    if sum(h) >= 71:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'

c = 0
for s in range(1, 70):
    h = 10, s
    if f(h) == 'V2':
        print(s,f(h))
        c += 1
print(c)"""  # 19-21
"""for i in range(1, 1000000):
    x = i
    a = 0; b = 0
    while x > 0:
     a = a + 1
     b = b + (x % 100)
     x = x // 100
    if a == 2 and b == 15:
        print(i)
"""  # 22
"""def f(x, y):
    if x > y or x == 8:
        return 0
    if x == y:
        return 1
    return f(x**2, y) + f(x+2, y) + f(x*2, y)

print(f(2, 64))"""  # 23
"""a = open('zxc.txt').readline()
s1 = 'BCD'
s2 = 'BDE'
s3 = 'BCE'
c = 0
for i in range(len(a) - 2):
    if a[i] in s1 and a[i+1] in s2 and a[i+2] in s3 and a[i] != a[i+1] and a[i+1] != a[i+2]:
        c += 1
print(c)"""  # 24
"""def find_div(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d |= {i, n//i}
    if len(d) == 3:
        return sorted(d)[-1]
    return 0

for i in range(152346, 957812 + 1):
    t = find_div(i)
    if t != 0:
        print(i, t)"""  # 25
"""f = open('zxc.txt')
n = int(f.readline())
s = [0]

for i in range(n):
    pair = [int(x) for x in f.readline().split()]
    s = [a + b for a in s for b in pair]
    s = {x % 7: x for x in sorted(s)}.values()
print(max(i for i in s if i % 7 != 0))"""  # 27

"""a = open('zxc.txt').readline()
s = ('ABC', 'BAC', 'CAB', 'CBA')
c = 0
m = 0
index = 0
i = 0
while i < len(a):
    if a[i:i+3] in s:
        i += 2
        c += 1
        m = max(m, c)
    elif a[i - 1: i + 2] in s:
        c = 1
        i += 1
    else:
        i += 1
        c = 0
print(m)"""


# 24.1
"""
a = open('24 osnova.txt').readline()

c = 0
m = 0
i = 0
while i < len(a) - 1:
    if a[i] in 'AO' and a[i+1] in 'BCD':
        c += 1
        i += 2
        m = max(m, c)
    else:
        c = 0
        i += 1
print(m)
"""

# 24.2
"""
a = open('24 osnova.txt').readline()

s = ['OB', 'OC', 'OD', 'AB', 'AC', 'AD']
for i in s:
    a = a.replace(i, '*')
a = a.replace('A', ' ').replace('B', ' ').replace('C', ' ').replace('D', ' ').replace('O', ' ').replace('U', ' ')
a = a.split()
print(len(max(a, key=len)))
"""

# 24.3
"""
s = open('24 osnova.txt').readline()

A = ['A', 'O']; B = ['B', 'C', 'D']
n = 0
nmax = 0
i = 1
while i < len(s) :
    if s[i-1] in A and s[i] in B or s[i-1] in B and s[i] in A:
        n = 1
        i += 2
        while i<len(s) and (s[i-1] in A and s[i] in B or s[i-1] in B and s[i] in A):
            n += 1
            i += 2

        nmax = max(nmax,n)
    else : i += 1
print(nmax)
"""

# 25.1
"""
import re

for x in range(1, 10**8 + 1):
    if x % 123 == 0 and re.fullmatch(r'123.*67', str(x)) is not None:
        print(x, x//123)
print()"""

# 25.2
"""if 12367 % 123 == 0:
    print(12367, 12367//123)

for s1 in '0123456789':
    s = int('123' + s1 + '67')
    if s % 123 == 0:
        print(s, s//123)

for s1 in '0123456789':
    for s2 in '0123456789':
        s = int('123' + s1 + s2 + '67')
        if s % 123 == 0:
            print(s, s//123)

for s1 in '0123456789':
    for s2 in '0123456789':
        for s3 in '0123456789':
            s = int('123' + s1 + s2 + s3 + '67')
            if s % 123 == 0:
                print(s, s//123)
"""

# 26
"""f = open('zxc.txt')
n = int(f.readline())

a = [int(i) for i in f]
a.sort(reverse=True)
c = 1
last = a[0]
for i in range(n):
    if a[i] <= last - 3:
        c += 1
        last = a[i]
print(c, last)
"""

# 27A
"""f = open('zxc.txt')
n = int(f.readline())
dlina = []
k_sumok = []

for i in range(n):
    r, k = [int(i) for i in f.readline().split()]
    dlina.append(r)
    k_sumok.append((k-1)//36 + 1)

m = 10**10
ans = 0
for i in range(n):
    s = 0
    for j in range(n):
        s += k_sumok[j] * abs(dlina[j] - dlina[i])
    if s < m:
        m = s
        ans = i
print(m, ans + 1)"""

# 27B
"""f = open('zxc.txt')
n = int(f.readline())
dlina = []
k_sumok = []

for i in range(n):
    r, k = [int(i) for i in f.readline().split()]
    dlina.append(r)
    k_sumok.append((k-1)//96 + 1)

summa = sum(k_sumok)
cost = [0]*n

for i in range(n):
    cost[0] += k_sumok[i] * abs(dlina[0] - dlina[i])


s_prev = k_sumok[0]
s_next = summa - s_prev

for i in range(1, n):
    r = dlina[i] - dlina[i-1]
    cost[i] = cost[i-1] + s_prev*r - s_next*r
    s_prev += k_sumok[i]
    s_next -= k_sumok[i]

print(min(cost), cost.index(min(cost)) + 1)"""

# 5
"""for n in range(1, 1000):
    N = bin(n)[2:]
    if N.count('1') % 2 == 0:
        N = '10' + N[2:] + '0'
    else:
        N = '11' + N[2:] + '1'
    R = int(N, 2)
    if R >= 16:
        print(n)"""

# 8
"""from itertools import product
# 1 3 5 7
s1 = ['16', '36', '56', '76', '61', '63', '65', '67']
c = 0
for i in product('01234567', repeat=5):
    s = ''.join(i)
    if s[0] != "0" and s.count('6') == 1 and all([x not in s for x in s1]):
        c += 1
print(c)"""

# 19-21
"""def moves(h):
    a, b = h
    return (a+1, b), (a, b+1), (a*2, b), (a, b*2)

from functools import lru_cache
@lru_cache(None)
def f(h):
    if sum(h) >= 259:
        return 'end'
    if any(f(x) == 'end' for x in moves(h)):
        return 'p1'
    if all(f(x) == 'p1' for x in moves(h)):
        return 'v1'
    if any(f(x) == 'v1' for x in moves(h)):
        return 'p2'
    if all(f(x) == 'p1' or f(x) == 'p2' for x in moves(h)):
        return 'v2'

for s in range(1, 250):
    h = 17, s
    if f(h) == 'v2':
        print(s,f(h))"""

























































