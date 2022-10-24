'''
# ЗАДАЧА 1: дано число n, затем n чисел, найти количество пар чисел
#произведение которых чётно

    #1 способ - неэффективная программа
#при большом n прога умрет(
n = int(input())
c = 0
a = []
for i in range(n):
    a.append(int(input()))
for i in range(n):
    for j in range(i+1,n):
        if (a[i]*a[j])%2==0:
            c+=1
print(c)

    #2 способ - комба
n = int(input())
rasim = 0
a = []
for i in range(n):
    x = int(input())
    if x%2==0:
        rasim+=1

#rasim - кол-во четных чисел
#edem - кол-во нечентых чисел
edem = n - rasim
# k = все четные числа взятые с самим собой + четные числа с нечетными в паре
k = rasim*(rasim-1)//2 + rasim*edem
print(k)

    #3 способ - ДИНАМИКА
n = int(input())
chet,nechet,ans = 0,0,0
for i in range(n):
    x = int(input())
    if x%2==0:
        ans += chet + nechet
        chet+=1
    else:
        ans += chet
        nechet+=1
print(ans)


# ЗАДАЧА 2: дано число n, затем n чисел, найти количество пар чисел
#произведение которых делится на 3

    #1 способ - комба
k3 = 0
n = int(input())        #либо оба числа :3 , либо одно :3, а второе !:3
for i in range(n):      #если x:3, x - любое число
    x = int(input())    #если x!:3, тогда x образует пару с числами :3
    k3+= (x%3==0)       #ыыы отказ от if ыыыыы
ans = k3*(k3-1)//2 + k3*(n-k3)      #СУУУПЕР ИЗИ!!!
#ans = ребра в полном графе + ребра в двудольном

    #2 способ
n = int(input())
k3 = 0
nekr3 = 0
for i in range(n):
    x = int(input())
    if x%3==0: #то он образует пары со всеми прочитанными числами
        ans += k3 + nekr3
        k3+=1
    else: #то есть икс !: 3, и ответ надо увеличить
          #только на k3 (количество чисел среди прочитанных, которые :3)
        ans +=k3
        nekr3+=1
print(ans)


# ЗАДАЧА 3: дано число n, затем n чисел
#найти MAX произведение пар чисел, кратное 5

    #1 способ - статика
#надо два числа: самое большое :5, и второе: либо пердмакс :5
#либо макс !:5
m5 = 0
pm5 = 0
mnekr = 0
n = int(input())
for i in range(n):
    x = int(input())
    if x%5==0:
        if (x > m5):
            pm5 = m5 #вице-президент
            m5 = x #президент(не сыр)
        elif (x > pm5):
            pm5 = x
    elif(x > mnekr):
            mnekr = x   #макс некратное, чтоб потом умножить на m5
ans = max(m5*mnekr, m5*pm5)
print(ans)

    #2 способ - динамика
m5 = 0  #макс число :5
m = 0   #макс число !:5
ans = 0
n = int(input())
for i in range(n):
    x = int(input())
    if x%5==0:
        if(x*m>ans):    #если x:5, то умножаем его на max !:5 число
            ans = x*m
    else:               #если x!:5, то умножаем его на max :5 число
        if (x*m5>ans):
            ans = x*m5

    #икс обработали, выкинем его на свалку
    #когда икс попадает на свалку, возможно он настолько большой
    #что заменяет собой m и m5. Это надо проверить

    if (x%5==0):    #почему не через and? а хуй его знает)) Типо лагает else
        if(x>m5):
            m5 = x
    else:
        if (x>m):   # X может быть и m и m5 одновременно, поэтому if
            m = x
print(ans)


# ЗАДАЧА 4: дано число n, затем n чисел
#найти количество пар чисел произведение которых :6

    #1 способ - динамика
nekr = 0
k2 = 0 # :2, но !:6 (т.е. не учитываются k6)
k3 = 0 # :3, но !:6 (т.е. нечётные)
k6 = 0 # :6

#ИНТЕРЕСНЫЙ(ОЧЕНЬ) ФАКТ >>> nekr+k2+k3+k6 == i
n = int(input())
ans = 0
for i in range(n):
    x = int(input())
    if (x%6==0):
        ans +=i
        k6+=1
    elif(x%3==0):
        ans += k2+k6
        k3+=1
    elif(x%2==0):
        ans += k3+k6
        k2+=1
    else:
        ans +=k6

    #ответ подсчитан, остался maintenance - поддерживающая работа

    if (x%6 == 0):
        k6+=1
    elif (x%3 == 0):
        k3+=1
    elif (x%2 ==0):
        k2+=1
    else:
        nekr +=1
print(ans)


#В ТОМ ЧИСЛЕ КРАТНЫЕ 6
n = int(input())
k2 = 0
k3 = 0
k6 = 0

ans = 0
for i in range(n):
    x = int(input())
    if (x % 6 == 0):
        ans += i
    elif (x % 3 == 0):
        ans += k2
    elif (x % 2 == 0):
        ans += k3
    else:
        ans+=k6

    #сброс иксов на свалку)
    if (x % 6 == 0):
        k6 += 1
    if (x % 3 == 0):
        k3 += 1
    if (x % 2 == 0):
        k2 += 1
print(ans)

#########
f = open('27_1.txt')
n,x = [int(i) for i in f.readline().split()]
print(n,x)
a = [int(i) for i in f]
'''  # Пары чисел
import time

'''
#########################################################################################
# ПАРЫ ЧИСЕЛ
# 27.1
# cумма выбранных не делилась на 7 и при этом была MAX

f = open('Задание_27_A__asf6.txt')
n = int(f.readline())
s = 0
md = 100000000000000000
for i in range(n):
    a,b = [int(s) for s in f.readline().split()]
    s += max(a,b)
    diff = abs(a-b)
    if diff % 7 != 0:
        md = min(md,diff)

if s % 7 != 0:
    print(s)
else:
    print(s-md)
# ans A = 150214
# ans B = 52303520

# 27.2
# cумма выбранных не делилась на 7 и при этом была MAX
n = int(input())
s = 0
mdiff1 = 1000000000000000000
mdiff2 = 1000000000000000000
for i in range(n):
    a,b = [int(k) for k in input().split()]
    s += max(a,b)
    diff = abs(a-b)
    if diff % 3 == 1:
        if diff < mdiff1:
            mdiff1 = diff
    if diff % 3 == 2:
        if diff < mdiff2:
            mdiff2 = diff
if s % 3 == 0:
    print(s)
elif s % 3 == 1:
    print(s - mdiff1)
elif s % 3 == 2:
    print(s - mdiff2)

a = 1234
b = 5678
c,maxim = 0,-100000000000000000000000000
for i in range(a,b+1):
    if i % 3 == 0:
        c+=1
        maxim = max(maxim,i)
print(c,maxim,sep='')
'''  # Две кучи
'''
#########################################################################################
# Префиксные (частичные) суммы. Ищем максимальную цепочку (сумму нескольких подряд идущих)
# S(m) - S(k) = X(k+1) + X(k+2) + ... + X(m-1) + X(m) <<< cумма среза последовательности (if m > k)
# Если ищем max_SUM/min_SUM, то находим min_PS/max_PS и вычитаем

# Задача 1
# Найти MAX сумму цепочки последовательных чисел.

# неэфф O(n^3)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

maxim = -1000000000000000
for i in range(n):  # левый конец
    for j in range(i, n):  # правый конец
        s = 0
        for k in range(i,j+1):
            s += a[k]
        if s > maxim:
            maxim = s
print(maxim)


# неэфф O(n^2)
n = int(input())
a = []
maxim = -1000000000000000
for i in range(n):
    a.append(int(input()))

for i in range(n):
    s = 0
    for j in range(i,n):
        s += a[j]
    if s > maxim:
        maxim = s
print(maxim)

# эфф O(n)
# Если ищем MAX/MIN, то находим min_PS/max_PS и вычитаем из S
# надо хранить текущую префиксную сумму и минимальную префиксную сумму
n = int(input())
ans = -10000000000000000
min_ps = 0  # минимальная префиксная сумма
s = 0  # начальная префиксная сумма S{-1}

for i in range(n):
    x = int(input())
    s += x
    ans = max(s - min_ps, ans)
    min_ps = min(s, min_ps)

    if (s - min_ps) > ans:
        ans = s - min_ps
    if s < min_ps:
        s = min_ps
print(ans)


#1
n = int(input())
pref = [0]*n
pref[0] = int(input())
for i in range(1,n):
    pref[i] = pref[i-1] + int(input())
print(pref)


#2
n = int(input())
pref = [0]*n
pref[0] = int(input())
for i in range(1,n):
    pref[i] = pref[i-1] * int(input())
print(pref)


#3
n = int(input())
pref = [0]*n
pref[0] = int(input())
for i in range(1,n):
    pref[i] = pref[i-1] + int(input())
print(sum(pref))


#4
n = int(input())
pref = [0]*n
pref[0] = int(input())
ans = pref[0]
for i in range(1,n):
    pref[i] = pref[i-1] + int(input())
    ans *= pref[i]
print(ans)


#5
n = int(input())
pref = [0]*n
pref[0] = int(input())
counter = int(pref[0] % 2 == 0)
for i in range(1,n):
    pref[i] = pref[i-1] + int(input())
    counter += pref[i] % 2 == 0
print(counter)


#6
n = int(input())
pref = [0]*n
pref[0] = int(input())
counter = int(pref[0] % 10 != 0)
for i in range(1,n):
    pref[i] = pref[i-1] + int(input())
    counter += (pref[i] % 10 != 0)
print(counter)


#7
n = int(input())
pref = [0]*n
pref[0] = int(input())
ans = pref[0]
for i in range(1,n):
    pref[i] = pref[i-1] + int(input())
    if i % 2 == 0:
        ans += pref[i]
    else:
        ans -=pref[i]
print(ans)


#8
n = int(input())
pref = [0]*n
diffs = [0]*n
pref[0] = int(input())
for i in range(1,n):
    pref[i] = pref[i-1] + int(input())
    diffs[i-1] = pref[i] - pref[i-1]
print(diffs)


#9
n = int(input())
pref = [0]*n
pref[0] = int(input())

minim = pref[0]
maxim = 0

for i in range(1,n):
    pref[i] = pref[i-1] + int(input())

    if pref[i] > maxim:
        maxim = pref[i]
    if pref[i] < minim:
        minim = pref[i]
print(maxim-minim)


#10
n = int(input())
pref = [0]*n
pref[0] = int(input())
maxim = -1
for i in range(1,n):
    pref[i] = pref[i-1] + int(input())
    if pref[i] % 5 == 0:
        maxim = i + 1


#11
n = int(input())
ans = -1

pref = [0]*n
pref[0] = int(input())
for i in range(1,n):
    pref[i] = pref[i-1] + int(input())
    if pref[i] % 10 == 0 and pref[i] % 29 == 0:
        ans = i + 1, pref[i]
print(ans)


#12
def simple(n):
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
pref = [0]*n
pref[0] = int(input())
ans = -1
for i in range(1,n):
    pref[i] = pref[i-1] + int(input())
    if simple(pref[i]) and pref[i] >= ans:
        ans = pref[i]
print(ans)


#13
def prime(n):
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
pref = [0]*n
pref[0] = int(input())
for i in range(1,n):
    pref[i]= pref[i-1] + int(input())
print(not prime(sum(pref)))


#14
n = int(input())
pref = [0]*n
pref[0] = int(input())
ans = 100000000000000000
for i in range(1,n):
    pref[i] = pref[i-1] + int(input())

for i in range(n):
    for j in range(i+1,n):
        if pref[i]*pref[j] % 6 == 0:
            ans = min(pref[i]*pref[j],ans)
if ans < 10000000000000000000000:
    print(ans)
else:
    print(-1)


#15
n = int(input())
pref = [0]*n
pref[0] = int(input())
ans = 1000000000
for i in range(1, n):
    pref[i] = pref[i-1] + int(input())

for i in range(n):
    for j in range(i+1,n):
        if pref[i]*pref[j] % 10 == 0:
            ans = min(ans,pref[i]*pref[j])
if ans < 10000000000000000000000:
    print(ans)
else:
    print(-1)


#16
n = int(input())
pref = [0]*n
pref[0] = int(input())
ans = -1
for i in range(1, n):
    pref[i] = pref[i-1] + int(input())

for i in range(len(pref)):
    for j in range(i+1,len(pref)):
        if pref[i]*pref[j] % 15 == 0:
            ans = max(ans,pref[i]*pref[j])
print(ans)


# 17
n = int(input())
pref = [0] * n
ans = 1000000000000000000000000000
pref[0] = int(input())
if pref[0] % 2 == 1:
    ans = min(ans, pref[0]) # нужна минимальная сумма, чтоб потом вычесть её

for i in range(1, n):
    pref[i] = pref[i - 1] + int(input())
    if pref[i] % 2 == 1 and i != n - 1:
        ans = min(ans,pref[i])

if pref[-1] % 2 == 0:
    print(pref[-1])
else:
    print('BAD')
    print((pref[-1] - ans) if ans > 1000000000000 else -1)


#18
n = int(input())
pref = [0]*n
min_ps = 100000000000000000000000000

pref[0] = int(input())
if pref[0] % 2 != 0:
    min_ps = min(pref[0],min_ps)

for i in range(1,n):
    pref[i] = pref[i-1] + int(input())
    if pref[i] % 2 != 0 and i != n - 1:
        min_ps = min(pref[i],min_ps)

if pref[-1] % 2 != 0:
    print(pref[-1])
else:
    print(pref[-1] - min_ps if min_ps < 10000000000000 else -1)


#19
n = int(input())
pref = [0]*n
min_ps = 1000000000000000000
pref[0]= int(input())
if pref[0] % 2 != 0:
    min_ps = min(min_ps,pref[0])

for i in range(1,n):
    pref[i] = pref[i-1] + int(input())
    if pref[i] % 2 != 0 and i != n - 1:
        min_ps = min(min_ps,pref[i])

if pref[0] % 2 == 0:
    print(pref[0])
else:
    print(pref[0] + min_ps if min_ps < 100000000000000 else -1)


#20
n = int(input())
pref = [0]*n
min_ps = 10000000000000000000000000000
pref[0] = int(input())

if pref[0] % 2 != 0:
    min_ps = min(min_ps,pref[0])

for i in range(1,n):
    pref[i] = pref[i-1] + int(input())
    if pref[i] % 2 != 0 and i != n - 1:
        min_ps = min(min_ps,pref[i])

if pref[0] % 2 != 0:
    print(pref[0])
else:
    print(pref[0] + min_ps if min_ps < 10000000000000 else -1)


#21
minim = [10000000000]*3
minim[0] = 0
maxim, summ = 0,0

n = int(input())
for i in range(n):
    x = int(input())
    summ += x 
    ost = summ % 3
    if (summ - minim[ost] > maxim):
        maxim = summ - minim[ost]
    if summ < minim[ost]:
        minim[ost] = summ
print(maxim)


#22
minim = [1000000000000000]*3
minim[0] = 0
maxim,summ = 0,0
n = int(input())
ind = [-1]*3
for i in range(n):
    x = int(input())
    summ += x
    ost = summ % 3

    if (summ - minim[ost] > maxim):
        maxim = summ - minim[ost]
        dlina = i - ind[ost]
    if summ < minim[ost]:
        minim[ost] = summ
        ind[ost] = i

print(dlina)


#23
minim = [1000000000000000]*5
minim[0] = 0
maxim,summ = 0,0
ind = [-1]*5
n = int(input())
for i in range(n):
    x = int(input())
    summ += x
    ost = summ % 5

    if summ - minim[ost] > maxim:
        maxim = summ - minim[ost]
        dlina = i - ind[ost]
    if summ < minim[ost]:
        minim[ost] = summ
        ind[ost] = i
print(maxim - dlina)


#24
minim = [1000000000000]*7
minim[0] = 0
ind = [-1]*7
maxim,summ = 0,0
n = int(input())
for i in range(n):
    x = int(input())
    summ += x
    ost = summ % 7

    if summ - minim[ost] > maxim:
        maxim = summ - minim[ost]
        dlina = i - ind[ost]
    if summ < minim[ost]:
        minim[ost] = summ
        ind[ost] = i
print(maxim * dlina)


#25
minim = [1000000000000000]*8
minim[0] = 0
ind = [-1]*8
maxim = 0
summ = 0
n = int(input())
for i in range(n):
    x = int(input())
    summ += x
    ost = summ % 8
    if summ - minim[ost] > maxim:
        maxim = summ - minim[ost]
        dlina = i - ind[ost]
    if summ < minim[ost]:
        minim[ost] = summ
        ind[ost] = i
print(maxim // dlina)


#26
n = int(input())
pref = [0]*n
pref[0] = int(input())
for i in range(1,n):
    pref[i] = pref[i-1] + int(input())
print(*pref)


# 27
n = int(input())
pref = [0] * n
pref[0] = int(input())
diff = [0] * n
for i in range(1, n):
    pref[i] = pref[i - 1] + int(input())
    diff[i - 1] = pref[i] - pref[i - 1]
diff.sort()
print(*diff)


#28
n = int(input())
pref = [0]*n
pref[0] = int(input())
ans = -1
for i in range(1,n):
    pref[i] = pref[i-1] + int(input())
    if pref[i] % 100 == 0:
        ans = pref[i]
print(ans)


#29
n = int(input())
pref = [0]*n
pref[0] = int(input())
min_ps = 10000000000000000000
for i in range(1,n):
    pref[i] = pref[i-1] + int(input())
    if pref[i] % 2 != 0:
        min_ps = min(min_ps,pref[i])

if pref[0] % 2 == 0:
    print(pref[0])
else:
    print(pref[0] + min_ps if min_ps < 100000000 else -1)


#30
min_ps = [100000]*3
maxim,summ = 0,0
min_ps[0] = 0
n = int(input())
for i in range(n):
    x = int(input())
    summ += x
    ost = summ % 3
    if summ - min_ps[ost] > maxim:
        maxim = summ - min_ps[ost]
    if summ < min_ps[ost]:
        min_ps[ost] = summ
print(maxim)









        # HARD DZ
        
# ('fileA__d8ld.txt')
# ('fileB__d8le.txt')

# 1-3
f = open('fileB__d8le.txt')
n = int(f.readline())
minPS = [100000000000] * 120
minPS[0] = 0
maxim, summ = 0, 0

for i in range(n):
    x = int(f.readline())
    summ += x
    ost = summ % 120
    if summ - minPS[ost] > maxim:
        maxim = summ - minPS[ost]
    if summ < minPS[ost]:
        minPS[ost] = summ
print(maxim)


#4-6
f = open('fileA__d8ld.txt')
n = int(f.readline())

minim, summ = -10e16,0
maxPS = [10e16]*17
maxPS[0] = 0

for i in range(n):
    x = int(f.readline())
    summ += -x
    ost = summ % 17

    if summ - maxPS[ost] > minim:
        minim = summ - maxPS[ost]
    if summ < maxPS[ost]:
        maxPS[ost] = summ

print(-minim)


# 7-8
f = open('fileA__d8ld.txt')
n = int(f.readline())

minPS, minPS[0] = [10e16] * 13, 0
maxim = 0

maxPS, maxPS[0] = [-10e16] * 3, 0
minim = 10e10

summ = 0

for i in range(n):
    x = int(f.readline())
    summ += x
    ostMAX = summ % 13
    ostMIN = summ % 3

    if summ - minPS[ostMAX] > maxim:
        maxim = summ - minPS[ostMAX]
    if summ < minPS[ostMAX]:
        minPS[ostMAX] = summ

    if summ - maxPS[ostMIN] < minim:
        minim = summ - maxPS[ostMIN]
    if summ > maxPS[ostMIN]:
        maxPS[ostMIN] = summ

print(abs(maxim - minim))


#9
f = open('fileB__d8le.txt')
n = int(f.readline())

minPS,minPS[0] = [16e10]*9,0
maxim = 0

maxPS,maxPS[0] = [-16e10]*8,0
minim = 10e10

summ = 0
for i in range(n):
    x = int(f.readline())
    summ += x
    ostMAX = summ % 9
    ostMIN = summ % 8
    maxim = max(maxim, summ - minPS[ostMAX])
    minim = min(minim, summ - maxPS[ostMIN])

    minPS[ostMAX] = min(summ, minPS[ostMAX])
    maxPS[ostMIN] = max(summ, maxPS[ostMIN])

print(abs(maxim - minim))

#10
f = open('fileB__d8le.txt')
n = int(f.readline())

minX,minX[0] = [16e10]*17,0
minY,minY[0] = [16e10]*6,0

maximX, maximY, summ = 0, 0, 0
for i in range(n):
    x = int(f.readline())
    summ += x
    ostX = summ % 17
    ostY = summ % 6
    maximX = max(maximX, summ - minX[ostX])
    maximY = max(maximY, summ - minY[ostY])

    minX[ostX] = min(summ, minX[ostX])
    minY[ostY] = min(summ, minY[ostY])

print(maximX, maximY, maximX + maximY)


#11-12
f = open('fileB__d8le.txt')
n = int(f.readline())

minX,minX[0] = [16e10]*99,0
minY,minY[0] = [16e10]*128,0

maximX, maximY, summ = 0, 0, 0
for i in range(n):
    x = int(f.readline())
    summ += x
    ostX = summ % 99
    ostY = summ % 128
    maximX = max(maximX, summ - minX[ostX])
    maximY = max(maximY, summ - minY[ostY])

    minX[ostX] = min(summ, minX[ostX])
    minY[ostY] = min(summ, minY[ostY])

print(maximX, maximY, maximX + maximY)


#13-15
f = open('fileB__d8le.txt')
n = int(f.readline())

minX, minX[0] = [16e10]*99, 0
ind, ind[0] = [-1000]*99, -1
maxim, summ, dlina = 0, 0, 0

for i in range(n):
    x = int(f.readline())
    summ += x
    ost = summ % 99
    if summ - minX[ost] > maxim:
        maxim = summ - minX[ost]
        dlina = i - ind[ost]
    if summ < minX[ost]:
        minX[ost] = summ
        ind[ost] = i
print(dlina)


#16-17
f = open('fileA__d8ld.txt')
n = int(f.readline())

minX,minX[0] = [10e16]*67, 0
ind, ind[0] = [-1000]*67, -1

maxim, dlina, summ = 0, 0, 0

for i in range(n):
    x = int(f.readline())
    summ += x
    ost = summ % 67
    if summ - minX[ost] > maxim:
        maxim = summ - minX[ost]
        dlina = i - ind[ost]
    if summ < minX[ost]:
        minX[ost] = summ
        ind[ost] = i
print(maxim, dlina/3) #из условия dlina % 3, поэтому можно проверить этот факт через обычное деление
                      #в ответ нужно писать целое число 


#18
f = open('fileB__d8le.txt')
n = int(f.readline())

minX,minX[0] = [10e16]*133, 0
ind, ind[0] = [-1000]*133, -1

maxim, dlina, summ = 0, 0, 0

for i in range(n):
    x = int(f.readline())
    summ += x
    ost = summ % 133
    if summ - minX[ost] > maxim:
        maxim = summ - minX[ost]
        dlina = i - ind[ost]
    if summ < minX[ost]:
        minX[ost] = summ
        ind[ost] = i
print(maxim, dlina//7)


#19-21
f = open('fileA__d8ld.txt')
n = int(f.readline())

minX, minX[0] = [10e16]*100, 0
ind, ind[0] = [-1000]*100, -1

maxim, dlina, summ = 0, 0, 0

for i in range(n):
    x = int(f.readline())
    summ += x
    ost = summ % 100
    if summ - minX[ost] > maxim:
        maxim = summ - minX[ost]
        dlina = i - ind[ost]

    if summ < minX[ost]:
        minX[ost] = summ
        ind[ost] = i
print(maxim//dlina)


#22-24
f = open('fileB__d8le.txt')
n = int(f.readline())

minX, minX[0] = [10e16]*12345, 0
ind, ind[0] = [-10000]*12345, -1

maxim, dlina, summ = 0, 0, 0

for i in range(n):
    x = int(f.readline())
    summ += x
    ost = summ % 12345
    if summ - minX[ost] > maxim:
        maxim = summ - minX[ost]
        dlina = i - ind[ost]
    if summ < minX[ost]:
        minX[ost] = summ
        ind[ost] = i
if maxim == 0:
    print(-1)
else:
    print(maxim*dlina)


#25-27
f = open('fileB__d8le.txt')
n = int(f.readline())

minX, minY = [10e16] * 9, [10e16] * 8
indX, indY = [-100] * 9, [-100] * 8
minX[0], minY[0], indX[0], indY[0] = 0, 0, -1, -1

maximX, maximY, dlinaX, dlinaY, summ = 0, 0, 0, 0, 0

for i in range(n):
    x = int(f.readline())
    summ += x

    ost = summ % 9
    if summ - minX[ost] > maximX:
        maximX = summ - minX[ost]
        dlinaX = i - indX[ost]
    if summ < minX[ost]:
        minX[ost] = summ
        indX[ost] = i

    ost = summ % 8
    if summ - minY[ost] > maximY:
        maximY = summ - minY[ost]
        dlinaY = i - indY[ost]
    if summ < minY[ost]:
        minY[ost] = summ
        indY[ost] = i
print(abs(maximX - maximY) * abs(dlinaX - dlinaY))


#28-30
f = open('fileA__d8ld.txt')
n = int(f.readline())

maxPS,maxPS[0] = [-10e16]*777, 0
ind, ind[0] = [-1000]*777, -1
minim, dlina, summ = 10e16, 0, 0

for i in range(n):
    x = int(f.readline())
    summ += x
    ost = summ % 777
    if summ - maxPS[ost] < minim:
        minim = summ - maxPS[ost]
        dlina = i - ind[ost]
    if summ > maxPS[ost]:
        maxPS[ost] = summ
        ind[ost] = i
print(minim - dlina)


#1
f = open('fileB__d8le.txt')
n = int(f.readline())

minX, minX[0] = [10e16]*17, 0
minY, minY[0] = [10e16]*6, 0
maximX, maximY, dlinaX, dlinaY, summ = 0, 0, 0, 0, 0

for i in range(n):
    x = int(f.readline())
    summ += x

    ost = summ % 17
    if summ - minX[ost] > maximX:
        maximX = summ - minX[ost]
    if summ < minX[ost]:
        minX[ost] = summ

    ost = summ % 6
    if summ - minY[ost] > maximY:
        maximY = summ - minY[ost]
    if summ < minY[ost]:
        minY[ost] = summ
        
a = maximX + maximY + maximY + maximX




f = open('fileA__d8ld.txt')
n = int(f.readline())

minX, minX[0] = [10e16]*17, 0
minY, minY[0] = [10e16]*6, 0
maximX, maximY, dlinaX, dlinaY, summ = 0, 0, 0, 0, 0

for i in range(n):
    x = int(f.readline())
    summ += x

    ost = summ % 17
    if summ - minX[ost] > maximX:
        maximX = summ - minX[ost]
    if summ < minX[ost]:
        minX[ost] = summ

    ost = summ % 6
    if summ - minY[ost] > maximY:
        maximY = summ - minY[ost]
    if summ < minY[ost]:
        minY[ost] = summ
        
b = maximX + maximY + maximY + maximX
print(a+b)



#3
f = open('fileB__d8le.txt')
n = int(f.readline())

minPS, minPS[0] = [10e16]*17, 0
ind, ind[0] = [-1000]*17, -1
maxim, summ, dlina = -10e16, 0, 0

for i in range(n):
    x = int(f.readline())
    summ += -x
    ost = summ % 17
    if summ - minPS[ost] > maxim:
        maxim = summ - minPS[ost]
        dlina = i - ind[ost]
    if summ < minPS[ost]:
        minPS[ost] = summ
        ind[ost] = i
print(-maxim - dlina)
#16+16

m,pm,nkr = -10e16,-10e16,-10e16
f = open('Задание_27_B__d0r9__d95g.txt')
n = int(f.readline())
for i in range(n):
    x = int(f.readline())
    if x % 11 == 0:
        if x > m:
            pm = m
            m = x
        elif x > pm:
            pm = x
    else:
        if x > nkr:
            nkr = x
print(max(pm*m,m*nkr))
'''  # Цепочки
'''
#########################################################
            #1 ПРОТОТИП ЦЕПОЧИК
# макс сумму цепочки, кратную 10
f = open('123123')
n = int(f.readline())
a = [10e16]*10
a[0] = 0

s = 0
ans = -100000000000

for i in range(n):
    x = int(f.readline())
    s += x

    if s - a[s%10] > ans:
        ans = s - a[s%10]

    if s < a[s%10]:
        a[s%10] = s

print(ans)



f = open('fileB__d8le.txt')
n = int(f.readline())

minX,minX[0] = [10e16]*133, 0
ind, ind[0] = [-1000]*133, -1

maxim, dlina, summ = 0, 0, 0

for i in range(n):
    x = int(f.readline())
    summ += x
    ost = summ % 133
    if summ - minX[ost] > maxim:
        maxim = summ - minX[ost]
        dlina = i - ind[ost]
    if summ < minX[ost]:
        minX[ost] = summ
        ind[ost] = i
print(maxim, dlina//7)




#########################################################
            #2 ПРОТОТИП ДВЕ КУЧИ
#Две кучи

# СПОСОБ Jenius (оооочен долгий)
# бинарный поиск макс суммы через маску

# перебираем по маске (сначала 0,0,0 - 1,0,0 - 0,1,0 - 1,1,0 - 1,1,1 взависимо от длины и т.д.)
# все возможные варианты выбора чисел из двух кучек
# число слева загоняем в один массив, число справо в другой
# перебираем маску и получаем сумму, сравниваем с МАКС и получаем ответ
    # КАК ДВОИЧНАЯ СС и числа в ней
n = int(input())
a = []
b = []
ans = -10e16
for i in range(n):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)

for t in range(2**n): # n - длина
    mask = []
    x = t
    for j in range(n):
        mask.append(x%2)
        x = x//2

# если в маске 0, выбираем A
# если в маске 1, выбираем Б

    s = 0
    for j in range(n):
        if mask[j] == 0:
            s += a[j]
        else:
            s += b[j]

    if s % 2 == 0:
        if s > ans:
            ans = s
print(ans)



#СПОСОБ Noob
# нечетное - нечетное = четное
# ищем минимальную нечетную разность

n = int(input())
s = 0
md = 10e16
for i in range(n):
    x,y = map(int,input().split())
    s += max(x,y)
    diff = abs(x-y)
    if diff % 2 == 1:
        if diff < md:
            md = diff
if s % 2 == 0:
    print(s)
else:
    print(s - md)

# А ЕСЛИ МАКС СУММА КРАТНАЯ 10?????

# будем динамически заполнять МАГИЧЕСКИЙ массив

n = int(input())
a = [-10e16]*10
a[0] = 0 #кратная 10
for i in range(n):
    x,y = map(int,input().split())
    a_new = [-10e16]*10

    for j in range(10):
        ost = (a[j] + x) % 10
        if a[j] + x > a_new[ost]:
            a_new[ost] = a[j] + x

    for j in range(10):
        ost = (a[j] + y) % 10
        if a[j] + y > a_new[ost]:
            a_new[ost] = a[j] + y

    for j in range(10):
        a[j] = a_new[j]
print(a[0])




#########################################################
            # 3 ПРОТИП ПАРЫ ЧИСЕЛ
# дано n чисел, затем n чисел, найдите количество пар чисел, произведение которых делится на 6

# СТАТИКА

k6 = 0  # кратные 6
k3 = 0  # кратные 3, но НЕ кратные 6
k2 = 0  # кратные 2, но НЕ кратные 6
nk = 0  # некратные 6

n = int(input())
for i in range(n):
    x = int(input())
    if x % 6 == 0:
        k6 += 1
    elif x % 3 == 0:
        k3 += 1
    elif x % 2 == 0:
        k2 += 1
    else:
        nk += 1

ans = k6*(k3+k2+nk) + (k3*k2)


#ДИНАМИКА
k6 = 0  # кратные 6
k3 = 0  # кратные 3, но НЕ кратные 6
k2 = 0  # кратные 2, но НЕ кратные 6
nk = 0  # некратные 6

n = int(input())
for i in range(n):
    x = int(input())

    if x % 6 == 0:
        ans += nk + k2 + k3 + k6
        k6 += 1

    elif x % 3 == 0:
        ans += k2+k6
        k3 += 1

    elif x % 2 == 0:
        ans += k3 + k6
        k2 += 1

    else:
        ans += k6
        nk += 1

print(ans)


            # ЧИСЛА НА РАССТОЯНИИ (Царский сдвиг)

# дано число n, затем n чисел, найти количество пар чисел,
# произведение которых делится на 6, и находящихся на расстоянии хотяб 7
# образуется очередь чисел, которые не берутся в переборе пар, так как расстояние 7, то очередь будет равна 6
# например 1,   [2,3,4,5,6,7]    ,8     1 - 8 = 7

k6 = 0  # кратные 6
k3 = 0  # кратные 3, но НЕ кратные 6
k2 = 0  # кратные 2, но НЕ кратные 6
nk = 0  # некратные 6

ans = 0
n = int(input())

line = []
for i in range(6):
    line.append(int(input())) # считываем первые элементы в очередь

for i in range(6,n):
    x = int(input())

    if x % 6 == 0:
        ans += k6 + k3 + k2 + nk
    elif x % 3 == 0:
        ans += k6 + k2
    elif x % 2 == 0:
        ans += k6 + k3
    else:
        ans += nk


    if line[0] % 6 == 0:
        k6 += 1
    elif line[0] % 3 == 0:
        k3 += 1
    elif line[0] % 2 == 0:
        k2 += 1
    else:
        nk += 1

    for j in range(5):
        line[j] = line[j+1]
    line[5] = x

print(ans)
'''  # Базовые прототипы


# TIMER

def Dtimer(func):
    from datetime import datetime

    def wrapper():
        start = datetime.now()
        func()
        end = datetime.now()
        print(end - start)

    return wrapper


"""import random

#Дано число n затем n натуральных чисел.
#Требуется найти максимальное четное произведение среди пар чисел.

def no_eff(a):
    maxim = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if (a[i]*a[j] % 2 == 0) > maxim:
                maxim = a[i]*a[j]
    return maxim

def eff(a):
    ans = 0
    ch = 0
    nech = 0

    for i in range(len(a)):
        if a[i] % 2 == 0:
            ans = max(a[i]*ch, a[i]*nech, ans)
            ch = max(a[i], ch)
        else:
            ans = max(a[i] * ch, ans)
            nech = max(a[i], nech)

    return ans

for i in range(100):
    tests = []
    for i in range(random.randint(100, 1000)):
        tests.append(random.randint(1, 10000))
    a = list(set(tests))
    print(no_eff(a) == eff(a))"""  # DEBUG 1
"""#Дано число n затем n натуральных чисел.
#Требуется найти количество пар чисел, чья сумма кратна 8, а также элементы пары
#находятся на расстоянии 3 и более.

def no_eff(a):
    ans = [a[i]+a[j] for i in range(len(a)) for j in range(i+3, len(a)) \
           if (a[i]+a[j]) % 8 == 0]

    return len(ans)

def eff(a):
    ans = 0
    line = a[:3]
    count = [0]*8

    for i in range(3, len(a)):
        count[line[0]%8] += 1

        ans += count[(8 - a[i] % 8) % 8]

        for j in range(2):
            line[j] = line[j+1]
        line[2] = a[i]

    return ans

def generator():
    import random
    for i in range(100):
        tests = []
        for i in range(random.randint(100, 1000)):
            tests.append(random.randint(1, 10000))
        a = list(set(tests))
        if no_eff(a) != eff(a):
            print(a)
            return False
    return True

print(generator())"""  # DEBUG 2

# HARD 27
"""# Асимптотика
# y = x^2 + 3 - 5   >>> O(n^2)

# y = 10000*x       >>> O(10000n)

# 1
# Дано целое число n, затем последовательность из n натуральных чисел.
# Требуется найти максимальную сумму, состоящую из пар чисел, которая будет кратна 6

n = int(input())
a = []
summ = 0
for i in range(n):
    a += [int(input())]  # Аналог a.append
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] + a[j]) % 2 == 0:
            summ = max(summ, a[i] + a[j])
print(summ)

n = int(input())
summ = 0
max_kr2 = 0
max_nekr2 = 0
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        summ = max(summ, x + max_kr2)
        max_kr2 = max(x, max_kr2)
    else:
        summ = max(summ, x + max_nekr2)
        max_nekr2 = max(x, max_nekr2)
print(summ)





# 2
# Дано целое число n, затем последовательность из n натуральных чисел.
# Требуется найти максимальное произведение, состоящее из пары чисел, которое будет кратно 6

# Теория
# A*B % 6 == 0, когда
#   1) А - кратно 6,    B - кратно 6
#   2) А - кратно 6,    В - кратно 3, кратно 2, некратно
#   3) A - кратно 3,    B - кратно 2

    # CТАТИКА
n = int(input())
max_kr_6 = 0
pr_kr_6 = 0
kr_3 = 0
kr_2 = 0
nekr = 0
for i in range(n):
    x = int(input())
    if x % 6 == 0:
        if x > max_kr_6:
            pr_kr_6 = max_kr_6
            max_kr_6 = x
        else:
            pr_kr_6 = max(x, pr_kr_6)
    elif x % 3 == 0:
        kr_3 = max(x, kr_3)
    elif x % 2 == 0:
        kr_2 = max(kr_2, x)
    else:
        nekr = max(nekr, x)

print(max(max_kr_6 * pr_kr_6, max_kr_6 * kr_3, max_kr_6 * kr_2, max_kr_6 * nekr, kr_3 * kr_2))

    # ДИНАМИКА
n = int(input())
max_kr_6, kr_3, kr_2, nekr = 0, 0, 0, 0
ans = 0

for i in range(n):
    x = int(input())
    if x % 6 == 0:
        ans = max(ans, x * max_kr_6, x * kr_3, x * kr_2, x * nekr)
        max_kr_6 = max(x, max_kr_6)
    elif x % 3 == 0:
        ans = max(ans, max_kr_6 * x, x * kr_2)
        kr_3 = max(x, kr_3)
    elif x % 2 == 0:
        ans = max(ans, max_kr_6 * x, x * kr_3)
        kr_2 = max(x, kr_2)
    else:
        ans = max(ans, x * max_kr_6)
        nekr = max(x, nekr)

print(ans)





# 3
# Дано целое число n, затем последовательность из n натуральных чисел.
# Требуется найти количество пар, произведение которых будет кратно 6

    # СТАТИКА
n = int(input())
ans = 0

kr_6 = 0
kr_3 = 0
kr_2 = 0
nekr = 0

for i in range(n):
    x = int(input())
    if x % 6 == 0:
        kr_6 += 1
    elif x % 3 == 0:
        kr_3 += 1
    elif x % 2 == 0:
        kr_2 += 1
    else:
        nekr += 1

# Распределили числа по кратности, теперь сложим их количество
# Исходя из задания #2, чтобы получить произведение пар кратных 6,
# нужно, чтоб либо оба числа были кратные 6, либо первое число кратное 6, а второе кратное 3 или 2 или некратное (но не кратное 6),
# либо первое число кратно 2, а второе кратно 3 (тогда при умножении их произведение будет кратно 6)

# Шестерка с сама собой - полный граф a(a-1)//2! # Число на которе делим - количество чисел (в данном задании у нас пара, т.е. два числа)
ans += kr_6 * (kr_6 - 1) // 2 + kr_6 * (kr_3 + kr_2 + nekr) + kr_3 * kr_2
print(ans)

    # ДИНАМИКА
# Если число кратно 6, то его можно умножить на ВСЕ числа некратные 6 (кр3, кр2, некр)
# поэтому мы динамически будем добавлять в ответ количество подходящих чисел
# если x % 6 == 0 тогда к ans += k3 + k2 + nekr (см. ниже код) и т.д. с другими кратностями

n = int(input())
kr_6, kr_3, kr_2, nekr, ans = 0, 0, 0, 0, 0

for i in range(n):
    x = int(input())
    if x % 6 == 0:
        ans += kr_6 + kr_3 + kr_2 + nekr
        kr_6 += 1
    elif x % 3 == 0:
        ans += kr_6 + kr_2
        kr_3 += 1
    elif x % 2 == 0:
        ans += kr_6 + kr_3
        kr_2 += 1
    else:
        ans += kr_6
        nekr += 1
print(ans)





# 4
# Дано целое число n, затем последовательность из n натуральных чисел.
# Требуется найти максимальную сумму, среди пар чисел, которая будет кратно 10

# Есть ТРИ случая:
#   1) Берем в пару  MAX % 10 == 0   +   predMAX % 10 == 0
#   2) Берем в пару  MAX % 10 == 5   +   predMAX % 10 == 5
#   3) Берем в пару числа с взаимодополняющим отстаком при делении на 10

# Взаимодополняющий остаток:
# A, B = 17, 13
# 17 % 10 == 7 и 13 % 10 == 3, следовательно
# (a+b) % 10 == 0

    # СТАТИКА
n = int(input())

# Чтобы хранить взаимодополняющие остатки, заведем ДВА массива:
MAX = [0] * 10  # Массив МАКСимальных чисел при каком-то остатке (MAX[0] - максимальное число кратное 10)
predMAX = [0] * 10  # Массив ПРЕДМАКСимальных чисел (predMAX[0] - предмаксимальное число кратное 10)

for i in range(n):
    x = int(input())

    if x % 10 == 0:
        if x > MAX[0]:
            predMAX[0] = MAX[0]
            MAX[0] = x
        else:
            predMAX[0] = max(predMAX[0], x)

    elif x % 10 == 5:
        if x > MAX[5]:
            predMAX[5] = MAX[5]
            MAX[5] = x
        else:
            predMAX[5] = max(predMAX[5], x)

    else:
        a[x % 10] = max(a[x % 10], x)

# Сравниваем максимальные суммы
ans = max(predMAX[0] + MAX[0], predMAX[5] + MAX[5])
for i in range(1, 4):  # Чтобы не перебирать [0] и [5] элементы массива
    ans = max(ans, MAX[i] + MAX[
        10 - i])  # Пофакту, мы могли не создавать второй массив с предМАКС, так как взаимодополняющие берутся из МАКС массива
print(ans)

    # ДИНАМИКА
# На каждом шаге считываем макс сумму с максимальным взаимодополняющим числом по остатку
# Не забываем обновлять массив

n = int(input())
MAX = [0] * 10
ans = 0
for i in range(n):
    x = int(input())
    ans = max(ans, MAX[(10 - (x % 10)) % 10] + x)
    a[x % 10] = max(a[x % 10], x)
print(ans)





# 5
# Дано целое число n, затем последовательность из n натуральных чисел.
# Требуется найти количество пар чисел, сумма которых будет кратна 91

# Так же как и в прошлой задачи будут 2 случая (т.к. 91 нечетное, то 3 не будет)

# СТАТИКА
n = int(input())
a = [0] * 91
ans = 0

for i in range(n):
    x = int(input())
    a[x % 91] += 1

# После считывания количества чисел с определенными остатками в массив
# Мы через комбу складываем количество чисел % 91
# А дальше, через взаимодополняющие досчитываем оставшиеся пары

ans = a[0] * (a[0] - 1) // 2
for i in range(1, 46):
    ans += a[i] * a[91 - i]
print(ans)

# ДИНАМИКА
n = int(input())
a = [0] * 91
ans = 0

for i in range(n):
    x = int(input())
    ans += a[(91 - x % 91) % 91]
    a[x % 91] += 1
print(ans)





# 6
# Дано целое число n, затем последовательность из n натуральных чисел.
# Требуется найти количество пар чисел, сумма которых будет кратна 8, произведение кратно 7

# В задаче 2 условия, начнем решать с самого простого - произведение
    # СТАТИКА
n = int(input())
# Создадим 2 массива:
kr_7 = [0] * 8  # Взаимодополняющие числа кратные 7
nekr = [0] * 8  # Взаимодополняющие числа НЕкратные 7

for i in range(n):
    x = int(input())
    if x % 7 == 0:
        kr_7[x % 8] += 1
    else:
        nekr[x % 8] += 1

# То же самое, полностью также как и в прошлых задачах на поиск количества пар
# Не забываем про [4], так как при сложении чисел с остатком 4 получится число кратное 8
ans = kr_7[0] * (kr_7[0] - 1)//2 + \
      kr_7[4] * (kr_7[4] - 1)//2 + \
      kr_7[0] * nekr[0] + \
      kr_7[4] * nekr[4]

for i in range(8):
    # Умножаем количество чисел с одним остатком на количество чисел с противоположным остатком (взаимодополняющим)
    ans += (kr_7[i] * kr_7[8-i]) // 2 + \
           (kr_7[i] * nekr[8-i])
print(ans)

    # ДИНАМИКА
n = int(input())
kr_7 = [0]*8
nekr = [0]*8
ans = 0

for i in range(n):
    x = int(input())
    if x % 7 == 0:
        ans += kr_7[(8-x % 8) % 8] + nekr[(8-x % 8) % 8]
        kr_7[x % 8] += 1
    else:
        ans += kr_7[(8-x % 8) % 8]
        nekr[x % 8] += 1
print(ans)





# 7
# Дано целое число n, затем последовательность из n натуральных чисел.
# Требуется найти количество пар чисел, сумма которых будет кратна 5, произведение кратно 21.
# Обязательно хотя бы одно из чисел должно быть больше 40

n = int(input())
# Первый индекс - больше или меньше 40. 1 >40, а 0 <=40
# Второй индекс - кр. 21, 7, 3, некр (то есть индексы 0, 1, 2, 3)
# Третий индекс - остаток при делении на 5
a = [[[0 for i in range(5)] for j in range(4)] for k in range(2)]

ans = 0

for i in range(n):
    x = int(input())
    t = (5 - x % 5) % 5
    if x % 21 == 0:
        for j in range(4):
            ans += a[1][j][t] + a[0][j][t] * (x > 40)
        a[x > 40][0][x % 5] += 1

    elif x % 7 == 0:
        for j in range(0, 4, 2):
            ans += a[1][j][t] + a[0][j][t] * (x > 40)
        a[x > 40][1][x % 5] += 1

    elif x % 3 == 0:
        for j in range(2):
            ans += a[1][j][t] + a[0][j][t] * (x > 40)
        a[x > 40][2][x % 5] += 1

    else:
        ans += a[1][0][t] + a[0][0][t] * (x > 40)
        a[x > 40][3][x % 5] += 1

print(ans)

#Отказ от ИВ
#Первый индекс - больше или меньше 40. 1 - >40, а 0 <= 40
#Второй индекс - кр. 21, 7, 3, некр (то есть индексы 0, 1, 2, 3)
#Третий индекс - остаток при делении на 5
a = [[[0 for i in range(5)] for j in range(4)] for k in range(2)]

ans = 0

for i in range(n):
    x = int(input())

    k = 3-((x%3 == 0)*1+(x%7 == 0)*2)

    for j in range(4):
        if k == 0:
            ans += a[1][j][(5-x%5)%5] + a[0][j][(5-x%5)%5]*(x > 40)
        elif k == 1:
            ans += (a[1][j][(5 - x % 5) % 5] + a[0][j][(5 - x % 5) % 5] * (x > 40)) * (j == 0 or j == 2)
        elif k == 2:
            ans += (a[1][j][(5 - x % 5) % 5] + a[0][j][(5 - x % 5) % 5] * (x > 40)) * (j == 0 or j == 1)
        else:
            ans += (a[1][j][(5 - x % 5) % 5] + a[0][j][(5 - x % 5) % 5] * (x > 40)) * (j == 0)

    a[x > 40][k][x%5] += 1

print(ans)"""  # ПАРЫ ЧИСЕЛ
'''
# Расстояние - разность индексов

# 1
# Дано целое число n затем последовательность из n натуральных чисел. Требуется найти
# количество пар, которые кратны 10, где расстояние между элементами пары хотяб 3

n = int(input())
line = []
a = [0]*8
ans = 0
for i in range(3):
    line.append(int(input()))
for i in range(3, n):
    #1й блок: Отправляем на свалку
    #Самый крайний элемент, с которым х может взаимодействовать
    a[line[0] % 8] += 1
    #2й блок: Взаимодействие всех подходящих с х
    x = int(input())
    ans += a[(8 - x%8)%8]
    #3й блок: Сдвиг очереди
    for j in range(3-1):
        line[j] = line[j+1]
    line[2] = x
print(ans)







# 2
# Дано целое число n затем последовательность из n натуральных чисел. Требуется найти
# максимальную сумму среди пар, кратную 10, где расстояние между элементами пары хотяб 5

n = int(input())
ans = 0
a = [0]*10
line = []

for i in range(5):
    line += [int(input())]
    
for i in range(5,n):
    a[line[0] % 10] = max([line[0] % 10], line[0])  # Сравниваем, так как нужна МАКС сумма
    
    x = int(input())
    ans = max(ans, x + a[(10 - x % 10) % 10]) # X + Число с взаим. доп. отстатком
                        # Еще раз делим на 10, чтоб не получилось a[10] 
    for j in range(5-1):
        line[j] = line[j+1]
    line[4] = x
    
print(ans)







# 3
# Дано целое число n затем последовательность из n натуральных чисел. Требуется найти
# количество пар чисел, чье произведение будет кратно 22, при этом расстояние
# между элементами пары хотяб 7, а один из элементов пары не меньше 55


# Двумерный массив
    # Первый индекс - ОТКАЗ ОТ ИВ
        # 0 - < 55
        # 1 - >= 55

    # Второй индекс
        # 0 - % 22
        # 1 - % 11
        # 2 - только % 2
        # 3 - некратные ничему


svalka = [[0 for i in range(4)] for j in range(2)]

n = int(input())
ans = 0
line = []

for i in range(7):
    line.append(int(input()))

for i in range(7,n):
    if line[0] % 22 == 0:
        svalka[line[0] >= 55][0] += 1

    elif line[0] % 11 == 0:
        svalka[line[0] >= 55][1] += 1

    elif line[0] % 2 == 0:
        svalka[line[0] >= 55][2] += 1

    else:
        svalka[line[0] >= 55][3] += 1

    x = int(input())
    
    # ВСПОМИНАЕМ!!!     ( A*B % 22 == 0 ) 

    # 22 можно взять со всеми кратностями (0,1,2,3 индексы)
    # 11 можно взять с 22 и 2 (0,2 индексы)
    # 2 можно взять с 22 и 11 (0,1 индексы)
    # некр можно взять только с 22 (0 индекс)
    
    if x % 22 == 0:
        for j in range(4):
            ans += svalka[0][j] * (x >= 55) + svalka[1][j]
            
    elif x % 11 == 0:
        for j in range(0, 4, 2):
            ans += svalka[0][j] * (x >= 55) + svalka[1][j]
            
    elif x % 2 == 0:
        for j in range(0, 2):
            ans += svalka[0][j] * (x >= 55) + svalka[1][j]
    else:
        ans += svalka[0][0] * (x >= 55) + svalka[1][0]
        
    for j in range(7-1):
        line[j] = line[j+1]
    line[6] = x 
print(ans)






# 3 с отказом от ИВ

svalka = [[0 for i in range(4)] for j in range(2)]

n = int(input())
ans = 0
line = []

for i in range(7):
    line.append(int(input()))

for i in range(7,n):
    # Отказ от проверки кратности (- 15 строчек)
    x = int(input())
    tmp = 3 - ((x % 11 == 0) * 2 + (x % 2 == 0)) 
    svalka[line[0] >= 55][tmp] += 1
    

    if x % 22 == 0:
        for j in range(4):
            ans += svalka[0][j] * (x >= 55) + svalka[1][j]
    
    elif x % 11 == 0:
        for j in range(0, 4, 2):
            ans += svalka[0][j] * (x >= 55) + svalka[1][j]
    
    elif x % 2 == 0:
        for j in range(0, 2):
            ans += svalka[0][j] * (x >= 55) + svalka[1][j]
    else:
        ans += svalka[0][0] * (x >= 55) + svalka[1][0]
    
    for j in range(7 - 1):
        line[j] = line[j + 1]
    line[6] = x
print(ans)







# 4 
# Дано целое число n затем последовательность из n натуральных чисел. Требуется найти
# минимальную разность между парамы чисел, кратную 45, при этом расстояние 
# между элементами пары хотяб 9, а один из элементов пары не больше 20 (<= 20)

# (A - B) % 45 == 0, если
    # A % 45 == 0
    # B % 45 == 0

n = int(input())
ans = 0
line = []

a = [[0 for i in range(45)] for j in range(2)] # Максимальные числа
b = [[10e16 for k in range(45)] for m in range(2)] # Минимальные числа

for i in range(9):
    line.append(int(input()))
    
for i in range(9, n):
    # Отправляем на свалки МАКСов и МИНов
    a[line[0] <= 20][line[0] % 45] = max(a[line[0] <= 20][line[0] % 45], line[0])
    b[line[0] <= 20][line[0] % 45] = min(b[line[0] <= 20][line[0] % 45], line[0])
    
    x = int(input())
    if x <= 20:
        
        #####
        ##### Ждем конспект
        #####
    
    else:
        
        #####
        ##### Ждем конспект
        #####
        
    for j in range(9-1):
        line[j] = line[j+1]
    line[8] = x
print(ans)          
'''  # ОЧЕРЕДИ
'''
# ???!!!>>> ЦАРСКИЙ СДВИГ <<<!!!???

# Дано число n и последовательность из n натуральных чисел. Требуется найти 
# количество пар чисел, чья сумма будет четна. 
# Парой являются два числа на расстоянии 3 (разница индексов 3 и более)

n = int(input())
ans = 0
a = [0] * 2
line = []
for i in range(2): # Делаем на 1 меньше очередь (из-за разницы)
    line += [int(input())]

for i in range(2, n):
    x = int(input()) 
    ans += a[x % 2]
        # На свалку
    a[line[i % 2] % 2] += 1
        # Царский сдвиг очереди 
    line[i % 2] = x # X уходит на место числа с индексом ТАКОЙ ЖЕ КРАТНОСТИ
print(ans)






# Дано число n и последовательность из n натуральных чисел. Требуется найти 
# количество пар чисел, чья сумма будет кратна 6, произведение кратно 5, 
# а одно из чисел обязательно должно быть больше 20 (СТРОГО). Расстояние 5

# ТРЕХМЕРНЫЙ МАССИВ
    # 1 индекс - больше, меньше
    # 2 индекс - кратность, некратность 5
    # 3 индекс - остаток от 6

a = [[[0 for i in range(6)] for j in range(2)] for k in range(2)]

n = int(input())
line = []

for i in range(4):
    line += [int(input())]

for i in range(4,n):
    x = int(input())
    dop = (6 - x % 6) % 6
    # Чисто комба
    ans += a[0][1][dop]*(x < 20) + a[1][1][dop] + (a[0][0][dop]*(x < 20) + a[1][0][dop])*(x % 5 == 0)
    a[line[i % 6] > 20][1 - (line[i % 6] % 5 == 0)][line[i % 6] % 6] += 1
    # Самое сложное - царский сдвиг
    line[i % 5] = x
print(ans)
'''  # Царский сдвиг

"""# 28 = 14*2 = 4*7

# Макс и предмакс некратные ничему. То есть произведение таких двух чисел ТОЧНО некратно 28.

# Макс. кратный 14, макс. кратный 7, макс. кратный 4, макс кратный 2.

# 1) Макс * предмакс (некратные ничему)
# 2) Макс (некратный ничему) * любой оставшийся Макс
# 3) Макс_14*Макс_7, Макс_4*Макс_2, Макс_7*Макс_2
# 4) Также рассматриваются произведения вида:
#   Макс_7 * пр_Макс_7, Макс_4 * пр_Макс_4, Макс_2 * пр_Макс_2 и т.д.

n = int(input())

nekr, pr_nekr = 0, 0
kr_14 = 0
kr_7, pr_7 = 0, 0
kr_4, pr_4 = 0, 0
kr_2, pr_2 = 0, 0

# 14 = 7 * 2
# a*14 * b*14 = a * 7 * 2 * b * 7 * 2 = a * b * 7 * 4 * 7 = a*b * 28 * 7

for i in range(n):
    x = int(input())

    if x % 28 != 0:

        if x % 14 == 0:
            kr_14 = max(kr_14, x)

        elif x % 7 == 0:
            if x >= kr_7:
                pr_7 = kr_7
                kr_7 = x
            elif x >= pr_7:
                pr_7 = x

        elif x % 4 == 0:
            if x >= kr_4:
                pr_4 = kr_4
                kr_4 = x
            elif x >= pr_4:
                pr_4 = x

        elif x % 2 == 0:
            if x >= kr_2:
                pr_2 = kr_2
                kr_2 = x
            elif x >= pr_2:
                pr_2 = x

        else:
            if x >= nekr:
                pr_nekr = nekr
                nekr = x
            elif x >= pr_nekr:
                pr_nekr = x

print(max(nekr*pr_nekr,\
          nekr*kr_14, nekr*kr_7, nekr*kr_4, nekr*kr_2, \
          kr_14*kr_7, kr_4*kr_2, kr_7*kr_2, \
          kr_7*pr_7, kr_4*pr_4, kr_2*pr_2))
"""  # Макс. и некратное 28.
"""n = int(input())
m7 = [0] * 160 # m7[31] максимальный элемент на свалке, который ДЕЛИТСЯ на 7 и НЕ ИМЕЕТ остаток 31 от деления на 160
m = [0] * 160
ans = 0
for i in range(n):
    x = int(input())
    t = x % 160
    if x % 7 == 0:
        ans = max(ans, x + m7[t], x + m[t])
        for j in range(160): # перезаписываем
            if x > m7[j] and j != t:
                m7[j] = x

    if x % 7 != 0:
        ans = max(ans, x + m7[t])
        for j in range(160):
            if x > m[j] and j != t:
                m[j] = x

print(ans)"""  # Найти макс сумму пары, у котороых различные остатки от деления на 160 и хотяб 1 число делится на 7
"""chet = 0 
nechet = 0
ans = 0
n = 25
for i in range(n):
    x = int(input())
    if x % 2 == 0:
        ans += chet + nechet
        chet += 1
    if x % 2 != 0:
        ans += chet
        nechet += 1
print(ans)"""  # Типичная динамика >> поиск пар, произведение которых четно
"""# 8 = 2*4 или 8*1
n = 25

kr2 = 0
kr4 = 0
kr8 = 0
nekr = 0
ans = 0

line = []
for i in range(8):
    line.append(int(input()))

for i in range(8, n):
    if line[0] % 8 == 0:
        kr8 += 1
    elif line[0] % 4 == 0:
        kr4 += 1
    elif line[0] % 2 == 0:
        kr2 += 1
    else:
        nekr += 1

    x = int(input())
    if x % 8 == 0:
        ans += kr8 + kr4 + kr2 + nekr
    elif x % 4 == 0:
        ans += kr8 + kr4 + kr2   #   28 * 4 = 112   >>>  (28 % 8 != 0 and 4 % 8 != 0)    А вот 112 делится на 8, но почему ???
                                  #   Так как по ОТА >>> 4 = 2*2, 28 = 2*2*7, 8 = 2*2*2 = 2**3    =>    (2**4 * 7) % (2**3) == 0 !!!!!
                                  #   Значит произведение чисел, которые делятся на 4, делится на 8
    elif x % 2 == 0:
        ans += kr8 + kr4
    else:
        ans += kr8

    for j in range(7):
        line[j] = line[j + 1]
    line[7] = x
print(ans)"""  # Кол-во пар, a*b % 8 == 0 и расстояние >= 8. ТЕОРИЯ ВНУТРИ !!!
"""# 26 = 26*1, 13*2
f = open('27988_B.txt')
n = int(f.readline())

kr26 = 0
prkr26 = 0
kr13 = 0
kr2 = 0
nekr = 0

for i in range(n):
    x = int(f.readline())
    if x % 26 == 0:
        if x > kr26:
            prkr26 = kr26
            kr26 = x
        elif x > prkr26:
            prkr26 = x

    elif x % 13 == 0:
        kr13 = max(kr13, x)

    elif x % 2 == 0:
        kr2 = max(kr2, x)

    else:
        nekr = max(nekr, x)
print(max(kr26 * prkr26, kr26 * kr13, kr26 * kr2, kr26 * nekr, kr13*kr2))
# 783900 988000"""  # R - произведение двух чисел. Найти МАКС R % 26 == 0
"""n = int(input())

kr_10 = [0] * 15
kr_5 = [0] * 15
kr_2 = [0] * 15
nekr = [0] * 15

ans = 0

for i in range(n):
    x = int(input())
    ost = (15 - x % 15) % 15

    ans += kr_10[ost] + (x % 10 == 0) * (nekr[ost]) + (x % 5 == 0) * (kr_2[ost]) + (x % 2 == 0) * (kr_5[ost])

    if x % 10 == 0:
        kr_10[x % 15] += 1

    elif x % 5 == 0:
        kr_5[x % 15] += 1

    elif x % 2 == 0:
        kr_2[x % 15] += 1

    else:
        nekr[x % 15] += 1
print(ans)"""  # Дано число натуральное n затем n натуральных чисел. Требуется найти количество пар чисел, сумма кратна 15, а произведение кратно 10.
"""n = int(input())

b_55 = [[0]*10 for i in range(4)]
m_55 = [[0]*10 for i in range(4)]

line = []

ans = 0

for i in range(4):
    line.append(int(input()))

for i in range(4, n):
    x = int(input())

    if line[0] >= 55:
        b_55[3-((line[0]%2 == 0) + (line[0] % 11 == 0)*2)][line[0] % 10] += 1
    else:
        m_55[3-((line[0]%2 == 0) + (line[0] % 11 == 0)*2)][line[0] % 10] += 1

    ost = (10 - x % 10) % 10
    if x >= 55:
        ans += b_55[0][ost] + (x % 22 == 0) * (b_55[3][ost]) +\
               (x % 11 == 0) * (b_55[2][ost]) + (x % 2 == 0) * (b_55[1][ost]) + \
                \
               m_55[0][ost] + (x % 22 == 0) * (m_55[3][ost]) + \
               (x % 11 == 0) * (m_55[2][ost]) + (x % 2 == 0) * (m_55[1][ost])

    else:
        ans += b_55[0][ost] + (x % 22 == 0) * (b_55[3][ost]) + \
               (x % 11 == 0) * (b_55[2][ost]) + (x % 2 == 0) * (b_55[1][ost])

    for j in range(4-1):
        line[j] = line[j+1]
    line[3] = x

print(ans)
"""  # Найти количество пар чисел, которые находятся на расстоянии >= 4, сумма кратна 10, произведение кратно 22, а один из элементов больше или равен 55.
"""f = open('27985_B.txt')
n = int(f.readline())

kr14 = 0
pr14 = 0
kr7 = 0
kr2 = 0
nekr = 0

ans = 0
for i in range(n):
    x = int(f.readline())
    if x % 14 == 0:
        if x > kr14:
            pr14 = kr14
            kr14 = x
    elif x % 7 == 0:
        kr7 = max(kr7, x)
    elif x % 2 == 0:
        kr2 = max(kr2, x)
    else:
        nekr = max(nekr, x)

print(max(kr14*pr14, kr14*kr7, kr14*kr2, kr14*nekr, kr7*kr2))"""  # Макс. Два числа % 14
"""f = open('28130_B.txt')
n = int(f.readline())
b80 = [0]*80
m80 = [0]*80

ans = 0
for i in range(n):
    x = int(f.readline())
    if x > 50:
        ost = x % 80
        ans += b80[(80 - ost)%80] + m80[(80 - ost)%80]
        b80[ost] += 1
    else:
        ost = x % 80
        ans += b80[(80 - ost) % 80]
        m80[ost] += 1

print(ans)"""  # Количество. Два числа сумма % 80, хотяб одно > 50
"""
f = open('27__9p3l.txt')
ans = 0
kr2 = 0
kr14 = 0
n = int(f.readline())

for i in range(n):
    x = int(f.readline())

    if x % 14 == 0:
        ans = max(ans, kr14 + x, x + kr2)
        kr14 = max(kr14, x)
    elif x % 2 == 0:
        ans = max(ans, kr14 + x)
        kr2 = max(kr2, x)

print(ans)
"""  # Хотяб 1 число % 14, их сумма МАКС,а разность четная
"""f = open('28129_A.txt')
n = int(f.readline())

max7, prmax7 = 0, 0
ost = 0
max0 = 0

for i in range(n):
    x = int(f.readline())
    if x % 7 == 0:
        if x > max7:
            prmax7 = max7
            max7 = x
            ost = x % 160
        elif x > prmax7:
            if ost != x % 160:
                prmax7 = x
    else:
        if x > max0:
            if ost != x % 160:
                max0 = x


a = max7+prmax7
b = max7+max0
if a > b:
    print(max7, prmax7)
else:
    print(max7, max0)"""  # Различные остатки от деления на d=160 и хотя бы одно из чисел делится на p=7. найти и вывести пару с макс суммой



'''
# 1
# Дано число n, затем n строк, в каждой по паре натуральных различных чисел.
# Из каждой пары берется одно число так, чтобы итоговая сумма всех таких чисел
# Была некратна 10 и была макс

n = int(input())
ans = 0
diff = 10e16

for i in range(n):
    a, b = map(int,input().split())
    ans += max(a,b)
    if abs(a-b) % 10 != 0:
        diff = min(diff, abs(a-b))

print(ans - diff*(ans % 10 == 0))
# или
if ans % 10 != 0:
    print(ans)
else:
    print(ans - diff)


# 2
# Мин. сумма

n = int(input())
ans = 0
diff = 10e16

for i in range(n):
    a, b = map(int,input().split())
    ans += min(a,b)
    if abs(a-b) % 10 != 0:
        diff = min(diff, abs(a-b))

print(ans + diff*(ans % 10 == 0))





# 3
# Дано число n, затем n строк, в каждой по паре натуральных различных чисел.
# Из каждой пары берется одно число так, чтобы итоговая сумма всех таких чисел
# Была кратна 2 и была макс

    # Сумма
# (A + B) % 3 == 0
    # A % 3 == P
    # B = (3 - P) % 3
# 4(1) + 8(2) = 12(0)

    # Разность
# (A - B) % 3 == 0
    # A % 3 == B % 3 - Сравнимы по модулю 3
# 10(1)-4(1) = 6(0)

n = int(input())
ans = 0
diff = 10e16

for i in range(n):
    a = [int(i) for i in input().split()]
    ans += max(a)

    if abs(a[0] - a[1]) % 2 == 1:
        diff = min(diff, abs(a[0] - a[1]))

print(ans - diff * (ans % 2 == 1))

# s(1) = diff(1) = ans(0)






# 4
# Дано число n, затем n строк, в каждой по паре натуральных различных чисел.
# Из каждой пары берется одно число так, чтобы итоговая сумма всех таких чисел
# Была кратна 3 и была мин

# S(2) - minDIFF(2) = ans(0)
# S(2) - minDIFF(1) - PREminDIFF(1) = ans(0)

n = int(input())
ans = 0
# ИНД 0 и 1 отвечают за мин дифы с отс. 1
# 2 и 3 за мин дифы с ост. 2
diff = [10e16] * 4

for i in range(n):
    a, b = map(int,input().split())
    ans += min(a,b)
    tmp = abs(a-b)
    if abs(a-b) % 3 == 1:
        if tmp < diff[0]:
            diff[1], diff[0] = diff[0], tmp
        else:
            diff[1] = min(diff[1], tmp)
    if abs(a-b) % 3 == 2:
        if tmp < diff[2]:
            diff[3], diff[2] = diff[2], tmp
        else:
            diff[3] = min(diff[3], tmp)

if ans % 3 == 0:
    print(ans)
elif ans % 3 == 1:
    print(ans + min(diff[2], diff[0]+diff[1]))
else:
    print(ans + min(diff[0], diff[2]+diff[3]))






# 5
# Дано число n, затем n строк, в каждой по ТРОЙКЕ натуральных различных чисел.
# Из каждой пары берется одно число так, чтобы итоговая сумма всех таких чисел
# Была кратна 10 и была макс

n = int(input())
ans = [0] * 10  # Массив всех макс. сумм, которые имеют опр. ост. при дел. на 10
for i in range(n):
    a, b = map(int, input().split())
    ans_new = [-1000000000] * 10

    for j in range(10):  # Блок подсчета всех сумм, путем прибавления числа a
        ost = (ans[j] + a) % 10
        if ans[j] + a > ans_new[ost]:
            ans_new[ost] = ans[j] + a

    for j in range(10):  # Блок подсчета всех сумм, путем прибавления числа b
        ost = (ans[j] + b) % 10
        if ans[j] + b > ans_new[ost]:
            ans_new[ost] = ans[j] + b

    # ans -> адрес массива ans_new. То есть ans просто указывает на местоположение элементов массива ans_new.
    # ТО есть при замене элементов ans_new массив ans также изменится.
    ans = ans_new  # Обновление всех макс. сумм, имеющих опр. ост. при дел. на 10

print(ans[0])






# 6
# Дано число n, затем n строк, в каждой по ТРОЙКЕ натуральных различных чисел.
# Из каждой ТРОЙКИ берется одно число так, чтобы итоговая сумма всех таких чисел
# Была кратна 8 и была мин

n = int(input())
ans = [0]*8
for i in range(n):
    a = [int(j) for j in input().split()]
    ans_new = [10e16]*8
    for k in range(3):
        for j in range(8):
            ost = (a[k] + ans[j]) % 8
            ans_new[ost] = min(ans_new[ost], a[k] + ans[j])
    ans = ans_new
print(ans[0])






# 7
# Дано число n, затем n строк, в каждой по ТРОЙКЕ натуральных различных чисел.
# Найдите три суммы таких, чтобы МИН была нечетная, а МАКС четная и была типа МИДЛ еще
# Каждое число обязательно прибавляется в одну из сумм и только одно

########################################
#######################################
# ЖДЕМ КОНСПЕКТ
#######################################
######################################
'''  # Две кучи

"""
n = 25
ans = 0
diff = 10e16
for i in range(n):
    x, y = [int(j) for j in input().split()]
    ans += max(x, y)
    #diff = min(diff, abs(x - y) + 10e16 * (abs(x - y) % 2 == 0)) 
    # но лучше сделать по человечески >>>
    tmp = abs(x - y)
    if tmp % 2 != 0 and tmp < diff:
        diff = tmp
if ans % 2 != 0:
    print(ans)
else:
    print(ans - diff)
"""  # Две кучи - сумма НЕ ДЕЛИЛАСЬ на 2 (просто вычитаем diff % 2 != 0 из S если S % 2 == 0)
"""n = 26
s = [-100000] * 16
s[0] = 0
for i in range(n):
    x, y = map(int, input().split())
    new_s = [-100000] * 16

    for j in range(16):
        ost = (s[j] + x) % 16
        if s[j] + x > new_s[ost]:
            new_s[ost] = s[j] + x

    for j in range(16):
        ost = (s[j] + y) % 16
        if s[j] + y > new_s[ost]:
            new_s[ost] = s[j] + y

    for j in range(16):
        s[j] = new_s[j]
print(s[0])"""  # Две кучи - сумма делилась на 16 (через новый массивчик и перебор значений и сравнение с прошлым массивом)
'''
n = int(input())
ans = 0 
diff = 100000000
for i in range(n):
    a, b = map(int, input().split())
    #a = [int(i) for i in input().split()]
    ans += max(a,b)   
    if abs(a-b) % 100 != 0:
        diff = min(diff, abs(a-b))      
if ans % 100 == 0:
    print(ans - diff)
else:
    print(ans)
'''  # Дано нат. число n, затем n пар натуральных чисел. Найти сумму, некратную чему-либо. макс. сумму, некратную 100. Из каждой пары берется одно число.
'''
n = int(input())
ans = [0]*10
for i in range(n):
    a = [int(i) for i in input().split()]
    ans_new = [-100000000]*10
    for j in range(2):
        for t in range(10):
            ans_new[(a[j] + ans[t]) % 10] = max(ans_new[(a[j] + ans[t]) % 10], a[j] + ans[t])
    ans = ans_new
print(ans)
'''  # Из каждой пары берется одно число. Требуется найти макс. сумму, кратную 10.
"""n = int(input())
s = [-1000000000000000]*70

s[0] = 0

for i in range(n):
    a, b, c = [int(i) for i in input().split()]
    x, y, z = a+b, b+c, a+c
    s_new = [-1000000000000000]*70

    for j in range(70):
        ost = (s[j] + x) % 70
        s_new[ost] = max(s_new[ost], s[j] + x)
    for j in range(70):
        ost = (s[j] + y) % 70
        s_new[ost] = max(s_new[ost], s[j] + y)
    for j in range(70):
        ost = (s[j] + z) % 70
        s_new[ost] = max(s_new[ost], s[j] + z)
    s = s_new[:]

print(max(s[3], s[10], s[17], s[24], s[31], s[38], s[52], s[59], s[66], s[5], s[15], s[25], s[35], s[55], s[65]))
"""  # Тройки чисел: из каждой ровно 2 числа, чтобы МАКС сумма оканчивалась либо на 3 % 7, либо на 5 % 10, но НЕ ОКАНЧИВАЛАСЬ ОДНОВРЕМЕННО
"""data = open("27-B.txt", "r").read().split("\n")

n = int(data[0])

s = [0]
for i in range(1, n + 1):
    a = [int(x) for x in data[i].split()]

    comb = [b + c for b in s for c in a]
    s = {x % 246: x for x in sorted(comb, reverse=True)}.values()

print(min(x for x in s if (x % 123 != 0 and x % 2 == 0)))
"""  # Три кучи, не делится на 123 при этом четная и минимально возможная (ГРОБ)
"""f = open('27A__7mwr_1.txt')
dif = 10000000000
s = 0
n = int(f.readline())

for i in range(n):
    x, y, z = [int(j) for j in f.readline().split()]
    if max(x, y, z) == x:
        s += x
        if abs(x-y) % 4 != 0:
            dif = min(dif, abs(x - y))
        if abs(x-z) % 4 != 0:
            dif = min(dif, abs(x - z))
    elif max(x, y, z) == y:
        s += y
        if abs(x-y) % 4 != 0:
            dif = min(dif, abs(x - y))
        if abs(y-z) % 4 != 0:
            dif = min(dif, abs(y - z))
    elif max(x, y, z) == z:
        s += z
        if abs(z-y) % 4 != 0:
            dif = min(dif, abs(z - y))
        if abs(x-z) % 4 != 0:
            dif = min(dif, abs(x - z))
if s % 4 != 0:
    print(s)
else:
    print(s - dif)
f.close()


f = open('27B__7mww_2.txt')
arr = [-1000000000000000]*4
arr[0] = 0
for i in range(int(f.readline())):
    x = [int(i) for i in f.readline().split()]
    arr_new = [-1000000000000000]*4

    for j in range(3):
        for l in range(4):
            t = (arr[l] + x[j]) % 4
            arr_new[t] = max(arr_new[t], arr[l] + x[j])

    arr = arr_new
print(max(arr[1::]))
# 332077175
# 2222"""  # Три кучи, не делится на 4




'''
n = int(input())
s = [0]*n
s[0] = int(input())

for i in range(1, n):
    s[i] = s[i-1] + int(input())
print(s)





#1
# Дано число n, затем n чисел. Требуется найти наибольшую подпоследовательность,
# чья сумма будет кратна 10 и максимальна.

n = int(input())
s = [10e16] * 10   # массив кратности
ind = [-10e16] * 10
s[0], ind[0] = 0, -1
summa, ans, dlina = 0, 0, 0


for i in range(n):
    x = int(input())
    summa += x
    t = summa % 10
    
    if summa - s[t] > ans:
        ans = summa - s[t]
        dlina = i - ind[t]
        
    elif summa - s[t] == ans:
        dlina = max(dlina, i - ind[t])
        
    if summa <= s[t]:
        s[t] = summa
        ind[t] = i

print(ans, dlina)





# 2
# Дано число n, затем n чисел. Требуется найти наибольшую подпоследовательность,
# чья сумма будет кратна 10, а ее длина максимальна. Найти длину и сумму.
# Если таких много, то найти мин. сумму

n = int(input())
s, s[0] = [10e16] * 10, 0
ind, ind[0] = [-1] * 10, 0


ans, summ, dlina = 10e16, 0, 0

for i in range(n):
    x = int(input())
    summ += x

    if ind[summ % 10] != -1:
        if i - ind[summ % 10] > dlina:
            dlina = i - ind[summ % 10] + 1 * (summ % 10 != 0)
            ans = summ - s[summ % 10]

        elif i - ind[summ % 10] == dlina:
            ans = min(ans, summ - s[summ % 10])


    if summ < s[summ % 10]:
        s[summ % 10] = summ
        ind[summ % 10] = i

print(ans, dlina)





# АВТОРСКАЯ **
# Дано число n, затем n чисел. Требуется найти подпоследовательность с наименьшим количество элементов,
# чье произведение будет кратно 8 и максимально. Гарантируется, что элемента кратного 8 нет.
# Если таких подпоследовательностей несколько, то найти с макс. произведение
'''  # Подпоследовательности

"""f = open('27_A.txt')
n = int(f.readline())
summ, ans, dlina = 0, 0, 0
ps = [10e16] * 43
ps[0] = 0
ind = [-1] * 43
ind[0] = 0
for i in range(n):
    x = int(f.readline())
    summ += x
    if summ - ps[summ % 43] > ans:
        ans = summ - ps[summ % 43]
        dlina = i - ind[summ % 43] + 1 * (ind[summ % 43] == 0)
    elif summ - ps[summ % 43] == ans:
        dlina = min(dlina, i - ind[summ % 43] + 1 * (ind[summ % 43] == 0))
    if summ < ps[summ % 43]:
        ps[summ % 43] = summ
        ind[summ % 43] = i
print(dlina)

f = open('27_B.txt')
n = int(f.readline())
summ, ans, dlina = 0, 0, 0
ps = [10e16] * 43
ps[0] = 0
ind = [-1] * 43
ind[0] = 0
for i in range(n):
    x = int(f.readline())
    summ += x
    if summ - ps[summ % 43] > ans:
        ans = summ - ps[summ % 43]
        dlina = i - ind[summ % 43] + 1 * (ind[summ % 43] == 0)
    elif summ - ps[summ % 43] == ans:
        dlina = min(dlina, i - ind[summ % 43] + 1 * (ind[summ % 43] == 0))
    if summ < ps[summ % 43]:
        ps[summ % 43] = summ
        ind[summ % 43] = i
print(dlina)
# 185 329329"""  # 27 КЕГЭ 2021 сумма элементов подпоследовательности кратна 43. Найти МАКС сумму и МАКС длину при макс сумме
"""min_ps = [10e16] * 10
min_ps[0] = 0
s = 0
f = open('27-A') # у меня его нет
n = int(input())
nech = 0
ans = 0
for i in range(n):
    x = int(input())
    s += x
    if x % 2 != 0:
        nech += 1
    t = nech % 10

    ans = max(ans, s - min_ps[t])
    min_ps[t] = max(min_ps[t], s)

print(ans)"""  # найти макс. сумму цепочки, в кот. кол-во нечёт. элем кратно 10
"""n = 25
min_ps = [10e16] * 3
min_ps[0] = 0
ans, s = 0, 0

for i in range(n):
    x = int(input())
    s += x
    ost = s % 3
    ans = max(s - min_ps[ost], ans)
    min_ps[ost] = min(min_ps[ost], s)
print(ans)"""  # максимальная сумма подряд идущих чисел, кратная 3.
"""f = open("27_B_1.txt")
n = int(f.readline())
cnt_ps = [0] * 117
s = 0
ans = 0
line = []
for i in range(4):
    now = int(f.readline())
    s += now
    ost = s % 117
    line.append(ost)
for i in range(4, n):
    now = int(f.readline())
    s += now
    ost = s % 117
    ans += cnt_ps[ost]
    cnt_ps[(line[i % 4]) % 117] += 1
    line[i % 4] = s
print(ans + cnt_ps[0])"""  # Непрерывная послед. длиной не менее пяти элем, такая что сумма элем. кратна 117. Найти количество таких послед
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

print(c)"""  # МинПреф. Определить количетсво, сумма элементов кратна 999
'''
n = int(input())
s = [1000000]*5
s[0] = 0
summ = 0
ans = 0
ind = [-1]*5
dlina = 0
for i in range(n):
    summ += int(input())

    if summ - s[summ % 5] > ans:
        ans = summ - s[summ % 5]
        dlina = i - ind[summ % 5]

    elif summ - s[summ % 5] == ans:
        dlina = max(dlina, i - ind[summ % 5])

    if summ < s[summ % 5]:
        s[summ % 5] = summ
        ind[summ % 5] = i
print(ans, dlina)
'''  # Требуется найти подпоследовательность, сумма будет кратна 5, а также максимальна. Если сумм несколько, то найти макс количество элементов
'''
n = int(input())
s = [0]*3
diff = [10000000]*3 #0 -- разность между 1ой группой и 2ой. 1 -- 1ой и 3й. 2 -- 2ой и 3й

for i in range(n):
    a = sorted([int(i) for i in input().split()], reverse=True)
    for j in range(3):
        s[j] += a[j]

    if abs(a[0] - a[1]) % 2 != 0:
        diff[0] = min(abs(a[0] - a[1]), diff[0])

    if abs(a[2] - a[0]) % 2 != 0:
        diff[1] = min(abs(a[0] - a[2]), diff[1])

    if abs(a[2] - a[1]) % 2 != 0:
        diff[2] = min(abs(a[2] - a[1]), diff[2])

if s[0] % 2 != s[1] % 2:
    print(s[2])

else:
    print(s[2]+min(diff[2], diff[1]))
'''  # Набор данных состоит из троек натуральных чисел. Необходимо распределить все числа на три группы,
# при этом в каждую группу должно попасть ровно одно число из каждой исходной тройки.
# Сумма всех чисел в первой группе должна быть чётной, во второй—нечётной.
# Определите минимально возможную сумму всех чисел в третьей группе.




"""# Dominoshki

n = int(input())
y = [int(s) for s in input().split()]
NePer = 1  # Самая  длинная цепочка, которую удалось получить, закончив на этой доминошке, НЕ ПЕРЕРОВАЧИВАЯ ЕЁ
Per = 1    # Самая длинная цепочка, которую удалось получить, закончив на этой доминошке, ПЕРЕВОРАЧИВАЯ ЕЁ
ans = 1    # Самая длинная цепочка (ответ)
for i in range(1, n):
    x = [int(s) for s in input().split()] # текущая считанная доминошка
    # Сейчас доминошка находится в неперевернутом состоянии (x[0], x[1])
    # Для прошлой доминошки были вычислены параметры NePer и Per
    # Сохраним их в другие переменные >>>

    last = NePer    # количество последних неперевернутых
    last_per = Per  # количество последних перевернутых
    Per, NePer = 1, 1

    # Изучаем и сравниваем старые и новые доминошки
    # динамически добавляем в NePer или Per прошлые значения (зависящие от переворота или нет)
    if x[0] == y[1]:     # начало текущей "приклеилось" к концу прошлой (непер + непер)
        NePer = last + 1       # (НЕПЕРЕВЕРТЫШ)
    if x[0] == y[0]:     # начало текущей "приклеилось" к началу прошлой (непер + пер)
        NePer = last_per + 1     # (ПЕРЕВЕРТЫШ)
    if x[1] == y[1]:     # конец текущей "приклеился" к концу предыдущей (пер + непер)
        Per = last + 1     # (ПЕРЕВЕРТЫШ)
    if x[1] == y[0]:     # конец текущей "приклеился" к началу предыдущей (пер + пер)
        Per = last_per + 1

    ans = max(ans, Per, NePer)

    # Отправляем текущую доминошку в предыдущую
    y[0] = x[0]
    y[1] = x[1]

print(ans)



    # DZ

# 1
f = open('27_1__fcl6.txt')
n = int(f.readline())
y = [int(i) for i in f.readline().split()]

np = 1
p = 1
ans = 1

for i in range(1,n):
    x = [int(s) for s in f.readline().split()]
    last_p = p
    last_np = np
    p, np = 1, 1

    if x[0] == y[1]:
        np = last_np + 1
    if x[0] == y[0]:
        np = last_p + 1
    if x[1] == y[0]:
        p = last_p + 1
    if x[1] == y[1]:
        p = last_np + 1

    ans = max(ans, p, np)
    y[0] = x[0]
    y[1] = x[1]

print(ans)


# 2
f = open('27_2__fcl3.txt')
n = int(f.readline())
y = [int(i) for i in f.readline().split()]

p, np, ans = 1, 1, 1

for i in range(1,n):
    x = [int(k) for k in f.readline().split()]
    last_p = p
    last_np = np
    p, np = 1, 1

    if x[0] == y[0]:
        np = last_p + 1
    if x[0] == y[1]:
        np = last_np + 1
    if x[1] == y[0]:
        p = last_p + 1
    if x[1] == y[1]:
        p = last_np + 1

    ans = max(ans, p, np)

    y[0] = x[0]
    y[1] = x[1]

print(ans)


# 3
f = open('27_3__fcl5.txt')
n = int(f.readline())
y = [int(i) for i in f.readline().split()]

p, np, ans = 1, 1, 1

for i in range(1,n):
    x = [int(k) for k in f.readline().split()]
    last_np = np
    last_p = p
    p, np = 1, 1

    if x[0] == y[0]:
        np = last_p + 1
    if x[0] == y[1]:
        np = last_np + 1
    if x[1] == y[0]:
        p = last_p + 1
    if x[1] == y[1]:
        p = last_np + 1

    ans = max(ans, p*(p%2 == 0), np*(np%2 == 0))
    y[0] = x[0]
    y[1] = x[1]
print(ans)



# 4
f = open('27_4__fcl4.txt')
n = int(f.readline())
y = [int(i) for i in f.readline().split()]
p, np, ans = 1, 1, 1

for i in range(1,n):
    x = [int(s) for s in f.readline().split()]
    last_np = np
    last_p = p
    np, p = 1, 1

    if x[0] == y[0]:
        np = last_p + 1
    if x[0] == y[1]:
        np = last_np + 1
    if x[1] == y[0]:
        p = last_p + 1
    if x[1] == y[1]:
        p = last_np + 1

    ans = max(ans, p*(p%2 != 0), np*(np%2 != 0))
    y[0] = x[0]
    y[1] = x[1]
print(ans)


# 5 Под цепочкой понимается последовательность костяшек, в которой второе число первой костяшки не равно первому числу второй.
f = open('27_5__fcl7.txt')
n = int(f.readline())
y = [int(i) for i in f.readline().split()]

p, np, ans = 1, 1, 1

for i in range(1,n):
    x = [int(s) for s in f.readline().split()]
    last_np = np
    last_p = p
    np, p = 1, 1

    if x[0] != y[1]:
        np = last_np + 1
    if x[0] != y[0]:
        np = max(np, last_p + 1)
    if x[1] != y[1]:
        p = last_np + 1
    if x[1] != y[0]:
        p = max(p, last_p + 1)


    ans = max(ans, p, np)
    y[0] = x[0]
    y[1] = x[1]

print(ans)
"""  # Доминошки <3




# ВСЯКОЕ ДРУГОЕ
"""f = open('27986_B.txt')
nA = 21
nB = 60001
nekr = 0
kr = 0
maxim = 0
for i in range(nB):
    x = int(f.readline())
    if x == 0:
        break
    if x % 49 != 0:
        if x % 7 == 0:
            maxim = max(maxim, x * nekr)
            kr = max(kr, x)
        else:
            maxim = max(maxim, x * kr)
            nekr = max(nekr, x)
print(maxim)

f = open('27986_A.txt')
nekr = 0
kr = 0
maxim = 0
x = int(f.readline())
while x != 0:
    if x % 49 != 0:
        if x % 7 == 0:
            maxim = max(maxim, x * nekr)
            kr = max(kr, x)
        else:
            maxim = max(maxim, x * kr)
            nekr = max(nekr, x)
    x = int(f.readline())
print(maxim)
"""  # Количество чисел заранее неизвестно, но не менее двух, признаком конца данных считается число 0.
# Контрольное значение равно такому максимально возможному произведению двух чисел из переданного набора,
# которое делится на 7, но не делится на 49. Если такое произведение получить нельзя, контрольное значение считается равным 1.
'''
Задача со скрина 1

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return max(a,b)

def ncd(a,b):
    return a*b // gcd(a,b)

n = int(input())

ans_5 = [0] * 5
ans_7 = [0] * 7

for i in range(n):
    a = [int(i) for i in input().split()][1:]
    nok = sorted(list(set([ncd(a[j],a[k]) \
                           for j in range(len(a)) for k in range(j+1, len(a))] \
                          )))

    ans_new_5 = [-1000000000] * 5

    for k in range(len(nok)):
        for j in range(5):
            ost = (ans_5[j] + nok[k]) % 5

            if ans_5[j] + nok[k] > ans_new_5[ost]:
                ans_new_5[ost] = ans_5[j] + nok[k]

    ans_5 = ans_new_5

    ans_new_7 = [-1000000000] * 7

    for k in range(len(nok)):
        for j in range(7):
            ost = (ans_7[j] + nok[k]) % 7

            if ans_7[j] + nok[k] > ans_new_7[ost]:
                ans_new_7[ost] = ans_7[j] + nok[k]

    ans_7 = ans_new_7

print(max(ans_7[0], ans_5[0]))
'''  # Набор данных из групп чисел, из каждой группы выбрали два числа и нашли их НОК. Все значения НОК сложили. Определите наиб. сумму кратную 5 или 7 excOR
'''
Задача со скрина 2 

def prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False

    if x != 1:
        return True
    else:
        return False


n = int(input())

data = [] #Все числа из файла

num = [0] * n #Индекс этого массива равен индексу data и показывает, являются ли элементы из data
              #Простыми числами. Если да -- в массиве будет стоять 1.

for i in range(n):
    data += [int(input())]

    if prime(data[i]):
        num[i] += 1

summa = 0 #Сумма всех единиц массива num

s = [1000000]*3 #Мин. частичные суммы, имеющие определенный остаток при делении на 3.
#Почему на 3? Потому количество простых чисел должно быть кратно 3.

s[0] = 0

ind = [-1]*3 #На каком индексе была получена мин. частичная сумма

ind[0] = 0

dlina = 0 #Длина последовательности, в которой сумма наибольшая

kr = 0 #Число, отражающее максимальное количество простых чисел в рассматриваемой
#подпоследовательности, которое будет кратно 3

ans = 0

#3 5 7 11 13 - сами числа

#1 1 1 1 1 - массив, отражающий количество простых чисел сверху

for i in range(n):
    summa += num[i] #Подсчет i-ой частичной суммы из массива 1 и 0

    if summa - s[summa % 3] > 0:
        ans = max(ans, sum( data[ind[summa % 3]:i+1] ))

    if summa < s[summa % 3]: #Обновление мин. частичных сумм
        s[summa % 3] = summa #обновляем частичную сумму
        ind[summa % 3] = i   #Индекс последнего элемента этой суммы

print(ans)

print(data)
print(num)
'''  # Послед. Найти кол0во простых чисел, которое кратно 9. Найти макс сумму такой послед.
'''
def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return max(a,b)

def ncd(a,b):
    return a*b // gcd(a,b)

n = int(input())

ans_5 = [0] * 5
ans_7 = [0] * 7

for i in range(n):
    a = [int(i) for i in input().split()][1:]

    nok = sorted(list(set(
                           [ncd(a[j],a[k]) \
                           for j in range(len(a)) for k in range(j+1, len(a))] \
                          )))

    ans_new_5 = [-1000000000] * 5

    for k in range(len(nok)):
        for j in range(5):
            ost = (ans_5[j] + nok[k]) % 5

            if ans_5[j] + nok[k] > ans_new_5[ost]:
                ans_new_5[ost] = ans_5[j] + nok[k]

    ans_5 = ans_new_5

    ans_new_7 = [-1000000000] * 7

    for k in range(len(nok)):
        for j in range(7):
            ost = (ans_7[j] + nok[k]) % 7

            if ans_7[j] + nok[k] > ans_new_7[ost]:
                ans_new_7[ost] = ans_7[j] + nok[k]

    ans_7 = ans_new_7

print(max(ans_7[0], ans_5[0]))
'''
"""def prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False

    if x != 1:
        return True
    else:
        return False


n = int(input())

data = [] #Все числа из файла

num = [0] * n #Индекс этого массива равен индексу data и показывает, являются ли элементы из data
              #Простыми числами. Если да -- в массиве будет стоять 1.

for i in range(n):
    data += [int(input())]

    if prime(data[i]):
        num[i] += 1

summa = 0 #Сумма всех единиц массива num

s = [1000000]*3 #Мин. частичные суммы, имеющие определенный остаток при делении на 3.
#Почему на 3? Потому количество простых чисел должно быть кратно 3.

s[0] = 0

ind = [-1]*3 #На каком индексе была получена мин. частичная сумма

ind[0] = 0

dlina = 0 #Длина последовательности, в которой сумма наибольшая

kr = 0 #Число, отражающее максимальное количество простых чисел в рассматриваемой
#подпоследовательности, которое будет кратно 3

ans = 0

#3 5 7 11 13 - сами числа

#1 1 1 1 1 - массив, отражающий количество простых чисел сверху

for i in range(n):
    summa += num[i] #Подсчет i-ой частичной суммы из массива 1 и 0

    if summa - s[summa % 3] > 0:
        ans = max(ans, sum( data[ind[summa % 3]:i+1] ))

    if summa < s[summa % 3]: #Обновление мин. частичных сумм
        s[summa % 3] = summa #обновляем частичную сумму
        ind[summa % 3] = i   #Индекс последнего элемента этой суммы

print(ans)

print(data)
print(num)"""
"""n = int(input())
line = []
ans = 0

data = [[0]*10 for i in range(4)]

for i in range(3):
    line.append(int(input()))

for i in range(3, n):
    #1й этап: отправляем крайний слева элемент очереди на свалку
    if line[0] % 14 == 0:
        data[0][line[0] % 10] += 1

    elif line[0] % 7 == 0:
        data[1][line[0] % 10] += 1

    elif line[0] % 2 == 0:
        data[2][line[0] % 10] += 1

    else:
        data[3][line[0] % 10] += 1

    #2й этап: число x взаимодействует со свалкой. считается ответ на данном шаге цикла
    x = int(input())

    if x % 14 == 0:
        for j in range(4):
            for k in range(10):
                if k != (10 - x % 10) % 10:
                    ans += data[j][k]

    elif x % 7 == 0:
        for j in range(0, 4, 2):
            for k in range(10):
                if k != (10 - x % 10) % 10:
                    ans += data[j][k]

    elif x % 2 == 0:
        for j in range(2):
            for k in range(10):
                if k != (10 - x % 10) % 10:
                    ans += data[j][k]

    else:
        for j in range(1):
            for k in range(10):
                if k != (10 - x % 10) % 10:
                    ans += data[j][k]

    #3й этап: сдвиг очереди. x попадает в очередь
    for j in range(3-1):
        line[j] = line[j+1]
    line[2] = x

print(ans)"""  # Требуется найти количество среди всех пар чисел, кратное 14, так что сумма двух чисел будет некратна 10,
# а также парой считаются элементы, которые находятся на расстоянии 3 и более
"""def f(s):
    global max
    if s == n:
        k = sum(a)
        if k % 3 != 0 and k > max:
            max = k
        return

    a[s] = x[s][0]

    f(s + 1)
    a[s] = x[s][1]

    f(s + 1)


file = open("27-A_demo (1).txt", "r")
n = int(file.readline())
a = [0] * n  # массив который хранит варианты перебора
x = []  # массив который хранит исходные пары
max = 0
for i in range(n):
    c, b = map(int, file.readline().split())
    x.append([c, b])
f(0)
print(max)
"""  # bebra ot Koly rekurisya
"""def f(b):
    global n, sum
    if b == n:
        sumv = 0
        ves = 0
        for i in range(len(s)):
            if s[i] == 1:
                sumv += a[i][1]
                ves += a[i][0]
                if ves <= 40 and sumv > sum:
                    sum = sumv
        return
    s[b] = 0
    f(b+1)
    s[b] = 1
    f(b+1)

file = open("ЯрюкзакЯрюкзак")
n, k = map(int, file.readline().split())
a = []
for i in range(n):
    m, s = map(int, file.readline().split())
    a.append([m, s])
sum = 0
a = sorted(a)
l = 6
s = [0]*n
f(0)
print(sum)"""  # Рюкзак 27 (или 26)
"""# Вроде должна решать задачку

f = open('input.txt')
n = int(f.readline())
a = [10000000000000000000000] * 17
b = [10000000000000000000000] * 3
a[0] = 0
b[0] = 0
d3 = 10000000000000000000
d17 = 10000000000000000000
for i in range(n):
    hz = [int(j) for j in f.readline().split()]
    a_new = [10000000000000000000000] * 17
    b_new = [10000000000000000000000] * 3
    for t1 in range(3):
        for t2 in range(t1 + 1, 3):
            for j in range(17):
                A = abs(hz[t1] - (sum(hz) - hz[t2] - hz[t1]))
                B = abs(hz[t2] - (sum(hz) - hz[t2] - hz[t1]))
                if A % 3 != 0 and A % 3 == 0 and A < d3:
                    d3 = A
                if B % 3 != 0 and B % 3 == 0 and B < d3:
                    d3 = B
                ost = (hz[t1] + hz[t2] + a[j]) % 17
                a_new[ost] = min(a_new[ost], hz[t1] + hz[t2] + a[j])
    a = a_new

    for t1 in range(3):
        for t2 in range(t1 + 1, 3):
            for j in range(3):
                A = abs(hz[t1] - (sum(hz) - hz[t2] - hz[t1]))
                B = abs(hz[t2] - (sum(hz) - hz[t2] - hz[t1]))
                if A % 17 != 0 and A % 3 == 0 and A < d17:
                    d17 = A
                if B % 17 != 0 and B % 3 == 0 and B < d17:
                    d17 = B
                ost = (hz[t1] + hz[t2] + b[j]) % 3
                b_new[ost] = min(b_new[ost], hz[t1] + hz[t2] + b[j])
    b = b_new
ANS = 1000000000000000000
if a[0] % 3 == 0:
    ANS = min(ANS, a[0] + d3)
else:
    ANS = min(ANS, a[0])
if b[0] % 17 == 0:
    ANS = min(ANS, b[0] + d17)
else:
    ANS = min(ANS, b[0])

print(ANS)

# 218073 1874142240"""  # Из каждой тройки 2 числа так, чтобы сумма делилась на 3 ИЛИ на 17, но не на 3 И 17 одновременно
# Polyakof
"""f = open('27-1b.txt')
n = int(f.readline())
s = 0
diff = 10e16
for i in range(n):
    x, y = [int(i) for i in f.readline().split()]
    s += min(x, y)
    t = abs(x-y)
    if t % 3 != 0:
        diff = min(diff, t)

print(s + diff*(s%3==0))"""  # 1
"""f = open('27-2b.txt')
n = int(f.readline())
s = 0
diff = [10e16]*3
for i in range(n):
    x, y = [int(i) for i in f.readline().split()]
    s += max(x, y)
    t = abs(x - y)
    ost = t % 3
    diff[ost] = min(diff[ost], t)

if s % 3 == 0:
    print(s)
elif s % 3 == 1:
    print(s - diff[1])
else:
    print(s - diff[2])
# 109737 401536407"""  # 2
"""f = open('27-3b.txt')
n = int(f.readline())
ans = [0]*3
for i in range(n):
    x, y = [int(i) for i in f.readline().split()]
    ans_new = [1000000000000000000000000]*3

    for j in range(3):
        ost = (x + ans[j]) % 3
        ans_new[ost] = min(ans_new[ost], x + ans[j])

    for j in range(3):
        ost = (y + ans[j]) % 3
        ans_new[ost] = min(ans_new[ost], y + ans[j])

    ans = ans_new
print(ans[0])
# 66228 203412732"""  # 3
"""# 1
n = int(input())
kr, nekr = 0, 0
ans = 0
line = []
for _ in range(4):
    line.append(int(input()))

for i in range(4, n):
    x = int(input())
    if x % 2 == 0:
        ans += nekr + kr
    else:
        ans += kr
    if line[i % 4] % 2 == 0:
        kr += 1
    else:
        nekr += 1
    line[i % 4] = x
print(ans)


# 2
n = int(input())
kr3, nekr = 0, 0
ans = 0
line = []
k = [0]*100
for _ in range(4):
    line.append(int(input()))

for i in range(4, n):
    x = int(input())
    ost = x % 100
    dop = (100 - ost) % 100
    ans += k[dop]
    k[line[i % 4] % 100] += 1
    line[i % 4] = x
print(ans)"""  # Две задачки

"""ans = 0
line = []
n = int(input())
for _ in range(12):
    line.append(int(input()))
m = []
for j in range(25):
    m += [[0] * 31]
m = [m, m]
print(m)
# m - двумерный массив из 25 массивов, каждый из которых состоит из 31 элемента. m[8] - это массив элемента, который отвечает
# за числа, которые делятся на 8, но не делятся на 24 и 12. Ячейки(то есть вторая []) отвечает за остатки от деления на 31.
# m[8][18] - количество чисел на свалке, которые делятся на 8, Но не делятся на 24, 12, при этом дают остаток 18 при делении на 31.
for i in range(12, n):
    x = int(input())
    dop = (31 - x % 31) % 31
    ans += sum(m[j][k][dop] for j in range(2) for k in range(1, 25) if
               (24 % k == 0) and ((kx) % 24 == 0) and (j == 1 or x >= 100))
    l = line[i % 12]
    z = max(j for j in range(1, 25) if ((l % j == 0) and (24 % j == 0)))
    m[l >= 100][z][l % 31] += 1
    line[i % 12] = x
print(ans)"""  # ГРОБ

# РЕШУ ЕГЭ >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Еще один способ решения стандарта I
"""f = open('27985_B.txt')
n = int(f.readline())
arr = [0] * 14

ans = 0
for i in range(n):
    x = int(f.readline())
    for j in range(14):
        t = x * arr[j]
        if t % 14 == 0:
            ans = max(ans, t)
    arr[x % 14] = max(arr[x % 14], x)
print(ans)
f.close()
# 719740 994000"""  # Произведение двух чисел, кратное 14
"""f = open('27988_B.txt')
n = int(f.readline())

arr = [0] * 26
R = 0
for i in range(n):
    x = int(f.readline())
    for j in range(26):
        t = x * arr[j]
        if t % 26 == 0:
            R = max(R, t)
    arr[x % 26] = max(arr[x % 26], x)
print(R)
f.close()
# 783900 988000"""  # Произведение двух чисел, кратное 26
"""f = open('27986_B.txt')
arr = [0]*49
ans = 0

x = int(f.readline())
while x != 0:
    for j in range(49):
        t = x * arr[j]
        if t % 7 == 0 and t % 49 != 0:
            ans = max(ans, t)
    arr[x % 49] = max(arr[x % 49], x)
    x = int(f.readline())
print(ans)
f.close()
# 847280 994000"""  # Произведение двух чисел, кратное 7 и некратное 49
"""f = open('27990_B.txt')
n = int(f.readline())
# 62 = 31 * 2
k62 = 0
k31 = 0
k2 = 0
nekr = 0

ans = 0

for i in range(n):
    x = int(f.readline())
    if x % 62 == 0:
        ans += k62 + k31 + k2 + nekr
        k62 += 1
    elif x % 31 == 0:
        ans += k62 + k2
        k31 += 1
    elif x % 2 == 0:
        ans += k62 + k31
        k2 += 1
    else:
        ans += k62
        nekr += 1
print(ans)
f.close()


f = open('27990_B.txt')
n = int(f.readline())
arr = [0]*62
ans = 0

for i in range(n):
    x = int(f.readline())
    for j in range(62):
        t = x * j
        if t % 62 == 0:
            ans += arr[j]
    arr[x % 62] += 1
print(ans)
f.close()

# 0 82307095 """  # Количество произведение двух чисел, кратное 62 (2 способа)

"""f = open('27991_B.txt')
n = int(f.readline())

maxim = 0
kr = 0
nekr = 0
ans = ()
for i in range(n):
    x = int(f.readline())
    if x % 17 == 0:
        if (kr+x)*(abs(kr-x) % 2 == 0) > maxim:
            maxim = (kr+x)*(abs(kr-x) % 2 == 0)
            ans = (kr, x)
        elif (nekr+x)*(abs(nekr-x) % 2 == 0) > maxim:
            maxim = (nekr+x)*(abs(nekr-x) % 2 == 0)
            ans = (nekr, x)
        kr = max(kr, x)
    else:
        if (kr + x) * (abs(kr - x) % 2 == 0) > maxim:
            maxim = (kr + x) * (abs(kr - x) % 2 == 0)
            ans = (kr, x)
        nekr = max(nekr, x)
print(*ans)
# 3077 8759
# 10000 9996"""  # Два числа: хотяб 1 число делится на 17, а разность четна. Вывести пару
"""f = open('28128_B.txt')
n = int(f.readline())

R = [0]*3
ans = 0
for i in range(n):
    x = int(f.readline())
    ans = max(ans, R[(3 - x % 3) % 3] + x)
    R[x % 3] = max(R[x % 3], x)
print(ans)
# 19020 19998"""  # Макс сумма двух чисел, кратная 3
"""f = open('TEST.txt')
n = int(f.readline())
ans = []
maxim = 0
arr = [0] * 160
for i in range(n):
    x = int(f.readline())
    for y in arr:
        if x % 7 == 0:
            if x + y > maxim and (x - y) % 160 != 0:
                maxim = x + y
                ans = [x, y]
            elif x + y > maxim and (x - y) % 160 != 0 and y % 7 == 0:
                maxim = x + y
                ans = [x, y]
        else:
            if x + y > maxim and (x - y) % 160 != 0 and y % 7 == 0:
                maxim = x + y
                ans = [x, y]
    arr[x % 160] = max(arr[x % 160], x)
ans.sort()
print(*ans)
f.close()


# 728 977
# 9982 9992"""  # Различные остатки от деления 160 и хотяб одно делится на 7
"""f = open('28130_B.txt')
n = int(f.readline())

b = [0] * 80
m = [0] * 80
ans = 0
for i in range(n):
    x = int(f.readline())
    dop = (80 - x % 80) % 80
    ans += m[dop] * (x > 50) + b[dop]
    b[x % 80] += (x > 50)
    m[x % 80] += not (x > 50)
print(ans)
# 3 625350"""  # Два числа, сумма делится на 80 и хотяб 1 число больше 50
"""f = open('28131_B.txt')
n = int(f.readline())
maxim = 0
arr = [0] * 120
ans = []

for i in range(n):
    x = int(f.readline())
    ost = x % 120
    dop = (120 - ost) % 120
    if x + arr[dop] > maxim and arr[dop] != 0:
        maxim = x + arr[dop]
        ans = [x, arr[dop]]
    arr[ost] = max(arr[ost], x)

ans.sort()
ans.reverse()
print(*ans)
# 8096 6544
# 9993 9927"""  # Cумма двух чисел, кратная 120

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




# ГРОБЫ
"""# НОД(55;77) = 11
# НОК(55;77) = 5*7*11

# НОД(a;b) * НОК(a;b) = a*b

from math import *
# print(gcd(100, 150)) # НОД
# print(lcm(100, 150)) # НОК

ans = [0] * 88
f = open('Задание_27_B__nz28 (1).txt')
n = int(f.readline())

for i in range(n):
    a = [int(p) for p in f.readline().split()][1:]
    noks = [lcm(a[i], a[j]) for i in range(len(a)) for j in range(i+1, len(a))]
    ans_new = [0] * 88

    for j in noks:
        for l in range(88):
            ost = (j + ans[l]) % 88
            ans_new[ost] = max(ans_new[ost], j + ans[l])
    ans = ans_new[:]
# тк как кратно 8 или кратно 11, то
print(max([i for i in ans if i % 8 == 0 or i % 11 == 0]))

f.close()"""  # (1) НОК, НОД - алгоритм Евклида
"""# Неэффективная
f = open('dsrk_27A.txt')

n = int(f.readline())
a = [int(i) for i in f]
ans = 100000000000
index = 0
for i in range(n):
    s = 0
    for j in range(n):
        dlina = min(abs(i-j), n - abs(i-j))
        s += dlina * a[j]
    if s < ans:
        ans = s
        index = i
print(ans, index + 1)

# Эффективная
f = open('dsr_28B.txt')
n = int(f.readline())
a = []
for i in range(n):
    a.append(int(f.readline()))
s = [0] * n
summa = 0
for i in range(n // 2):
    summa += a[i]
s[0] = summa
for i in range(1, n):
    s[i] = s[i - 1] - a[i - 1] + a[(i - 1 + n // 2) % n]

cost = 0  # стоимость доставки в нулевую ячейку
for i in range(n):
    cost += min(i, n - i) * a[i]
minim = cost
ans = 0
for i in range(1, n):  # мы сдвигаем домик из i-1 ячейки в i-ю
    cost = cost - s[i] + s[(i + n // 2) % n]
    if cost < minim:
        minim = cost
        ans = i
print(minim, ans+1)
f.close()

# Еще одна эффективная через префсуммы
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
f.close()

"""  # (2) ДОСРОК - мусорки
"""f = open('input.txt')
ost = [[-1000000000, -1000000000, -1000000000, -1000000000],
       [-1000000000, -1000000000, -1000000000, -1000000000],
       [-1000000000, -1000000000, -1000000000, -1000000000],
       [-1000000000, -1000000000, -1000000000, -1000000000]]

n = int(f.readline())
for i in range(n):
    x = int(f.readline())
    if x > min(ost[x % 4]):
        ost[x % 4].append(x)
        ost[x % 4].sort()
        del ost[x % 4][0]
ost_new = ost[0] + ost[1] + ost[2] + ost[3]
max_sum = 0

from itertools import combinations
for i in combinations(ost_new, 4):
    if sum(i) % 4 == 0 and sum(i) > max_sum:
        max_sum = sum(i)
print(max_sum)
f.close()"""  # (3) 4 числа, чтобы сумма делилась на 4 и была МАКС
"""f = open('input.txt')
n = int(f.readline())
summ = 0
razn = []
for i in range(n):
    a, b = [int(j) for j in f.readline().split()]
    summ += max(a, b)
    razn.append(abs(a-b))
razn.sort()
print(summ, summ % 7, summ % 5)
for i in range(len(razn)):
    if (summ - razn[i]) % 5 != 0 and (summ - razn[i]) % 7 != 0:
        summ = summ - razn[i]
        print(summ)
        break"""  # (4) Макс сумма из двух куч, которая не делится на 7 и 5
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
print(count) # >>> 346556678"""  # (5) Статград 27.04 (кол-во подпосл, mult % 980_869 != 0)
"""f = open('input.txt')
n = int(f.readline())

a = [10000000000000000] * 51
a[0] = 0

for i in range(n):
    N = [int(j) for j in f.readline().split()]
    X = N[0]+N[1], N[1]+N[2], N[0]+N[2]
    a_new = [10000000000000000] * 51
    for t in X:
        for j in range(51):
            ost = (t + a[j]) % 51
            a_new[ost] = min(a_new[ost], t + a[j])
    a = a_new
MAX3 = min(a[3], a[6], a[9], a[12], a[15], a[18], a[21], a[24], a[27], a[30], a[33], a[36], a[39], a[42], a[45], a[48])
MAX17 = min(a[17], a[34])
print(min(MAX3, MAX17))"""  # (6) Из каждой тройки 2 числа, чбы сумма : на 3 ИЛИ на 17, но не на 3 И 17 одновременно
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
print(maxim)"""  # (7) 2 числа из тройки. Макс сумма выбранных s % 7 == 3 или s % 10 == 5
"""f = open('zxc.txt')
n = int(f.readline())

k0, k1, k2 = 1, 0, 0

for i in range(n):
    x = int(f.readline())
    n_k0, n_k1, n_k2 = 0, 0, 0
    if x % 3 == 0:
        n_k0 = k0*2
        n_k1 = k1*2
        n_k2 = k2*2
    if x % 3 == 1:
        n_k0 = k0 + k2
        n_k1 = k1 + k0
        n_k2 = k2 + k1
    if x % 3 == 2:
        n_k0 = k0 + k1
        n_k1 = k1 + k2
        n_k2 = k2 + k0

    k0, k1, k2 = n_k0, n_k1, n_k2
print(k0)"""  # (8) №3822 Группы чисел из любого кол-ва элементов. Найти кол-во, для которых сумма элементов кратна 3
"""
f = open('27-B_5.txt')
n, k = [int(i) for i in f.readline().split()]
mass = [int(i) for i in f]

counter = 0
s = 0

for i in range(n):
    s += mass[i]

    if s < 0:
        s = 0

    counter = (s-1)//k + 1

print(counter, s)


def notEFF():
    f = open('27-A_4.txt')
    n = int(f.readline())

    mass = [int(i) for i in f]
    num = 0
    minim = 10e100
    for i in range(n):
        s = 0
        for j in range(n):
            dlina = min(abs(i - j), n - abs(i - j))
            s += mass[j] * dlina
        if s < minim:
            minim = s
            num = i + 1
    f.close()
    return num, minim


print(notEFF()[0])


def EFF():
    f = open('27-B_6.txt')
    n = int(f.readline())
    a = [int(i) for i in f]
    minim = 10 ** 20
    cost = [0] * n
    for i in range(n):
        r = min(i, n - i)
        cost[0] += r * a[i]
    naprotiv = n // 2
    summ_szadi = sum(a[naprotiv:])
    summ_vperedi = sum(a[1:naprotiv])
    for i in range(1, n):
        summ_szadi += a[i - 1] - a[naprotiv]
        summ_vperedi += a[naprotiv]
        cost[i] = cost[i - 1] - summ_vperedi + summ_szadi
        summ_vperedi -= a[i]
        naprotiv = (naprotiv + 1) % n
        if cost[i] < minim:
            minim = cost[i]
            res = i + 1
    f.close()
    return res

print(EFF())
"""  # (9) Кольца досрок
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
print(ans)"""  # (10) Подпосл сумма % 39, количество <= 20
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
    print(sMAX + sMIN - min(m1, m2+m3))"""  # (11) Необходимо выбрать пары, чтобы второе число в паре было нечётным, сумма бо́льших была чётной, а сумма меньших – нечётной.
                  # Какую наибольшую сумму чисел во всех выбранных парах можно при этом получить?
"""

    # НЕЭФФ
f = open('zxc.txt')
n = int(f.readline())
a = [int(i) for i in f]

s = []  # Массив сумм подмножеств
for x in a:
    s = s + [a+x for a in s] + [x]
print(max(x for x in s if x % 17 == 0))

    # ЭФФ
f = open('zxc.txt')
n = int(f.readline())
s = []
m = 0

for i in range(n):
    x = int(f.readline())
    s = s + [a+x for a in s] + [x]
    s = {x % 17: x for x in sorted(s)}
    if 0 in s:
        m = max(m, s[0])
    s = list(s.values())
print(m)"""  # (12) Подмножества. Наиб. сумма подмножества, кратная 17
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
print(m)"""  # (13) НЕЭФФ 4 числа, сумма не делится на 9
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
print(m)"""  # (13) ЭФФ 4 числа, сумма не делится на 9
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
print(dm[0])"""  # (14) Разность двух сумм максимальна и кратна 5
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
print(m)"""  # (15) НЕЭФФ выбор из пары



# Досрок - любимое решение
f = open('zxc.txt')
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
ans = 0
for i in range(1, n):
    cost = cost - s[i] + s[(i + n//2) % n]
    if cost < m:
        m = cost
        ans = i + 1
print(m * 3, ans)






# Полная имба
from itertools import combinations

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x, y in combinations(a, 2):
    print(x, y, x+y)















