"""from collections import Counter
a = 'abcbcbcbcbcbbcbcbcbcbcbgggggggggggyufioaehagjsdghggggggggggggggggggggggggggggggdkgjkjgkxdggggggggg'
print(Counter(a))""" # наиболее встречаемый символ строке (2 строчки кода)


'''
#1 ans >>> '1'*20 = '0'*20
a = '1' * 20
while '1' in a:
    if '1' in a:
        a = a.replace('1','0',1)
print(a)

#2 ans >>> '0'* 19 + 1
a = '1' * 20
while '11' in a:
    if '1' in a:
        a = a.replace('1','0',1)
print(a)

#3 ans >>> 22
a = '2' * 15
while '222' in a:
    if '22' in a:
        a = a.replace('22','2',1)
print(a)

#4
a = '3' * 10
while '33' in a:
    if '33' in a:
        a = a.replace('33','32',1)
print(a)

#5
a = '1' * 10 + '5' * 10
while '15' in a:
    if '15' in a:
        a = a.replace('15','51',1)
print(a)

#6
f = open('Задача 6.txt')
x = f.readline()
print(x.count('V'))

#7
f = open('Задача 7.txt')
x = f.readline()
print(x.count('M'))

#8
f = open('Задача 8.txt')
x = f.readline()
print(x.count('VV'))

#9
f = open('Задача 9.txt')
x = f.readline()
c = 0
for i in range(2,len(x)):
    if x[i] == 'V' and x[i-2] == 'V':
        c+=1
print(c)

#10
f = open('Задача 10.txt')
x = f.readline()
c = 0
for i in range(4,len(x)):
    if x[i] == 'M' and x[i-4] == 'M':
        c+=1
print(c)

    #Norm
#1
a = '12' * 12
while '12' in a or '222' in a:
    a = a.replace('12','2',1)
    a = a.replace('222', '2', 1)
print(a)

#2
a = '571' * 10
while '57' in a or '1111' in a:
    a = a.replace('57','1',1)
    a = a.replace('1111', '1', 1)
print(a)

#3
a = '1' * 10 + '2' * 5 + '333'
while ('12' in a) or ('13' in a) or ('33333' in a):
    if '23' in a:
        a = a.replace('23','3',1)
    elif '13' in a:
        a = a.replace('13', '3', 1)
    elif '333' in a:
        a = a.replace('333', '3', 1)
print(a)

#4
a = '1' * 100 + '2' * 100 + '3'
while ('12' in a) or ('23' in a) or ('33333' in a):
    if '12' in a:
        a = a.replace('12','2',1)
    elif '23' in a:
        a = a.replace('23', '33', 1)
    elif '333' in a:
        a = a.replace('3333', '3', 1)
print(a)

#5
a = '4' * 40 + '8' * 40 + '2' * 50
while ('28' in a) or ('84' in a) or ('24' in a):
    if '24' in a:
        a = a.replace('24', '42', 1)
    elif '84' in a:
        a = a.replace('84', '48', 1)
    elif '28' in a:
        a = a.replace('28', '82', 1)
print(a[24], a[70], a[104],sep="")

#6
f = open('1Задача 6.txt')
x = f.readline()
c = 0
maxim = 0
for i in range(len(x)):
    if x[i] == 'M':
        c+=1
    else:
        c = 0
    if c > maxim:
        maxim = c

print(maxim)

#7
f = open('2Задача 7.txt')
x = f.readline()
c = 0
maxim = 0
for i in range(len(x)):
    if x[i] == 'M':
        c+=1
    else:
        c = 0
    if c > maxim:
        max = c
print(maxim)

#8
f = open('3Задача 8.txt')
x = f.readline()

c0 = 1
c1 = 1
m0 = 0
m1 = 0
n = len(x)
for i in range(0, n-1, 2):
    if x[i] == 'M' and x[i+2] == 'M':
        c0+=1
        if c0 > m0:
            m0 = c0
    else:
        c0 = 1

for i in range(1, n-1, 2):
    if x[i] == 'M' and x[i+2] == 'M':
        c1+=1
        if c1 > m1:
            m1 = c1
    else:
        c1 = 1
if m0 > m1:
    print(m0)
else:
    print(m1)

# 9
f = open('4Задача 9.txt')
x = f.readline()
n = len(x)
c1, c2 = 1, 1
m1, m2 = 0, 0
for i in range(len(x) - 1):
    if x[i] == x[i + 1]:
        c1 += 1
        if c1 > m1:
            m1 = c1
    else:
        c1 = 1

for i in range(len(x) - 1):
    if x[i] != x[i + 1]:
        c2 += 1
        if c2 > m2:
            m2 = c2
    else:
        c2 = 1

print(m1,m2)

# 10
# Текстовый файл состоит не более чем из 106
# символов V, D, M.
# Найдите самую длинную последовательность, состоящую из пар разных элементов, т.е. в последовательности VVDMVDVMMVDVMDVDMMDD условию будет удовлетворять последовательность MMDD.
# Для выполнения этого задания следует написать программу. В ответ запишите
# максимальную длину последовательности

f = open('5Задача 10.txt')
x = f.readline()
n = len(x)
c = 0
flag = True
maxim = 0
for i in range(1,n):
    if (x[i] == x[i-1] and flag == True):
        c+=1
        flag = False

    elif (x[i] == x[i-1] and flag == False):
        if c > maxim:
            maxim = c

    elif (x[i] != x[i-1] and flag == True):
        if c > maxim:
            maxim = c
        c = 0
    else:
        flag = True
print(maxim)

    #hard
#1
a = '7' * 367 + '9' * 34
while '77' in a or '9' in a:
    while '79' in a:
        a = a.replace('79','77',1)
    if '77' in a:
        a = a.replace('77','9',1)
    elif '9' in a:
        a = a.replace('9', '8', 1)

maxim = 0
min = 10000000
for i in range(10):
    t = a.count(str(i))
    if (t > maxim):
        maxim = t
    if (t < min) and (t > 0):
        min = int(i)
print(maxim*min)

# условие неверно прочитал
a = '*' + '2' * 100 + '5' * 10 + '9' * 60
while '*2' in a or '*2' in a or '*9' in a:
    if '*2' in a:
        a = a.replace('*2', '*', 1)
    if '*5' in a:
        a = a.replace('*5', '6*', 1)
    if '*9' in a:
        a = a.replace('*9', '7*', 1)
print(a)
a = a.replace('*','0',1)
sum = 0
print()
for i in range(10):
    sum += i*(a.count(str(i)))
print(sum)
''' # Дезе

'''


#1

s = ['PRIVET',
     'INFORMATIKA',
     'AWERTYUIOPAZXCA']

count = 0
ans = 1
for k in s:
    if k.count('R') != 30:
        char = []
        check = []
        for i in range(len(k)):
            if not(k[i] in char):
                char.append(k[i])
                check.append([k[i], i])

            else:
                for j in range(len(char)):
                    if k[i] == char[j]:
                        ans = max(ans, i-check[j][1])
                        check[j][1] = i
                        count += 1
                        break

print(ans, count)



#2
s = 'AbbbbbbFFFokosdAbbbbbbFkfoskfdAbbbbbbbF'
ans = 0
i = 0
while i < len(s):
    if i + 7 < len(s):
        if s[i] == 'A' and s[i+7] == 'F':
            ans += 1
    if i + 8 < len(s):
        if s[i] == 'A' and s[i+8] == 'F':
            ans += 1
    if i + 9 < len(s):
        if s[i] == 'A' and s[i+9] == 'F':
            ans += 1
    if i + 10 < len(s):
        if s[i] == 'A' and s[i+10] == 'F':
            ans += 1
    i += 1

print(ans)



#3
# Текстовый файл 24-175.txt состоит не более чем из 10**6 символов и содержит только заглавные буквы латинского алфавита E, G, K.
# Определите максимальное количество идущих подряд символов, среди которых сочетания символов KEGE повторяются не более двух раз.

# EEEE KEGE GGGG KEGE egegegegeg KEGE
# EGEGGGGKEGEegegegegegKEGEegegegegegKEGEegegegegeegegegegege

s = "EGEGGGGKEGEegegegegegKEGEegegegegegKEGEegegegegeegegegegege"

counter = 0
check = []
ans = 1

for i in range(len(s) - 3):
    if s[i:i+4] == 'KEGE':
        check += [i]

    if len(check) != 3:
        counter += 1

    else:
        counter += 2
        ans = max(ans, counter)
        counter -= check[0]+1
        check = check[1:]

ans = max(ans, counter+2)

print(len(s), ans)

''' # База :)
'''
#4
with open("1.txt") as f:  # Открываем файлик с задачей
    s = f.read()  # Считываем строку

index_of_Kege = []  # Масссив для индексов "К" из последовательностей "КЕGE"
index_of_kegE = []  # Массив для индексов второй "Е"  из последовательностей "КЕGE"

for i in range(len(s) - 3):  # Цикл для пробежки по строке
    # Берем длинну строки минус 3 для того, чтобы при проверке i+3 элемента на последней итерации
    # s[i + 3] элемент не выходил за пределы массива

    if s[i:i + 4] == 'KEGE':  # Проверка для нахожедения последовательности "KEGE" с помощью срезов
        # Слева от двоеточия первый элемент(начало)
        # Справа от двоеточия последний элемент(конец)
        # По умолчанию шаг равен единице

        index_of_Kege.append(i)  # Записываем в массив индекс буквы "К" из найденного "KEGE"
        index_of_kegE.append(i + 3)  # Записываем в массив индекс второй буквы "Е" из найденного "KEGE"
max = 0  # переменная для запоминания максимальной длинны подходящей цепочки a.k.a. ответ

if len(index_of_kegE) < 3:  # Если в нашей последовательности менее трёх последовательностей "KEGE",
    # то ответом является длинна всей последовательности
    max = len(s)  # Присваиваем ответу значение длинны всей строки

else:  # Иначе находим максимальную длинну подоходящей последовательности
    for j in range(len(index_of_Kege) - 3):
        if (x := index_of_kegE[j + 3] - index_of_Kege[j] - 1) > max:  # Максимальная разница между индексами "К" и "Е"
            # через две последовательности "КЕGE" является ответом
            # Запоминаем текущую разницу во временную переменную x
            max = x  # Присваиваем макимальной длинне значение большей разницы

print(max)  # Выводим ответ

s = input()
a = s.replace('**','^')
print(a)



#5
#100*2 - 33 + 2561//2 * 93-55**3

operations = ['^', '*', '/', '+', '-']
ans = 0

s = input()
i = 0

while i < len(s):
    if s[i] == operations[0]:
        for j in range(i+1, len(s)):
            st = s[i+1:j+1]
            if s[j] in operations:
                st = s[i + 1:j]
                break

        for j in range(i-1, -1, -1):
            osn = s[j:i]
            if s[j] in operations:
                osn = s[j+1:i]
                break
    print(osn)
    tmp = osn[::-1] + '^' + st
    s = s.replace(tmp, str(int(osn[::-1]) ** int(st)), 1)

    i += 1

print(osn, st)
''' # Не база (гробы) :)
'''
f = open('Задание_24__d0rb__d95d.txt')
a = f.readline()
alf ='abcdefghijklmnopkrstuvwxyz'
COUNT = [0]*26
for i in range(26):
    COUNT[i] = a.count(alf[i])
print(max(COUNT) - min(COUNT))


s = "8" * 125

while ("333" in s) or ("888" in s):
    if ("333" in s):
        s = s.replace("333", "8", 1)
    else:
        if ("888" in s):
            s = s.replace("888", "3", 1)


print(s)
''' # Бэбра 12
"""n = 100
for i in range(n):
    for j in range(n):
        for k in range(n):
            s = '0' + '1'*i + '2'*j + '3'*k
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '2302', 1)
                s = s.replace('02', '10', 1)
                s = s.replace('03', '201', 1)
            if s.count('1') == 58 and s.count('2') == 23 and s.count('3') == 15:
                print(j)""" # ГРОБ 12
"""a, maxim = open('12312312312313.txt').readline(), 0
while 'PP' in a: a = a.replace('PP', 'P P')
for i in a.split(" "): maxim = max(maxim, len(i))
print(maxim)""" # ЛайфХак

"""maxim = 0
c = 0
cd = 0
a = open('24.txt').readline()
for i in range(len(a)):
    j = 0
    if a[i] != 'D':
        c += 1
        maxim = max(maxim, c)
    elif cd == 0:
        cD = 1
        j = i
        c += 1
        maxim = max(maxim, c)
    elif cd == 1:
        c = i - j
        j = i
        maxim = max(maxim, c)
print(maxim)
""" # НЕРЕШЕННЫЙ ГРОБ !!!

    # 24 ВСЕ ПРОТОТИПЫ
"""a = open('ege-inf-demo-2020-z24.txt').readline()
c = 1
maxim = 1
for i in range(len(a) - 1):
    if a[i] != a[i+1]:
        c += 1
    else:
        maxim = max(maxim, c)
        c = 1
print(maxim)"""  # 24.1  макс кол-во подряд разных
"""a = open('ege-inf-demo-2020-z24.txt').readline()
ans = 1
c = 1
for i in range(len(a) - 1):
    if a[i] == a[i+1]:
        c += 1
    else:
        ans = max(ans, c)
        c = 1
print(ans)"""  # 24.2  мак кол-во подряд идующих
"""f = open('24-z3.txt')
a = f.readlines()
c = 0
for i in range(len(a)):
    if a[i].count('A') > a[i].count('B'):
        c += 1
print(c) 
"""  # 24.3  кол-во строк, где A больше B
"""s = open('ege-inf-jobs-23112020-zad24.txt').readline()
a = []
for i in range(1, len(s) - 1):
    if s[i-1] < s[i] > s[i+1]:
        a.append(i)

maxim = 0
for i in range(len(a) - 1):
    maxim = max(maxim, a[i+1] - a[i])
print(maxim)"""  # 24.4  Локал. макс символ - номер которого больше номера предыдущего и последующего символа. Найти макс r между двумя соседними л.м.
"""
    # 1 способ
# Теория
# d = dict()
# d['J'] = 1
# d['B'] = 3
# print(d) >>> {'J': 1, 'B': 3}
# char = max(d, key = d.get)
# print(char) >>> B

a = open('24-z4.txt').readline()
d = dict()
for i in range(len(a) - 1):
    if a[i] == 'B' and a[i+1] != 'B':
        if a[i+1] not in d:
            d[a[i+1]] = 1
        else:
            d[a[i + 1]] += 1
char = max(d, key=d.get)
print(char)


    # 2 способ
s = [0]*26
for i in range(len(a) - 1):
    if a[i] == 'B' and a[i + 1] != 'B':
        s[ord(a[i+1]) - 65] += 1
maxim = 0
char = 0
for i in range(len(s)):
    if s[i] > maxim:
        maxim = s[i]
        char = i
print(chr(char + 65))
"""  # 24.5  Символ, который чаще всего встречается после 'B'
"""a = open('скобочкидля24.txt').readline()
c = 0
for i in range(len(a) - 1):
    if a[i] == '(' and a[i+1] == ')':
        c += 1
    if c == 10000:
        print(i+1)
        break
# 40451"""  # 24.6  Индекс 10000-ой пары скобок "()"
"""a = open('24.7.txt').readline()
c = 0
maxim = 0
for i in range(len(a)):
    #if a[i] == 'A' or a[i] == 'B' or a[i] == 'C':  <--- тупой способ
    if a[i] in 'ABC':
        c += 1
    else:
        maxim = max(maxim, c)
        c = 0
print(maxim)"""  # 24.7  макс длина подцепочки, состоящей из A, B или C (в любом порядке)
"""a = open('24-8.txt').readline()
c, ans = 0, 0
for i in range(len(a)):
    if a[i] != 'D':
        c += 1
    else:
        ans = max(ans, c)
        c = 0
print(ans)"""  # 24.8  макс длина цепочки, не содержащей D
"""a = open('24-9.txt').readline()
c = 0
ans = 0
for i in range(len(a)):
    if a[i] not in 'AE':
        c += 1
    else:
        ans = max(ans, c)
        c = 0
print(ans)"""  # 24.9  макс длина цепочики, не содержащей гласных букв 'AE'
"""f = open('input.txt')
a = f.readline()
dict = {}
for i in range(1, len(a) - 1):
    if a[i - 1] == 'X' and a[i + 1] == 'Z':
        if a[i] not in dict:
            dict[a[i]] = 1
        else:
            dict[a[i]] += 1
ans = max(dict, key=dict.get)
print(ans, dict[ans], sep='')

f.close()
"""  # 24.10 X*Y Наибольше встречаемый
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
print(m)"""  # 24.11 X + XYZ + XYZ + Z макс длина
"""a = [i.rstrip() for i in open('24 (17).txt')]

m = 0
c = 0
for i in a:
    s = set(i)
    for j in s:
        t = i
        t = t.split(j)[1:-1]
        for l in t:
            if l.count('R') < 30 and j not in l:
                c += 1
                m = max(m, len(l)+1)
print(m, c)"""  # 24.12 INFORMATIKA

a = open('24 (6).txt').readline()
c = 0
dict = {}
for i in range(len(a) - 4):
    if a[i] == 'C' and a[i+1] == 'A' and a[i+4] == 'C' and a[i+3] == 'A':
        if a[i+2] not in ['A', 'B', 'F']:
            c += 1
            if a[i+2] not in dict:
                dict[a[i+2]] = 1
            else:
                dict[a[i + 2]] += 1
print(c, dict)




f = open('zxc.txt')

ans = 0
for string in f:
    mass = [1000000000000] * 100
    if string.count('E') < 20:
        for j in range(len(string)):
            ans = max(ans, j - mass[ord(string[j]) - 65])
            mass[ord(string[j]) - 65] = min(mass[ord(string[j]) - 65], j)
print(ans)  # 24



# print(sum(1 for i in open('24__kglo__ki74.txt').readline().split('A')[1:-1] if len(i) >= 10 and i.count('B') >= 2))

