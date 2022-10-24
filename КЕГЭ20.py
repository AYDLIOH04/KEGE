'''
# 2
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x <= y) == (z <= w)) or (x and w)
                if f == 0:
                    print(x,y,z,w,int(f))


# 5
for x in reversed(range(100,1000)):
    for y in reversed(range(100,1000)):
        x, y = str(x), str(y)
        arr = []
        arr.append(int(str(int(x[2]) + int(y[2]))))

        arr.append(int(str(int(x[1]) + int(y[1]))))
        arr.append(int(str(int(x[0]) + int(y[0]))))
        arr.sort()
        arr.reverse()

        ans = str(arr[0]) + str(arr[1]) + str(arr[2])
        if int(ans) == 16118 and (int(x) == 307 or int(y) == 307):
            print(x,y)

# 6
for i in range(-1000,1000):
    s = i
    n = 105
    while n > s:
        s = s + 5
        n = n - 2
    if n == 75:
        print(i)

# 8
from itertools import product
ans = 0
for i in product("NASTY", repeat = 15):
    if (i[0] == 'A' or i[0] == 'Y') and (i[14] == 'A' or i[14] == 'Y') and (i.count('N') <= 3) and (i.count('A') <= 3) and (i.count('S') <= 3) and (i.count('T') <= 3) and (i.count('Y') <= 3):
        ans += 1
print(ans)

# 24024000

# 12
a = '1' + '0' * 75
while '10' in a or '1' in a:
    if '10' in a:
        a = a.replace('10', '001', 1)
    else:
        a = a.replace('1', '00', 1)
print(a.count('0'))


# 14
a = (66 + 6**2019) * (6**2019) + 66 + 6**6
b = 0
while a > 0:
    b += a % 6
    a //= 6
print(b)


# 15
for N in range(1,100):
    c = 0
    for x in range(1,100):
        f = (  (not(40 <= x <= 46)) <= (not(30 <= x <= 50))  ) and (   (not(N <= x <= 61)) <= (40 <= x <= 46)  )
        if f:
            c += 1
    if c > 25:
        print(N)


# 16
def f(n):
    if n < 10:
        return n
    return f(n) * f(n-2)

def g(n):
    if n < 11:
        return n * 3
    if n > 10 and n % 7 != 0:
        return f(n**2) + f(n**2 + 1) + f(n**n)
print(g(10) ** f(2) + f(5))


# 17
f = open('Задание_17__fpxb.txt')
a = [int(i) for i in f]
n = len(a)

c = 0
ans = 0
for i in range(n-1):
    if abs(a[i] - a[i+1]) % 42 == 0:
        c+=1
        ans = max(ans, a[i]+a[i+1])
print(c,ans)

# 19 - 21
def moves(h):
    return h+2, h*2

def f(h):
    if h >= 25:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'
for s in range(1,100):
    print(s,f(s))

# 22
for i in range(1,100):
    x = i
    q = 9
    l = 3
    while x >= q:
        l += 1
        x -= q
    m = x
    if m < l:
        m = l
        l = x
    if l == 7 and m == 8:
        print(i)

# 23
def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x+2,y) + f(x+3,y) + f(x+x-1,y)
print(f(2,11))
# <=>
a = [0]*30
a[2] = 1
for i in range(3,15):
    a[i] = a[i-2] + a[i-3]
    if i % 2 != 0:
        a[i] += a[i // 2 + 1]
print(a[11])

# 24
f = open('Задание_24__fpxa.txt')
c = 0
for i in f:
    if i.count('S') == i.count('X'):
        c += 1
print(c)

#25
# можно оптимизировать на доли секунд с помощью лру_кашэ
def find_div(n):
    a = []
    for i in range(1,int(n**0.5) + 1):
        if n % i == 0:
            a.append(i)
            if i != n//i:
                a.append(n//i)
    clon = []
    for i in a:
        gg = True
        for j in range(2,int(i**0.5) + 1):
            if i % j == 0:
                gg = False
        if gg == True:
            clon.append(i)
    clon.sort()
    return clon[1:]
c = 0
for i in range(420001, 440000):
    arr = (find_div(i))
    M = sum(arr)//len(arr)
    if M % 42 == 24:
        c += 1
        print(i)
    if c == 5:
        break


# 27

# Не делятся на 28
# 14 * 2, 7 * 4, 28 - нам нафиг ненужон

nk2, nk4, nk7, nk14, nk28 = 0, 0, 0, 0, 0
ans = 0
f = open('Задание_27_A__fpx5.txt')
n = int(f.readline())

for i in range(n):
    x = int(f.readline())
    if x % 28 != 0:
        if x % 14 == 0:
            ans = max(ans, x * nk2)
        elif x % 7 == 0:
            ans = max(ans, x * nk4)
        elif x % 4 == 0:
            ans = max(ans, x * nk7)
        elif x % 2 == 0:
            ans = max(ans, x * nk14)
        else:
            ans = max(ans, x * nk28)

    if x % 2 != 0 and x > nk2:
        nk2 = x
    if x % 4 != 0 and x > nk4:
        nk4 = x
    if x % 7 != 0 and x > nk7:
        nk7 = x
    if x % 14 != 0 and x > nk14:
        nk14 = x
    if x % 28 != 0 and x > nk28:
        nk28 = x
print(ans)
'''




