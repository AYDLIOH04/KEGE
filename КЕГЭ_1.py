"""print('a b c d f')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = a and (not b) or (a or b) and c or d
                if f == 0:
                    print(a, b, c, d, int(f))""" # 2
"""
for n in range(1, 100):
    N = bin(n)[2:]
    N = N + str(N.count('1') % 2)
    N = N + str(N.count('1') % 2)
    R = int(N, 2)
    if R > 80:
        print(R)
        break""" # 5
"""c = 0
for i in range(-1000, 10000):
    s = i
    n = 1
    while s > n:
     s = s - 15
     n = n * 5
    if n == 125:
        c += 1
print(c)""" # 6
"""c = 0
from itertools import product
for i in product('БАНКИР', repeat=6):
    s = ''.join(i)
    if s.count('А') <= 1 and s.count('И') <= 1:
        print(s,s.count('А') ,s.count('И') )
        c += 1
print(c)

print(4**6 + 4**5 *5 * 2 + 4**4 * 10)""" # 8
"""a = 103*7**103 - 5*7**57 + 98
perevod = ''
while a > 0:
    perevod = str(a%7) + perevod
    a //= 7

print(sum(int(i) for i in perevod))""" # 14
"""for A in range(-100, 100):
    gg = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            f = (y - x < A) or (7*x + 4*y > 350) or (3*y - 2*x > 45)
            if f == 0:
                gg = False
                break
        if gg == False:
            break
    if gg == True:
        print(A)
        break""" # 15
"""def f(n):
    if n == 0:
        return 3
    if 0 < n <= 15:
        return f(n-1)
    if 15 < n < 100:
        return 2.5 * f(n-3)
    if n >= 100:
        return 3.3 * f(n-2)
print(f(100))""" # 16
"""f = open('zadanie_17.txt')
c, minim = 0, 100000000000
for i in range(10000):
    x = int(f.readline())
    if (x % 4 == 0 or x % 7 == 0) and x % 13 != 0 and x % 17 != 0 and x % 21 != 0 and x % 23 != 0:
        c += 1
        minim = min(minim, x)
print(c, minim)""" # 17
"""def moves(h):
    a, b = h
    return (a+1, b), (a*2, b), (a, b+1), (a, b*2)
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

for s in range(1, 70):
    h = 13, s
    if f(h) == 'V2':
        print(s, f(h))""" # 19-21
"""for i in range(81, 1000):
    x = i
    s = 0
    while x > 0:
     s = s + x % 9
     x = x // 3
    if s == 17:
        print(i)
        break""" # 22
"""def f(x, y):
    if x > y or x == 10 or x == 11:
        return 0
    if x == y:
        return 1
    return f(x+1, y) + f(x+2, y) + f(x*3, y)
print(f(1,8) * f(8, 38))""" # 23
"""a = open('zadanie_24.txt').readline()
l = 3
maxim = 0
for i in range(3, len(a)):
    if a[i:i+3] != a[i-3:i]:
        l += 1
        maxim = max(maxim, l + 2)
    else: l = 3
print(maxim)""" # 24
"""def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


for i in range(7178551, 7178626 + 1):
    if is_prime(i):
        print(i)""" # 25


"""f = open('zadanie_26.txt')
V, K, N = [int(i) for i in f.readline().split()]
masiv = [int(i) for i in f]
masiv.sort()
masiv.reverse()

OBIEM, COUNTER = 0, 0
a = [0]*K
for i in range(N):
    x = masiv[i]
    gg = True
    for j in range(K):
        a[j] += x
        if a[j] > V:
            a[j] -= x
        else:
            gg = False
            break
    if gg == True:
        OBIEM += x
        COUNTER += 1
print(OBIEM, COUNTER)
f.close()""" # 26

"""f = open('zadanie_27_b.txt')
n = int(f.readline())
# Неэффективная
a = [int(i) for i in f]
maxim = 0
for x in range(n):
    for y in range(x+1, n):
        for z in range(y+1, n):
            for w in range(z+1, n):
                t = (a[x] + a[y] + a[z] + a[w])
                if t % 6 == 0:
                    maxim = max(maxim, t)
print(maxim)

# Эффективная (если бы)

# Буду хранить 4 самых максимальных числа с разными остатками на 6
maxim1 = [0]*6
maxim2 = [0]*6
maxim3 = [0]*6
maxim4 = [0]*6
for i in range(n):
    x = int(f.readline())
    for j in range(6):
        if x % 6 == j:
            if x > maxim1[j]:
                a, b, c = maxim1[j], maxim2[j], maxim3[j]
                maxim4[j] = c
                maxim3[j] = b
                maxim2[j] = a
                maxim1[j] = x
            elif x > maxim2[j]:
                a, b = maxim2[j], maxim3[j]
                maxim4[j] = b
                maxim3[j] = a
                maxim2[j] = x
            elif x > maxim3[j]:
                maxim4[j] = maxim3[j]
                maxim3[j] = x
            else:
                maxim4[j] = max(maxim4[j], x)
f.close()
# в итоге я получил максимальные числа с разными остатками на 6
# А как их нормально перебрать я не додумался...
print(maxim1, maxim2, maxim3, maxim4)
print(99997 + 99994 + 99994 + 99987, (99997 + 99994 + 99994 + 99987)% 6 == 0)""" # 27



