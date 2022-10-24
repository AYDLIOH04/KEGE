"""
f = open('11.txt')
a = [int(i) for i in f]
n = len(a)
c = 0
minim = 100000000000000
for i in range(n-1):
    proizv = a[i]*a[i+1]
    sum = a[i]+a[i+1]
    if (proizv % 6 == 0) and (sum % 3 == 0) and ((bin(sum))[-1] == '0'):
        c+=1
        minim = min(sum,minim)
print(c,minim)

f = open('12.txt')
c = 0
minim = 1000000000000000000000000000
a = [int(i) for i in f]
n = len(a)
for i in range(n-1):
    proizv = a[i]*a[i+1]
    sum = a[i]+a[i+1]
    if (proizv % 6 == 0) and (sum % 9 == 0) and (hex(sum)[-1] == '7'):
        c+=1
        minim = min(minim,sum)
print(c,minim)

f = open('13.txt')
c = 0
minim = 100000000000
a = [int(i) for i in f]
n = len(a)
for i in range(n-1):
    if (a[i]*a[i+1]) % (a[i]+a[i+1]) == 0:
        c+=1
    minim = min((a[i]+a[i+1],minim))
print(c,minim)

f = open('14.txt')
a = [int(i) for i in f]
n = len(a)
c = 0
minim = 1000000000000000000
for i in range(n-1):
    proizv = a[i]*a[i+1]
    sum = a[i]+a[i+1]
    if (proizv % sum == 0) and (sum % 10 == 2):
        c+=1
    minim = min(minim,sum)
print(c,minim)

f = open('15.txt')
a = [int(i) for i in f]
n = len(a)
c = 0
minim = 1000000000000000
for i in range(n-1):
    proizv = a[i]*a[i+1]
    sum = a[i]+a[i+1]
    proizv //= 1000
    if sum % proizv == 0:
        c+=1
        minim = min(minim,a[i],a[i+1])
print(c,minim)
""" # 17 ЗАДАНИЕ
'''
a = 5221
b = 19651
c,minim = 0,10000000000000000
for i in range(a,b+1):
    if (i % 6 == 0) and (i % 5 != 0) and (i % 9 != 0):
        c+=1
        if c == 1:
            minim = i
print(c,minim,sep='')

a = 20321
b = 34621
c, minim = 0, 1000000000000000
for i in range(a, b + 1):
    if i % 13 == 0 and i % 4 == 2:
        c += 1
        minim = min(i, minim)
print(c, minim, sep='')

c = 0
n = int(input())
a = [int(i) for i in input().split()]
for i in range(n-1):
    if (a[i]+a[i+1]) % 5 == 0:
        c+=1
print(c)
''' # Что-то

"""
k = 0
n = int(input())
m = int(input())

for i in range(n):
    for j in range(m):
        k+=1
print(k)

#счетчик ребер полного графа
n = int(input())
m = 0
for i in range(n):
    for j in range(i+1,n):
        print(i,j)
        m+=1
print(m)

#дано n, затем n чисел
# найти максимальную сумму в паре, кратную 100(из двух чисел)
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
m = -10000000000
for i in range(n):
    for j in range(i+1,n):
        if ((a[i]+a[j]) % 100 == 0):
            if(a[i]+a[j]>m):
                m = a[i]+a[j]
print(m)

m = 0
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
for i in range(n):
    for j in range(i,n):
        #рассмотрим подпоследовательность от i до j
        s = 0
        for k in range(i,j+1):
            s += a[k]
        if s%71 == 0:
            m+=1
print(m)

c = 0
for i in range(5):
    for j in range(5):
        for k in range(5):
            print(i,j,k)
            c+=1
print(c)

c = 0
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                for x5 in range(2):
                    for x6 in range(2):
                        for x7 in range(2):
                            for x8 in range(2):
                                for x9 in range(2):
                                    for x10 in range(2):
                                        print(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,sep="")
                                        c+=1
print(c)


    #МНОЖЕСТВА, но ниже написанная хуета не имеет смысла, тк мы не работаем с буквами
    #Этот же перебор, немного переработанный, может работать так же с числами.
    #Вся суть - БЕРЕБОР БЕЗ ПОВТОРЕНИЯ!!!
a = ['A','B','C','D']

#переберем пустые множества:
b =[]
print(b)

#переберем множества из ОДНОГО элемента:
for i in range(4):
    b = []
    b.append(a[i])
    print(b)

#переберем множества из ДВУХ элементов:
for i in range(4):
    for j in range(i+1,4): #ЧТОБЫ БЫЛО БЕЗ ПОВТОРА, т.е ABC не повторялось с CBA
         b = []
         b.append(a[i])
         b.append(a[j])
         print(b)

#переберем множества из ТРЕХ элементов:
for i in range(4):
    for j in range(i+1,4):
        for k in range(j + 1, 4):
            b = []
            b.append(a[i])
            b.append(a[j])
            b.append(a[k])
            print(b)

#множество из 4-х элементов:
print(a)
""" # Вроде гробы
"""
    #задание 1
n = int(input())
#если без повторяющихся
for i in range(n):
    for j in range(i+1,n):
        print(i,j)

    #задание 2
n = int(input())
m = int(input())
c = 0
for i in range(n):
    for j in range(m):
        c+=1
print(c)

    #задание 3
n = int(input())
m = int(input())
for i in range(n):
    for j in range(m):
        print(i,j)

    #задание 4
a,b = [],[]
print("Введите количество мальчиков и девочек")
n = int(input())
m = int(input())

print("Введите имя мальчиков >>> ")
for i in range(n):
    a.append(input())

print("Введите имя девочек >>> ")
for i in range(m):
    b.append(input())

for i in a:
    for j in b:
        print(i,'+',j)

    #задание 5
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

for i in range(n):
    for j in range(i+1,n):
        print(a[i],a[j])

    #задание 6
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max = 0
for i in range(n):
    for j in range(i+1,n):
        if (a[i]*a[j] > max):
            max = a[i]*a[j]
print(max)

    #задание 7
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
min = 10000000000000
for i in range(n):
    for j in range(i+1,n):
        if (a[i]+a[j] < min):
            min = a[i]+a[j]
print(min)

    #задание 8
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max = -1000000
for i in range(n):
    for j in range(i+1,n):
        if (a[i]+a[j] > max) and ((a[i]+a[j]) % 4 ==0):
            max = a[i]+a[j]
print(max)

    #задание 9
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max = -1000000000000
for i in range(n):
    for j in range(i+1,n):
        if (a[i]*a[j] > max) and ((a[i]*a[j])%3 == 0):
            max = a[i]*a[j]
print(max)

    #задание 10
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
min = 10000000000
for i in range(n):
    for j in range(i+1,n):
        if (a[i]*a[j] < min) and ((a[i]*a[j])%15 == 0):
            min = a[i]*a[j]
print(min)""" # Начало 27

"""f = open('17-n5.txt')
a = [int(i) for i in f]
c = 0
minim = 1000000
summ = 0
arr = [int(i) for i in a if i % 35 == 0]
for i in arr:
    chisla = [int(j) for j in str(i)]
    summ += sum(chisla)

for i in range(len(a) - 1):

    if a[i] > summ and a[i+1] % 256 == int('EF', 16) and a[i+1] <= summ:
        c += 1
        minim = min(minim, a[i] + a[i + 1])

    elif a[i+1] > summ and a[i] % 256 == int('EF', 16) and a[i] <= summ:
        c += 1
        minim = min(minim, a[i] + a[i + 1])

print(c, minim)""" # В файле последовательность, найти макс четный и макс нечентый. Если максЧЕТ > максНЕЧЕТ
"""
a = [5, 10, 5, 8, 5, 7, 3, 8, 0]
ans = 0
count_nch = 0
summ_nch = 0

for i in range(len(a)):
    if a[i] % 2 != 0:
        summ_nch += a[i]
        count_nch += 1

sr = summ_nch/count_nch

for i in range(len(a)-2):
    if sr in a[i:i+3] and a[i] < a[i+1] > a[i+2]:
        ans += 1
print(ans)

#Вместо этого for сделать генератор, который ищет ср. ар. нечетных

#[*что берем* *откуда берем* *при каких условиях*]

sr = [a[i] for i in range(len(a)) if a[i] % 2 != 0]
sr = sum(sr)/len(sr)
print(len([a[i:i+3] for i in range(len(a)-2) if sr in a[i:i+3] and a[i] < a[i+1] > a[i+2]]))
""" #Рассматриваются тройки чисел, тройкой являются три элемента, стоящие рядом
                #Требуется найти количество троек, в которых хотя бы один
                #элемент является среднеарифметическим вообще всех нечетных чисел,
                #а средний элемент тройки строго больше остальных двух.
"""a = [5, 10, 5, 8, 5, 7, 3, 8, 0]
ans = 0
for i in range(len(a)-2):
    if sum(a[i:i+3]) % 5 == 0 and a[i]*a[i+1]*a[i+2] % 10 == 0:
        ans += 1
print(ans)
""" #Рассматриваются тройки чисел, тройкой являются три элемента, стоящие рядом
                #Требуется найти количество троек, чья сумма кратна 5, а произведение кратно 10.
"""
a = [5, 10, 5, 8, 5, 7, 3, 8, 0]
sum_max = 0
sum_min = 1000000

for i in range(len(a)-1):
    if a[i] + a[i+1] > sum_max and (a[i] + a[i+1]) % 4 == 0:
        sum_max = a[i] + a[i+1]
    if a[i] + a[i+1] < sum_min and (a[i] + a[i+1]) % 4 == 0:
        sum_min = a[i] + a[i+1]

print(sum_max, sum_min)"""#Рассматриваются пары чисел, парой являются два элемента, стоящие рядом
                #Требуется найти пару с максимальной и минимальной суммой элементов, которая будет кратна 4.
"""a = []
while True:
    a.append(int(input()))
    if a[-1] == -1:
        a = a[:len(a)-1]
        break

chet = max(a) % 2
ans = 0
minim = 10000000
for i in range(len(a)):
    if a[i] % 2 == chet:
        ans += 1
        minim = min(a[i], minim)
print(ans, minim)



a = []
while True:
    a.append(int(input()))
    if a[-1] == -1:
        a = a[:len(a)-1]
        break

ans = [a[i] for i in range(len(a)) if a[i] % 2 == max(a) % 2]
print(len(ans), min(ans))""" # Необходимо найти максимальный чётный и максимальный нечётный элемент
                # последовательности. Если максимальный чётный больше максимального
                # нечётного, то программа должна вывести количество чётных,
                # а также минимальный из них. В противном случае программа
                # должна вывести количество нечётных, а также минимальный из них.
"""def num(x):
    ans = ''
    while x > 0:
        ans += str(x % 7)
        x //= 7
    return ans[::-1]

a = []
while True:
    a.append(int(input()))
    if a[-1] == -1:
        a = a[:len(a)-1]
        break

ans = 0
maxim = 0

for i in range(len(a)-1):
    summ = a[i] + a[i+1]
    if num(summ) == num(summ)[::-1]:
        ans += 1
        maxim = max(int(num(summ)), maxim)
print(ans, maxim)



def num(x):
    ans = ''
    while x > 0:
        ans += str(x % 7)
        x //= 7
    return ans[::-1]

a = []
while True:
    a.append(int(input()))
    if a[-1] == -1:
        a = a[:len(a)-1]
        break

ans = [int(num(a[i]+a[i+1])) for i in range(len(a)-1) if num(a[i]+a[i+1]) == num(a[i]+a[i+1])[::-1]]
print(len(ans), max(ans))""" # Определите сначала количество пар,
                # сумма элементов которых при переводе в систему счисления с основанием 7
                # образует число-палиндром,
                # а затем наибольшую сумму-палиндром в семеричной системе счисления.
                # Под парой чисел подразумевается
                # два идущих подряд элемента последовательности
