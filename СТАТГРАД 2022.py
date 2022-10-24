"""def g(s, f, hod):
    if s == f:
        return 1
    if s > f:
        return 0

    if hod == 3:
        return g(s+2, f, 2) + g(s+1, f, 1)

    return g(s+2, f, 2) + g(s+1, f, 1) + g(s*2, f, 3)

print(g(1, 11, 0))""" # 23 статград 8 февр.
def div(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d |= {i, n//i}
    return sorted(d)
"""


print(sum(1 for i in open('statgrad8_24.txt').readline().split('E') if len(i) >= 10 and 'F' not in i))  
""" # 24 статград 8 февр.
"""def count_div(n):
    a = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            a.append(i)
            if i != n//i:
                a.append(n//i)
    a.sort()
    if len(a) < 5:
        return 0
    return a[-5]

c = 0
for i in range(460000000 + 1, 470000000):
    if count_div(i) > 0:
        c += 1
        print(count_div(i))
        if c == 5:
            break
""" # 25 статград 8 февр.
"""f = open('27-A.txt')
n = int(f.readline())
c = 0
min_ps = [0]*999 # каунтер преф-сумм с отстатком при дел на 999
s = 0
for i in range(n):
    x = int(f.readline())
    s += x
    ost = s % 999

    if ost == 0:
        c += 1

    c += min_ps[ost]
    min_ps[ost] += 1

print(c)""" # 27 статград 8 февр.
"""f = open('27-A (1).txt')
n = int(f.readline())
min_PS = [10000000000] * 10 # массив минимальных сумм с определенной кратностью количества четных на 10
min_PS[0] = 0 # в начальный момент нам подходит любая сумма с количеством четных кратных 10
c = 0 # каунтер четных на определенный период
s = 0 # сумма на определенный период
maxim = 0 
for i in range(n):
    x = int(f.readline())
    s += x # увеличиваем сумму
    if x % 2 == 0: # если число кратно, то мы увеличиваем каунтер четных на 1
        c += 1
    t = c % 10 # статок от деления каунтера четных на 10

    if s - min_PS[t] > maxim: # из суммы вычитаем мин_преф сумму с таким-же остатком от деления количества четных на 10
        maxim = s - min_PS[t]
    min_PS[t] = min(min_PS[t], s) # заполняем массив минимальными суммами с определенной кратностью количества четных элементов в ней на 10

print(maxim)""" # 27 статград 27 окт.
"""f = open('27А_СГ_ДЕКАБРЬ (3).txt')
n = int(f.readline())
a = [int(i) for i in f]


ans = 0
for i in range(n):
    for j in range(i+1, n):
        s = 0
        c = 0
        for l in range(i, j + 1):
            if a[l] % 2 != 0 and a[l] > 0:
                c += 1
            s += a[l]
        if c % 30 == 0:
            ans = max(ans, s)
print(ans)
f.close()

f = open('27Б_СГ_ДЕКАБРЬ (2).txt')
min_ps = [1000000000000000]*30 # массив минимальных сумм с определенной кратностью количества нечетных-положительных(НП) на 30
min_ps[0] = 0 # в начальный момент нам подходит любая сумма с количеством НП кратном 30
n = int(f.readline())
s, c = 0, 0 # постоянная сумма и каунтер НП
# Будем хранить минимальные последовательности с определенным делением количества НП на 30
# С каждой итерации цикла считываем X и добавляем его в S (с каждым шагом S будет увеличиваться или уменьшатся взависимости от значений в файле)
# Так же будем хранить количество НП на определенный момент прочтения файла

ans = 0
for i in range(n):
    x = int(f.readline())
    s += x # увеличиваем сумму
    if x % 2 != 0 and x > 0: # если число НП, то мы увеличиваем каунтер НП на 1
        c += 1
    ost = c % 30 # Остаток от деления количества НП на 30

    if s - min_ps[ost] > ans: # Из суммы с отстаком кол-ва НП (ost) вычитаем минимальную преф. сумму с отстаком(ost)
        # Допустим, в S = 32 кратных числа (ost = 2), тогда вычтем из него минимальную сумму, у которой тоже остаток при делении на 30 равен 2.
        # Т.е. при вычитании остатки будут убиваться
        ans = s - min_ps[ost]

    min_ps[ost] = min(min_ps[ost], s) # Обновляем, если требуется, минимальные суммы
print(ans)
f.close()""" # 27 статград 24 дек. С ОБЪЯСНЕНИЕМ ПРЕФ-СУММ
"""
# Эфф 1 ПРО 100ЕГЭ
f = open('txt')
n = int(f.readline())
massiv = []
for i in range(n):
    x, y = [int(j) for j in f.readline().split()]
    massiv.append((x, y))

massiv.append((-1, 1))
massiv = list(set(massiv))
massiv.sort()

otv_ryad = - 1
max_sv = - 1
c = 0

for i in range(1, len(massiv)):
    ryad = massiv[i][0]
    mesto = massiv[i][1]
    ryad_pred = massiv[i-1][0]
    if ryad_pred == ryad:
        if mesto % 2 == 0:
            c += 1
            if c > max_sv:
                max_sv = c
                otv_ryad = ryad
    else:
        if mesto % 2 == 0:
            c = 1
        else:
            c = 0
print(max_sv, otv_ryad)

# Эфф 2 АРа
f = open('txt')
n = int(f.readline())
massiv = [set() for i in range(10001)]

for i in range(n):
    ryad, mesto = [int(j) for j in f.readline().split()]
    if mesto % 2 == 0:
        massiv[ryad].add(mesto)

maxim  = 0
ans_ryad = 0

for i in range(10001):
    if len(massiv[i]) > maxim:
        maxim = len(massiv[i])
        ans_ryad = i 
print(maxim, ans_ryad)
""" # 26 статград 30 март (Частицы)
"""f = open('27-B__kglq__ki76.txt')
n = int(f.readline())

ans = 0
line = [] # ОЧЕРЕДЬ - массив для ста ПС, считанных до текущей
line.append(0) # добавили "пустую" сумму
s = 0
for i in range(99):
    s += int(f.readline())
    line.append(s)

k_ps = [0] * 999 # СВАЛКА

for i in range(99, n):
    s += int(f.readline())
    ans += k_ps[s % 999]

    # Сброс line[0] на свалку
    ost = line[0] % 999
    k_ps[ost] += 1

    del line[0]
    line.append(s)
print(ans)""" # 27 статград 30 март. (Подпосл: Более из 100 элементов, сумма кратна 999)
"""# +1, +2, *2 в сумме 60-s камней
def moves(h):
    a, SUM = h
    if a <= SUM:
        return (a + 1, SUM - 1), (a+2, SUM - 2), (a*2, SUM - a)
    if SUM >= 2:
        return (a + 1, SUM - 1), (a + 2, SUM - 2)
    if SUM == 1:
        return (a + 1, SUM - 1)

from functools import lru_cache
@lru_cache(None)
def f(h):
    if h[0] >= 51:
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

for s in range(1, 55):
    h = s, 60-s
    print(s, f(h))
# 45 V2
# 22, 42 V3
# Тут нужно ручками подумать и понять, что ответ 24 P2""" # 19-21 статград 27 апр.
"""s = open('input.txt').readline()
s = s.replace('D', 'C')
s = s.split('C')
maxim = 0
for i in range(len(s) - 3):
    sub = f'{s[i]}C{s[i+1]}C{s[i+2]}C{s[i+3]}'
    maxim = max(maxim, sub)
print(maxim)""" # 24 статград 27 апр.
"""def f(n):
    c = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                c += 1
            if i != n//i and n//i % 2 == 0:
                c += 1
    return c

a = 900_000_000
left = int((a//2)**0.5)
k = 0
for i in range(left, 10000000):
    x = (i**2) * 2
    t = f(x)
    if a <= x:
        if t % 2 != 0:
            print(x - a, t)
            k += 1
            if k == 5:
                break""" # 25 статград 27 апр.
"""f = open('input.txt')
n = int(f.readline())
a = [[0]*10001 for i in range(10001)]
for i in range(n):
    x, y = [int(j) for j in f.readline().split()]
    a[x][y] = 1

mlen = 0
mryad = 0
mx = 0
for x in range(1, 10001):
    k = 0
    ryad = 10**20
    for y in range(1, 10001):
        if a[x][y] == 1:
            ryad = min(ryad, x-1, y-1, 10000-x, 10000-y)
            k += 1
            if k > mlen or (k == mlen and ryad > mryad):
                mlen = k
                mx = x
        else:
            k = 0
            r = 10**20
print(mlen, mryad)""" # 26 статград 27 апр. лучше рисунок нарисовать
"""
f = open('27-A_сг27.04.txt')
n = int(f.readline())

a = [int(i) for i in f]
count = 0

for i in range(n):
    mult = 1
    for j in range(i, n):
        mult *= a[j]
        if mult % 980_869 != 0:
            count += 1
print(count) # >>> 203185



f = open('27-B_сг27.04.txt')
n = int(f.readline())
# 980_869 = 89 * 103 * 107
ind89, ind103, ind107 = 0, 0, 0
count = 0

for i in range(1, n + 1): # Чтоб не было проблем с подсчетом количества
    x = int(f.readline())
    if x % 89 == 0:
        ind89 = i
    if x % 103 == 0:
        ind103 = i
    if x % 107 == 0:
        ind107 = i

    count += (i - min(ind89, ind103, ind107))
print(count) # >>> 346556678""" # 27 статград 27 апр. (кол-во подпосл, mult % 980_869 != 0)
"""# 18160655955024 524908
f = open('dsr_28B.txt')
n = int(f.readline())
a = [int(i) for i in f]

ps = [0]
s = 0
for i in range(3):
    for j in a:
        s += j
        ps.append(s)

otv = 1000000000000000000000000
ans = 0
SUM = a[n//2] * (n//2)
for i in range(1, n//2):
    SUM += (a[i] + a[-i]) * i


for i in range(1, n):
    start = n + i
    SUM -= ps[start + n//2] - ps[start]
    SUM += ps[start] - ps[start - n//2]
    if SUM < otv:
        otv = SUM
        ans = i
print(otv, ans)
f.close() """ # 27 ДОСРОК

"""f = open('Demo27A.txt')
n = int(f.readline())
a = [int(i) for i in f]
ans = 0
maxim = 0
for i in range(n):
    sum_temp = 0
    len_temp = 0
    for j in range(i, n):
        sum_temp += a[j]
        len_temp += 1
        if sum_temp % 43 == 0:
            if sum_temp > maxim:
                maxim = sum_temp
                ans = len_temp
            if sum_temp == maxim:
                ans = min(ans, len_temp)
print(maxim, ans)
f.close()


f = open('Demo27B.txt')
n = int(f.readline())

min_ps = [10000000000000000] * 43
min_ps[0] = 0
ind_ps = [-100000000] * 43
ind_ps[0] = -1
max_sum = 0
ind_min_sum = 1000000000000000000000000000000000000000000000

sum_temp = 0
for i in range(n):
    x = int(f.readline())
    sum_temp += x
    ostatok = sum_temp % 43

    if sum_temp - min_ps[ostatok] > max_sum:
        max_sum = sum_temp - min_ps[ostatok]
        ind_min_sum = i - ind_ps[ostatok]

    if sum_temp - min_ps[ostatok] == max_sum:
        ind_min_sum = min(ind_min_sum, i - ind_ps[ostatok])

    if sum_temp < min_ps[ostatok]:
        min_ps[ostatok] = sum_temp
        ind_ps[ostatok] = i

print(max_sum, ind_min_sum)
f.close()
""" # 27 Демо

