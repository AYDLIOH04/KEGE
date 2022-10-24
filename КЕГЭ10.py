'''
#4
for i in range(-100,100):
    s = i
    n = 4096
    while s < 149 :
        s = s + 9
        n = n // 2
    if n == 4:
        print(i)

#12
a = '1'*50 + '2'*100 +'3'
while ('12' in a) or ('23' in a) or ('33333' in a):
    if ('12' in a):
        a = a.replace('12','2',1)
    elif ('23' in a):
        a = a.replace('23', '33', 1)
    elif ('333' in a):
        a = a.replace('333', '3', 1)
print(a)

#14
c = 0
a = 729**113 + 81**200 - 9**156 - 191
while a>0:
    if a%9 == 8:
        c+=1
    a//=9
print(c)
v
#15
for A in range(-100,100):
    GG = True
    for x in range(1,100):
        for y in range(1, 100):
            if ((x<A) or (y <= A) or ((x*y)%2 == 0) or ((x*y)>= 100)) == False:
                GG = False
                break
        if GG == False:
            break
    if GG == True:
        print(A)

#16
def f(n):
    if n <= 1:
        return 1
    if n % 2 == 0:
        return n + f(n-1)
    return n*n + f(n-2)

print(f(80))

#17
f = open('Задание_17__ahsu.txt')
n = 1000000
c = 0
max = 0
a = [int(i) for i in f]
for i in range(n-1):
    if (a[i] + a[i+1])%10 == 5 and (a[i] + a[i+1])%35 == 0:
        c+=1
        if (a[i]*a[i+1])%10 == 0 and (a[i]*a[i+1]) > max:
            max = (a[i]*a[i+1])
print(c,max)

#19

from functools import lru_cache
def moves(h):
    return h+1, h*3

@lru_cache()
def f(h):
    if h>=93:
        return 'END'
    if (any(f(x) == 'END' for x in moves(h))):
        return 'P1'
    if (all(f(x) == 'P1' for x in moves(h))):
        return 'V1'
    if (any(f(x) == 'V1' for x in moves(h))):
        return 'P2'
    if (all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h))):
        return 'V2'
for s in range(1,100):
    print(s,f(s))

#22
for i in range(1,10000000000):
    x = i
    a = 53
    b = 1
    while x > 0:
        a = a - 13
        b = b * (x % 155)
        x = x//155
    if a == 1 and b == 1:
        print(i)

#23.1
def f(start,finish):
    if start == finish:
        return 1
    if start < finish:
        return 0
    if start == 14 or start == 21:
        return 0

    return f(start-1,finish)+f(start-2,finish)

print(f(26,5))
# Задание 23.2
# от 26 до 5 -1 или -2
# можем сделать обратное решение --> от 5 до 26 +1 +2
# Динамический алгоритм
a = [0]*100
a[5] = 1
for i in range(6,27):
    a[i] = a[i-1] + a[i-2]
    if i == 14 and i == 21:
        a[i] = 0
print(a[26])


#25
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
        print(i,end=", ") # типо из условия надо через запятую вставить

# 1634, 8208, 9474
'''
'''
f = open('Задание_26__apww.txt')
a = [int(i) for i in f]
a.pop(0) #чтоб удалить первый симвл
n = len(a)
#print(a)
#print(n) #без удаления было 9301 (т.е. бралось первое число из файла9300)
'''
# 27
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