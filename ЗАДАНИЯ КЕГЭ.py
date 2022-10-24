"""def is_prime(n):
    for i in (2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
for i in [g for g in range(80) if is_prime(g)]:
    print(i)""" # Генератор простых чисел
"""maxim = -10e16
minim = 10e16
for x in range(1, 200):
    for y in range(1, 200):
        summ = 0
        num = (3 + 2 * 4**x) * 4 ** x + 3 + 4 ** y
        while num > 0:
            summ += num % 4
            num //= 4
        maxim = max(maxim, summ)
        minim = min(maxim, summ)
print(maxim, minim)
""" # 5 Задаnие
'''
        #КЕГЭ
    #фишки 27 задачи с двумя числами в первой строчке (в файле)
f = open('27_1.txt')
n,x = [int(i) for i in f.readline().split()] #считали первые два числа
print(n,x)
a = [int(i) for i in f] считываем оставшиеся, так как мы считали первые два, то они не будут считываться повторно
''' # LifeHack
"""#может понадобиться (для 17 или даже 27)
#a = [int(i) for i in f] - имба для 17 задачи (ввод всех элементов в массив)
# n чисел. Вывести max произведение двух подряд идущих чисел
n = int(input())
prev = int(input())
max = 0
for i in range(n-1):
    x = int(input())
    if x*prev>max:
        max = prev*x
    prev = max
print(max)

# n чисел. Вывести max произведение двух чисел.
n = int(input())
max1 = 0
max2 = 0
for i in range(n-1):
    x = int(input())
    if x>max1:
        max2 = max1
        max1 = x
    elif x>max2:
        max2 = x
print(max1*max2)""" # lifehack

#проверка на полиндромность
#if s == s[::-1]


"""
a =('1'*50)+('2'*100)+'3'
print(a)
c = a.count("3")
print(c)
while ('12' in a) or ('13' in a) or ('3333' in a):
    if ("23" in a):
        a=a.replace('23','3',1)
    elif("13" in a):
        a=a.replace('13','33',1)
    elif ("333" in a):
        a = a.replace('333', '3',1)
print(a)""" # Задание 12
'''#типичное 14 задание КЕГЭ на нахождение чисел в какой-то сс
a = 16**20+2**30-32
count = 0
while a>0:
    if a%4==3:
        count+=1
    a//=4
print(count)


for i in range(2,36):
    x = 93
    A = []
    while x > 0:
        ge = x%i
        x //=i
        A.append(ge)
    A = list(reversed(A))
    if len(A) >= 3 and int(A[-1]) % 10 == 2:
        print(A,i)     
''' # Задание 14
"""print((str(hex(3 * 4**38 + 2 * 4**23 + 4**20 + 3 * 4**5 + 2*4**4 + 1)[2:])).count('0'))

print(f'{3 * 4**38 + 2 * 4**23 + 4**20 + 3 * 4**5 + 2*4**4 + 1:x}'.count('0'))""" # Супер ЛайфХак для 14
"""
#15
for A in range(1,100):
    GG = True
    for x in range(1,100):
        if (((x&29!=0) and (x&18!=0)) <= ((x&A!=0) and (x&29!=0))) == 0:
            GG = False
    if(GG == True):
        print(A)
#otvet >>> 18""" # побитовое 15 КЕГЭ
"""
def F(n):
    if (n<=3):
        return n
    if (n==4):
        return 3
    return F(n-4)+F(n-3)+n

from functools import lru_cache
@lru_cache(None)
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

for i in range(10000):
    print(fibo(i))

from functools import lru_cache
@lru_cache(None)
def fact(n):
    if n == 0:
        return 1
    return fact(n-1) * n
for i in range(1, 10000):
    print(f'Факториал числа {i}! >>> {fact(i)}')

print(F(17))""" # Задание 16 КЕГЭ
"""
f = open('17__7n8u.txt')
n = 20000 #находим через x=f.readlines() , print(len(x))
a = []
c = 0
max = -10000000000
for i in range(n):
    a.append(int(f.readline()))

for i in range(n-1):
    if ((a[i]%6==0 or a[i]%7==0) and a[i]>1000)\
            or ((a[i+1]%6==0 or a[i+1]%7==0) and a[i+1]>1000) :
        c+=1
        if a[i]*a[i+1]>max:
            max = a[i]*a[i+1]
print(c,max)  #ВЕРНОЕ РЕШЕНИЕ!!!!!!!!!!!
#4754 97740230

# 17 с любым элементом (ВЛОЖ ЦИКЛ)
f = open('VAR_IZ_RESHUEGE.txt')
n = 10000
c = 0
maxim = -10000000000000
a = [int(i) for i in f]
for i in range(n):
    for j in range(i+1,n):
        t = a[i]+a[j]
        if t % 9 == 0:
            c+=1
            if t > maxim:
                maxim = t
print(c,maxim)
""" # Задание 17
"""# 17
n = int(input())
pref = [0] * n
ans = 1000000000000000000000000000
pref[0] = int(input())
if pref[0] % 2 == 1:
    ans = min(ans, pref[0])  # нужна минимальная сумма, чтоб потом вычесть её

for i in range(1, n):
    pref[i] = pref[i - 1] + int(input())
    if pref[i] % 2 == 1 and i != n - 1:
        ans = min(ans, pref[i])

if pref[-1] % 2 == 0:
    print(pref[-1])
else:
    print('BAD')
    print((pref[-1] - ans) if ans > 1000000000000 else -1)""" # ГРОБ !!!
"""
from functools import lru_cache
def moves(h):
    a,b = h
    return (a+1,b),(a,b+1),(a*4,b),(a,b*4)

@lru_cache(None)
def f(h):
    if(sum(h)>=82):
        return 'END'
    if(any(f(x) == 'END' for x in moves(h))):   #any - какой-то код
        return 'P1' #победа для первого хода Пети
    if(all(f(x)== "P1" for x in moves(h))):     #all - все ходы
        return 'V1'
    if(any(f(x) == 'V1' for x in moves(h))):
        return 'P2' #победа для второго хода Пети
    if(all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h))):
        return 'V2'

for s in range(1,100): #задание 19 П1
    h = 4,s
    print(s,f(h))
#ОТВЕТЫ:
#19 >>> 5
#20 >>> 1619
#21 >>> 18

#19-21
# 19-21
#19 - (16,s),>=58, minS P1 #ans >>> 21
#20 - WIN at starting position (11,17) #ans >>> 2(Vanya)
#21 - WIN at starting position (4,7) #ans >>> 2(Vanya)

from functools import lru_cache
def moves(h):
    a,b = h
    return (a+b,b),(a,a+b)

@lru_cache(None)
def f(h):
    if (sum(h)>=58):
        return 'END'
    if (any(f(x) == 'END' for x in moves(h))):
        return 'P1'
    if(all(f(x) == 'P1' for x in moves(h))):
        return 'V1'
    if (any(f(x) == 'V1' for x in moves(h))):
        return 'P2'
    if (all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h))):
        return 'V2'
    if(any(f(x) == 'V2' for x in moves(h))):
        return 'P3'
    if(all(f(x) == 'P1' or f(x) == 'P2' or f(x) == 'P3' for x in moves(h))):
        return 'V3'
#for 19
for s in range(1,100):
    h = 16,s
    print(s,f(h))

print()

#for 20-21
h = 1,17
print(f(h))

h = 4,7
print(f(h))""" # Задание 19-21

"""
#задание 23.1
#команды: +8, +1, *5
#сколько существует программ из 5 команд
#для которых при исходном числе 1 --> 98
#закодируем их: 0,1,2

def f(s,code):
    if code == 0:
        return s+8
    if code == 1:
        return s+1
    if code == 2:
        return s*5

c = 0
for x1 in range(3):
    for x2 in range(3):
        for x3 in range(3):
            for x4 in range(3):
                for x5 in range(3):
                    s = 1
                    s = f(s, x1)
                    s = f(s, x2)
                    s = f(s, x3)
                    s = f(s, x4)
                    s = f(s, x5)
                    if s == 98:
                        c+=1
print(c)

# Задание 23.2
# от 26 до 5 -1 или -2
def f(start,finish):
    if start == finish:
        return 1
    if start < finish:
        return 0
    if start == 14 or start == 21:
        return 0

    return f(start-1,finish)+f(start-2,finish)

print(f(26,5))

# Задание 23.3
# можем сделать обратное решение --> от 5 до 26 +1 +2
# Динамический алгоритм
a = [0]*100
a[5] = 1
for i in range(6,27):
    a[i] = a[i-1] + a[i-2]
    if i == 14 and i == 21:
        a[i] = 0
print(a[26])""" # Задание 23
"""
a, maxim = open('12312312312313.txt').readline(), 0
while 'PP' in a: a = a.replace('PP', 'P P')
for i in a.split(" "): maxim = max(maxim, len(i))
print(maxim)""" # Лайфхак для 24
"""
c = 0
for i in range(84684,84741):
    a = [int(x) for x in str(i)] #цифры числа в массив
    b = a[0]+a[1]+a[2]+a[3]+a[4]
    if i%b ==0:
        print(i)""" # 25.1
"""#25.2
# Числа Армстронга >>> n-значное число == сумме элементов числа ^n
# примеры: 153 = 1^3 + 5^3 + 3^3, 1634 = 1^4 + 6^4 + 3^4 + 4^4
def is_armstrong(n):
    if(summa_cyfr_v_stepeni(n,len(str(n))) == n):
        return True
    return False
def summa_cyfr_v_stepeni(n,k):
    a = [int(x)**k for x in str(n)]
    return sum(a)
for i in range(1500,9501):
    if(is_armstrong(i)):
        print(i,end=", ")
#1634, 8208, 9474""" # 25.2 Числа Армстронга
"""    
def divs(n):
    div = []  # Массив делителей
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            div.append(i)
            if i != n // i:
                div.append(n // i)
    return div


def is_prime(n):
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            return False
    return True


def is_sqrt_prime(n):
    if int(n ** 0.5) ** 2 == n and is_prime(int(n ** 0.5)):
        return True
    return False


def count_sqrt_divs(n):
    counter = 0
    for i in divs(n):
        if is_sqrt_prime(i):
            counter += 1
    return counter


a = 20211209  # Задаю границы цикла
b = 20220126
ans = 0  # Будущий ответ
for i in range(a, b + 1):
    if count_sqrt_divs(i) == 3:
        ans += 1
print(ans)




# Заметим, что 7 нечетных делителей имеют числа вида (p**6) * (2**x), где p - простое число,
# а x - любое целое неотрицаельное
left = 1000  # Задаю границы цикла
right = 123456789
ans = 0  # Будущий ответ
simple = [True] * (int(right ** (1 / 6)) + 1)
numbers = []
# Найдем все простые числа, которые меньше корня 6 степени от правой границы
for i in range(2, len(simple)):
    if simple[i]:
        numbers.append(i)
        for j in range(i + i, len(simple), i):
            simple[j] = False

numbers = numbers[1:]  # исключим двойку, ведь число вида (p**6) * (2**x) при p=2
# не имеет нечетных делителей, кроме 1

for number in numbers:
    x = 0
    while number ** 6 * 2 ** x <= right:  # переберем все варианты 2**x
        if left <= number ** 6 * 2 ** x <= right:
            ans += 1
        x += 1

print(ans)
""" # ГРОБЫ 25 (см. файл с 25 там все топ расписано)
"""
#27.1
#неэффективная программа
f = open("Задание_27В__9p3n.txt")
n = 79000
a = []
for i in range(n):
    a.append(int(f.readline()))

max = 0
for i in range(n):
    for j in range(i+1,n):
        if (a[i]%14==0) or (a[j]%14==0):
            if ((a[i]-a[j])%2==0):
                if (a[i]+a[j])>max:
                    max = a[i]+a[j]
print(max)

#полурабочая прога:
#A >>> 11976
#B >>> 19994

#27.2 ЭФФЕКТИВНАЯ
f = open('Задание_27B__9va4.txt')
#x = f.readlines()
n = int(f.readline())
a = []
k3,k13,k39=0,0,0
nk = 0
ans = 0
for i in range(n):
    x = int(f.readline())
    a.append(x)
    if x%39==0:
        ans+= k39+k13+k3+nk
        k39+=1
    elif x%13==0:
        ans+= k3+k39
        k13+=1
    elif x%3==0:
        ans+= k13+k39
        k3+=1
    else:
        ans+=k39
        nk+=1
print(ans)

# 27.3 ЭФФЕКТИВНАЯ
#пары чисел
# нужно выбрать такие числа, чтоб сумма всех выбранных не делилась на 23 и при этом была максимально возможной
# динамический алгоритм
f = open('Задание_27-B__apwy.txt')
n = int(f.readline()) #первое число в файле (количество пар)
s = 0
md = 1000000000000000
for i in range(n):
    a,b = [int(s) for s in f.readline().split()] #каждый символ в строчке, через пробел засовываем в a,b
    s += max(a,b) #добавляем максимальное число из пары в "сумму выбранных (S)"
    diff = abs(a-b)
    if diff %23 != 0:
        if diff < md:
            md = diff
if s%23 != 0:
    print(s)
else:
    print(s - md)

#A - 127352
#B - 399762769

#27.4 ЭФФЕКТИВНАЯ ЦЕПИ
# 7
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

print(abs(maxim - minim))""" # Что-то из 27
























