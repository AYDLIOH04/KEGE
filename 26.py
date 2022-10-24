def timer(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end - start)

    return wrapper

'''
f = open('Задача_1__eki2.txt')
# m, n = [int(k) for k in f.readline().split()]

m, n = map(int, f.readline().split())

a = []
for i in range(n):
    a.append(int(f.readline()))

a.sort()
summ = 0
i = 0
while summ <= m and i < n:
    summ += a[i]
    i += 1
else:
    summ -= a[i]
    i -= 1
print(i)
zh = a[i-1]
summ = summ - zh
for i in range(i, n):
    if summ + a[i] <= m:
        zh = a[i]
print(zh)
'''  # Задача 1 АРХ
'''
f = open('Задача_5__eki4 (2).txt')

n, m = map(int,f.readline().split())

a = [int(i) for i in f]

a.sort()
i = 0
summ = 0
while summ <= m:
    summ += a[i]
    i += 1
t = i - 1
print(t)

zh = a[t-1] # Самое жирное число (последнее, которое было выбранно)
summ = summ - zh
for i in range(t,n):
    if summ + a[i] <= m:
        zh = a[i]
print(zh)

# 7999
# 100
'''  # Задача 2 АРХ
'''
f = open('26/1.txt')
m, n = map(int,f.readline().split())

a = [int(i) for i in f]

a.sort()
summ = 0
i = 0
while summ <= m and i < n:
    summ += a[i]
    i += 1
else:
    summ -= a[i]
    i -= 1
print(i)
zh = a[i-1]
summ -= zh
for i in range(i,n):
    if summ + a[i] <= m:
        zh = a[i]
print(zh)
# 611, 27
'''  # ДЗ 1 АРХ
'''
f = open('26/8.txt')
S, N = map(int,f.readline().split())

a = [int(k) for k in f]
a.sort()

summ = 0
i = 0
while summ <= S and i < N:
    summ += a[i]
    i += 1
else:
    summ -= a[i]
    i -= 1
print(i)
maxim = a[i - 1]
summ -= maxim

for i in range(i ,N):
    if summ + a[i] <= S:
        maxim = a[i]
print(S/maxim)
# 2496
# 450.90625 = 451
# 451 + 2496 - 2947
'''  # ДЗ 8 АРХ
'''
f = open('Задание__1__emu3 (1).txt')
n, k = map(int,f.readline().split())
a = [int(i) for i in f]

a.sort()    # Всего 1000 чисел, их индексы заканчиваются 999 элементом
            # Последние 100 чисел - это числа от 900 до 999
skidka = 0
for i in range(900,1000):
    skidka += 0.2 * a[i]
print(skidka)
print(a[899])
'''  # Задача 1 Скидки

'''
week = 7*24*60*60
start = 1634515200
finish = start + week - 1 # Опять метод +-1 (представь интенсив, который начался 5 числа и длится 7 дней = финиш 11)
f = open('2__eph7.txt')
n = int(f.readline())
a = []  # начала всех процессов
b = []  # концы всех процессов

for i in range(n):
    x, y = map(int,f.readline().split())
    if y == 0:
        y = 2000000000
    a.append(x)
    b.append(y)
a.sort()
b.sort()

i = 0
j = 0
active = 0
maxim = 7768
seconds = 0
for t in range(start,finish + 1):
    while t >= a[i]:
        active += 1
        i += 1
    while t >= b[j]:
        active -= 1
        j += 1
    # maxim = max(maxim, active)

    if active == maxim:
        seconds += 1
print(maxim, seconds)
'''  # UNIX СТАТГРАД 2021
"""
n = int(input())
a, b = [], []
for i in range(n):
    x, y = [int(k) for k in input().split()]
    a.append(x)
    b.append(y)

i = 0 # Указатели массивов
j = 0
active = 0
maxim = 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        active += 1
        i += 1
    elif a[i] == b[j]:
        i += 1
        j += 1
    else:
        active -= 1
        j += 1
    maxim = max(maxim, active)

# Добивочная. Убиваем отставших
if i == len(a):
    while j < len(b):
        active -= 1
        j += 1
    maxim = max(maxim, active)
else:
    while i < len(a):
        active += 1
        i += 1
    maxim = max(maxim, active)

print(maxim)"""  # Два массива + указатели (UNIX ВРЕМЯ)
"""    # Merge SORT
# По усл. массивы уже SORT
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
res = []

i = 0
j = 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        res.append(a[i])
        i += 1
    else:
        res.append(b[j])
        j += 1

while j < len(b):
    res.append(b[j])
    j += 1

while i < len(a):
    res.append(a[i])
    i += 1

print(res)
"""  # Merge SORT + указатели

# 26 задача: Найти количество sr_arifm четных чисел
"""@timer
def f1():
    f = open('26.txt')
    n = int(f.readline())
    a = []
    for i in range(n):
        a.append(int(f.readline()))
    a.sort()

    c = 0
    maxim = 0

    od = set(a)
    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] + a[j]) % 2 == 0:
                sredn = (a[i] + a[j]) // 2
                if sredn in od:
                    c += 1
                    maxim = max(maxim, sredn)
    print(c, maxim)
f1()
print()"""  # 1 Способ <<<Поиск через кортеж>>>  17 СТРОЧЕК!!!
"""def bin_search(x, a):
    left = 0
    right = len(a) - 1
    while (right - left) > 1:
        middle = (right + left) // 2
        if x < a[middle]:
            right = middle
        elif x == a[middle]:
            return True
        else:
            left = middle

    if a[left] == x:
        return True
    if a[right] == x:
        return True

    return False

@timer
def f2():
    f = open('26.txt')
    n = int(f.readline())
    a = []
    for i in range(n):
        a.append(int(f.readline()))
    a.sort()

    c = 0
    maxim = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] + a[j]) % 2 == 0:
                sredn = (a[i] + a[j]) // 2
                if bin_search(sredn, a):
                    c += 1
                    maxim = max(maxim, sredn)
    print(c, maxim)
f2()
print()"""  # 2 Способ <<<Обычный Бин-Поиск>>>   32 СТРОЧКИ!!!
"""@timer
def f3():
    import bisect
    f = open('26.txt')
    n = int(f.readline())
    a = []
    for i in range(n):
        a.append(int(f.readline()))
    a.sort()

    c = 0
    maxim = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (a[i] + a[j]) % 2 == 0:
                sredn = (a[i] + a[j]) // 2
                if sredn == a[bisect.bisect(a, sredn) - 1]:
                    c += 1
                    maxim = max(maxim, sredn)
    print(c, maxim)
f3()
print()"""  # 3 способ <<<Втроенный Бин-Поиск>>> 17 СТРОЧЕК!!!

"""from bisect import bisect
from datetime import datetime
st = datetime.now()
f = open('3__eyr1.txt')
n = int(f.readline())
a = [int(f.readline()) for i in range(n)]
b = tuple(a)
a.sort()
c = 0
nimnim = 10000000000000000
for i in range(n):
    for j in range(i+1, n):
        for l in range(j+1, n):
            if (a[i]+a[j]+a[l]) % 3 == 0:
                sr = (a[i]+a[j]+a[l]) // 3
                if sr == a[bisect(a, sr) - 1]:
                    c += 1
                    nimnim = min(nimnim, sr)
print(c, nimnim)
end = datetime.now()
print(end - st)
# 36 34495210

# 0:00:05.585483
# 0:00:16.533410"""  # Три числа % 3 срзначение в файле бинпоиск

"""
f = open('26-n2.txt')
n = int(f.readline())
a = [0] * 100 # Массив с каунтером чисел от 1 до 100
for i in range(n):
    a[int(f.readline())] += 1 # Заполняем каунт-массив

ans = 0
for i in range(1, len(a)//2): # Перебираем каунт-массив до середины (не включительно 50)
    ans += min(a[i], a[100-i]) # Чтобы сделать пару, она должна существовать, поэтому выбираем минимум из двух каунтеров
ans += a[50]//2 # Смотрим 50-тый элемент (который не учитывался в форе) и тк пары состоят из друг друга, то делим на 2

print(ans)


# Типичный перебор для 27А посчитал...
f = open('26-n2.txt')
n = int(f.readline())
a = []

for i in range(n):
    a.append(int(f.readline()))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == 100:
            ans += 1
            a[i], a[j] = 0, 0
print(ans)
"""  # Робот и ящик 100 штук

"""def bin_search(x, a):
    left = 0
    right = len(a) - 1
    while (right - left) > 1:
        middle = (right + left)//2
        if x < a[middle]:
            right = middle
        elif x == a[middle]:
            return True
        else:
            left = middle

    if a[left] == x:
        return True
    if a[right] == x:
        return True

    return False"""  # Типо бинарный поиск

"""f = open("26_1.txt")

n, s = [int(i) for i in f.readline().split()]

_dict = {}  # Type: [Cost1, Cost2, Cost3, ...]  i < j => Costi <= Costj

for i in range(n):
    Type, Cost = [int(i) for i in f.readline().split()]

    try:
        a = _dict[Type]
        _dict[Type].append(Cost)

    except Exception:
        _dict[Type] = [Cost]

awn_s = 0
awn_n = 0

for i in _dict.keys():
    costs = _dict[i]
    costs.sort()
    s0 = s
    n0 = 0
    for c in costs:
        if c <= s0:
            s0 -= c
            n0 += 1
        else:
            break
    awn_s += s - s0
    awn_n += n0

print(awn_n, awn_s)"""  # Необходимо закупить компоненты. На рынке множество предложений по разным компонентам и по разилчной цене.
          # Предприяте выделяет средства так, чтобы купить все компоненты и при этом купить как можно больше каждого из них,
          # но не портатить на каждый тип более чем S денег. Сколько всего компонентов можно купить и какой будет наименьшая общая потраченая сумма денег.

"""f = open('input.txt')
n = int(f.readline())
k = 30000
d = [[] for i in range(k)]
for i in range(n):
    a, b = [int(i) for i in f.readline().split()]
    d[a].append(b)

ans = 0
maxim = 0
for ryad in range(k):
    nomera = d[ryad]
    for i in range(len(nomera)):
        for j in range(i+1, len(nomera)):
            if abs(nomera[i] - nomera[j]) == 4:
                if min(nomera[i], nomera[j]) + 2 > maxim:
                    maxim = min(nomera[i], nomera[j]) + 2
    if maxim != 0:
        ans = ryad
        break
print(maxim, ans)
f.close()"""  # Ряды в кинотеатре
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
f.close()"""  # 26 Cудно с грузами
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
"""  # 26 Кол-во чисел между СРЗНАЧ и МЕДИАНОЙ
"""f = open('26-44.txt')
n = int(f.readline())
a = [[] for i in range(20)]
for i in range(n):
    x = int(f.readline())
    a[(x - 1) // 500].append(x)

for mass in a: mass.sort()

SUM = 0
last = 0
for i in a:
    if len(i) > 1:
        for j in range(len(i) // 2):
            SUM += i[j] * 0.5
            last = max(last, i[j] * 0.5)
print(int(SUM), int(last))
# 11493372 4877"""  # 26 на группы чисел и скидку
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
print(c, int(minim))"""  # Bisect


