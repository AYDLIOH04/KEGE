
    # Самое важное
'''
# ПРОВЕРКА НА ПРОСТОТУ
def is_prime(n):
    for j in range(2,int(n**0.5)+1):
        if n%j == 0:
            return False
    return True

# ПОИСК ВСЕХ ДЕЛИТЕЛЕЙ
def find_div(n):
    divs = []
    for j in range(1,int(n**0.5)+1):
        if n%j == 0:
            divs.append(j)
            if j != n // j:
               divs.append(n//j)
    divs.sort()
    return divs

# КОЛИЧЕСТВО ДЕЛИТЕЛЕЙ ЧИСЛА
def count_div(n):
    c = 0
    for i in range(1,int(n**0.5) + 1):
        if n%i == 0:
            c+=1
            if i != n//i:
                c+=1
    return c

# ОБЪЕДИНЕННАЯ ШТУКА count+find (ОТ ПАВЛИКА), BUT THIS SHNYAGA IS TRASH, DONT USE IT
def union(n):
    c = 0
    divs = []
    for i in range(1,int(n**0.5) + 1):
        if n%i == 0:
            divs.append(i)
            c+=1
            if i != n//i:
                divs.append(n//i)
                c+=1
    divs.sort()
    if c == 2:
        return n,'ПРОСТОЕ ЧИСЛО     ',divs,c
    return n,'СОСТАВНОЕ',divs,c
'''  # is_prime, find_div, count_div
"""
def erato(n):
    massiv = list(range(n+1))
    massiv[1] = 0
    for i in massiv:
        if i > 1:
            for j in range(i*i, len(massiv), i):
                massiv[j] = 0
    massiv = [k for k in massiv if k != 0]
    return massiv
"""  # Решето Ератосфена
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
    return ans"""  # Разложение на множители по ОТА

# УДОБНАЯ ОПТИМИЗАЦИЯ
def div(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d |= {i, n//i}
    return sorted(d)


import time

"""def resheto(n):
    l = []
    for i in range(n+1):
        l.append(True) # l[0] ... l[n] = True
    l[0] = False
    l[1] = False # 0, 1 - не простые числа, поэтому делаем их False
    for i in range(2, n+1): # проверяем диапазон от 2 до n
        if (l[i]): # если True -> незачеркнутый -> i - простое число
            for j in range(i*i, n+1, i): # от i^2 до n начинаем вычеркивать с шагом i
                l[j] = False # i*i, i*i+i, i*i+2i, i*i+3i - все различаются на i

    ans = [] #массив простых чисел, который вернет функция
    for i in range(n+1):
        if (l[i]): # если так и не зачеркнули, то i простое
            ans.append(i) # сщхраняем простое число в массив

    return ans

print(resheto(50))"""  # Решето Эратосфена - алгоритм, находящий все простые числа на отрезке от 2 до n. Быстро

def timer(func):
    import time
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return wrapper

'''
# EXC 1 >>> find and print the first five numbers, large 100 000 000,
# in which the number of divisors is more than 5 and
# the first three divisors sums dont exceed 100 in total
k = 0
for i in range(100000001,200000000):
    if count_div(i) >= 5:
        d = find_div(i)
        if d[0]+d[1]+d[2] <= 100:
            print(i)
            k+=1
        if k == 5:
            break

'''  # Что-то на испанском
'''
# Задание 2 >>> Пусть M (N) – произведение 5 наименьших различных натуральных
# делителей натурального числа N, не считая единицы. Если у числа N меньше
# 5 таких делителей, то M (N) считается равным нулю.
# Найдите 5 наименьших натуральных чисел, превышающих 200 000 000, для
# которых 0 < M (N) < N.
# В ответе запишите найденные значения M (N) в порядке возрастания
# соответствующих им чисел N

#МОЕ РЕШЕНИЕ
k = 0
for n in range(200000001,600000000):
    if count_div(n) >= 5:
        d = find_div(n)
        MN = 1
        for i in range(1,6):
            MN *= d[i]
        if 0 < MN < n:
            print(MN)
            k += 1
            if k == 5:
                break

#РЕШЕНИЕ АРа
def M(n):
    if count_div(n) < 5:
        return 0
    a = find_div(n)
    MN = 1
    for i in range(1,6):
        MN *= a[i]
    return MN

k = 0
for n in range(200000001,500000000):
    if 0 < M(n) < n:
        k+=1
        print(M(n))
        if k == 5:
            break
'''  # Найдите 5 наименьших натуральных чисел, превышающих 200 000 000, для которых 0 < M (N) < N.
'''
# задача 3 >>> найти на промежутке от 100млн до 200млн количетсво чисел, у которых ровно 5 делителей
def count_div(n):
    c = 0
    for i in range(1,int(n**0.5) + 1):
        if n%i == 0:
            c+=1
            if i != n//i:
                c+=1
    return c


#сначала запустим от 1 до 1000 и посмотрим
k = 0
for n in range(1,1000):
    if count_div(n) == 5:
        k+=1
        print(n)
#хм, это что числа в 4 степени????


# при обычных условиях range(10**8,2*(10**8)) пол жизни будет считать
# поэтому, исходя из вывода сверху, берем их корни
# тем самым увеличиваем скороть программы в ДЕСЯТЬ ТЫСЯЧ РАЗ

k = 0
for n in range(int(100000000**0.5), int(200000000**0.5) + 1):
    x = n*n
    if count_div(x) == 5:
        k+=1
        print(x)
print(k)
'''  # Найти на промежутке от 100млн до 200млн количетсво чисел, у которых ровно 5 делителей
'''
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
#1634, 8208, 9474
'''  # Числа Армстронга
'''
#25
def find_divs(n):
    divs = []
    for j in range(1,int(n**0.5)+1):
        if n % j == 0:
            divs.append(j)
            if j != n//j:
                divs.append(n//j)
    divs.sort()
    return divs

# M = maxDEL + minDEL #esli net, to 0
c = 0
for i in range(700001,1000000):
    if len(find_divs(i)) > 2:
        a = find_divs(i)[-2]
        b = find_divs(i)[1]
        M = a + b
        if M % 10 == 8:
            c+=1
            print(i,M)
        if c == 5:
            break
# 700005 233338
# 700007 100008
# 700012 350008
# 700015 140008
# 700031 24168
'''  # range(700001,1000000) больше 2 делителей, M = maxDEL + minDEL #esli net, to 0. M % 10 == 8, c == 5

'''
#1
def count_div(a):
    c = 0
    for i in range(1,int(a**0.5) + 1):
        if a % i == 0:
            c+=1
            if i != a//i:
                c+=1
    return c

for i in range(300000,333000):
    if count_div(i) == 3:
        print(i)




def count_find_div(a):
    arr = []
    for i in range(1,int(a**0.5)+1):
        if a % i == 0:
            arr.append(i)
            if i != a//i:
                arr.append(a//i)
    arr.sort()
    c = 0
    for i in arr:
        if i % 2 != 0:
            c+=1
    return c

for i in range(88535,153373+1):
    if count_find_div(i) == 5:
        print(i)




def count_dif(n):
    c = 0
    for i in range(1,int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 != 0:
                c+=1
            if n//i % 2 != 0:
                if i != n//i:
                    c+=1
    return c

for i in range(88535,153373+1):
    if count_dif(i) == 5:
        print(i)





def find_div(n):
    arr = []
    for i in range(1,int(n**0.5) +1):
        if n % i == 0:
            if i % 2 != 0:
                arr.append(i)
            if n//i % 2 != 0:
                if i != n//i:
                    arr.append(n//i)
    arr.sort()
    arr.reverse()
    return arr
for i in range(198374,295381):
    if len(find_div(i)) == 7:
        print((find_div(i)))





def count_div(n):
    c = 0
    for i in range(1,int(n**0.5) + 1):
        if n % i == 0:
            c+=1
            if i != n//i:
                c+=1
    return c

count = 0
for i in range(100100,300300):
    if count_div(i) - 2 == 3:
        count +=1
print(count)




def count_div(n):
    c = 0
    for i in range(1,int(n**0.5) + 1):
        if n % i == 0:
            c+=1
            if i != n//i:
                c+=1
    return c

maxNUM = -100000000000000000
maxDEL = -100000000000000000
for i in range(231893,251859+1):
    if count_div(i) >= maxDEL:
        maxDEL = count_div(i)
        if i > maxNUM:
            maxNUM = i
print(maxDEL,maxNUM)




def is_prime(n):
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

c = 0
for i in range(55556,55776+1):
    if is_prime(i):
        c+=1
print(c)




n = int(input())
c = 0
for i in range(1,int(n**0.5) + 1):
    if n % i == 0:
        c+=1
        if i != n//i:
            c+=1
print(c)




def is_prime(n):
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

c,maxim = 0,-100000000
for i in range(100,100100 + 1):
    if is_prime(i):
        c+=1
        maxim = max(i,maxim)
print(c,maxim)




def count_div(n):
    c = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            c += 1
            if i != n // i:
                c += 1
    return c

maxDEL, minNUM = -10000000000000000000, 100000000000000000000000
arr = []
for i in range(591645, 592845+1):
    if count_div(i) >= maxDEL:
        maxDEL = count_div(i)
for i in range(591645, 592845+1):
    if count_div(i) == maxDEL:
        arr.append(i)
print(arr)




def find_div(n):
    arr = []
    for i in range(1,int(n**0.5) + 1):
        if n % i == 0:
            arr.append(i)
            if i != n//i:
                arr.append(n//i)
    return arr

def palindrom(n):
    n = str(n)
    if len(n) > 1:
        if n == n[::-1]:
            return True
    return False

c = 0
for i in range(12345,12425):
    OKAY = [palindrom(k) for k in find_div(i)]
    if any(OKAY):
        c+=1
print(c)




def chislo_palindrom(n) :
    n = str(n)
    if n == n[::-1]:
        return True
    return False

a = 12345
b = 12425
c = 0
for i in range(a, b + 1):
    maxim = 0
    for j in range(10, i + 1):
        if(i % j == 0) :
            if(chislo_palindrom(j)) :
                maxim = j
    if maxim != 0:
        print(i,maxim)
        c+=1
print(c)




def count_div(n):
    counter = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            counter += 1
            if i != n // i:
                counter += 1
    return counter


a = 111111
b = 777777
maxim = -10000000000
ans = 0
for i in range(a, b + 1):
    if count_div(i) >= maxim:
        maxim = count_div(i)
        ans = i
print(ans)
'''  # DZ Тут очень много задачек

'''
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


# Заметим, что 7 нечетных делителей имеют числа вида (p^6) * (2^x), где p - простое число,
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
'''  # Сложные 25
'''
def resheto(n):
    is_prime = [True]*(n+1)
    is_prime[0] = False
    is_prime[0] = False

    for i in range(2,n+1):
        if is_prime[i]:
            for j in range(i,n//i + 1):
                is_prime[i*j] = False

    ans = []
    for i in range(n+1):
        if is_prime[i]:
            ans.append(i)
    return ans
'''  # Решето Эратосфена

'''
#25
# Можно оптимизировать перебор делитилей на простоту с помощью лру_кашэ
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
'''  # M - целая часть от ср.арифм всех простых делителей числа. От 420000 если M % 42 == 24. Вывести первые 5 чисел
'''
def div(n):
    c = []
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            c.append(i)
            if i != n//i:
                c.append(n//i)
    c.sort()
    if len(c) == 0:
        return 0
    return (c[0] + c[-1])
for i in range(700000,702000):
    if div(i) % 10 == 8:
        print(i, div(i))
'''  # M - minDEL + maxDEL тривиальные >700000, M % 10 == 8. Первые 5 таких чисел и их значение

"""def S(n):
    divs = []
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            divs.append(j)
            if n//j != j:
                divs.append(n//j)
    divs.sort()
    if len(divs) < 3:
        return 0
    else:
        return divs[-1] + divs[-2] + divs[-3]


def nevozrast(n): # невозрастание = убывание
    a = [int(k) for k in str(n)]
    for i in range(len(a) - 1):
        if a[i+1] > a[i]:
            return False
    return True

c = 0
for n in range(10000001, 20000000):
    if nevozrast(S(n)) and S(n) > 0:
        print(S(n), n)
        c += 1
        if c == 5:
            break
# 8753332 10003808
# 8432221 10004330
# 8754221 10004824
# 8754431 10005064
# 999761 10005127
"""  # S(n) - сумма трех наиб. нетрив. делителей n. Если <3 делителей: S(n) = 0. Найти 5 min > 10млн для которых S(n) в порядке невозрастания. Записать S(n) и соот числа n


# ГРОБЫ ===============================================================================================================

"""    # Фан-Факт, который решает задачку >>>
# Если x имеет 7  нечетных делителей, то:
# x = p^k1 * p^k2 * p^k3 * ... * p^kn
# Количество делитилей числа x = (k1 + 1) * (k2 + 1) * (k3 + 1) *... * (kn + 1) = 7 (по усл)     ФОРМУЛА!!! ЗАПОМИНАЕМ!!!
# 7 - простое число => k1, k2, k3 ,...,kn = 1,      КРОМЕ ОДНОГО ЧИСЛА 7 !!!
# 1 * 1 * 1 * 7 * 1 * 1 * 1 =>   т.к. (kn + 1) = 7, то kn = 6
# x = p^0 * p^0 * ... * p^6 * ... * p^0 = p^6
# ОПАА ВСЕЕ!!! >>>  БЕРЕБИРАЕМ ВСЕ ПРОСТЫЕ ЧИСЛА p^6 до b ** (1/6) (правой границы)

a = 1000
b = 123456789

c = 0
for i in [3, 5, 7, 11, 13, 17, 19, 23, 29]: # Перебираем все первые делители (КРОМЕ ДВОЙКИ !!!)
    x = i ** 6
    while x <= b:
        if x >= a:
            c += 1
        x = x * 2
print(c)
# 58"""  # Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку
                # [1000; 123456789], числа, имеющие ровно 7 нечетных делителей. Программа должна вывести количество таких чисел.
"""def count_div_nechet(n):
    c = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 != 0:
                c += 1
            if (n//i) % 2 != 0 and n//i != i:
                c += 1
    return c

def is_prime(n):
    for i in (2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

a = 35000000
b = 40000000

# b**(1/5) = 79.527
# НЕОБХОДИМ ГЕНЕРАТОР ПРОСТЫХ ЧИСЕЛ ДО 80
ans = []
for i in [g for g in range(80) if is_prime(g)]:
    x = i ** 4
    while x <= b:
        if x >= a:
            if count_div_nechet(x) == 5:
                ans.append(x)
        x = x * 2

ans.sort()
for i in ans:
    print(i)

# 35819648
# 38950081
# 39037448
# 39337984"""  # Найдите числа [35000000; 40000000] у которых ровно 5 нечетных делителей
"""
def count_div(n): # Функция - каунтер нечетных делителей
    c = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 != 0:
                c += 1
            if (n // i) % 2 != 0 and n // i != i:
                c += 1
    return c

def prime(n): # Функция - поиск простых чисел
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

a = 45000000
b = 50000000

ans = [] # Переберем простые числа до int(50000000 ** 0.25) умножая их на 2 в цикле while
for i in [j for j in range(1, 85) if prime(j)]: # генератор простых чисел для перебора
    x = i**4
    while x <= b:
        if x >= a:
            if count_div(x) == 5:
                ans.append(x)
        x = x * 2
ans.sort()
for i in ans:
    print(i)"""  # От 45млн до 50 млн 5 нечетных делителей
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
print(c, ans)"""  # [536792; 604298] числа, состоящие из 3 простых с одинаковой кратностью 10
# ====================================================================================================================



"""def prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def div(x, k = 0):
    ans = []
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            ans += [i]
            if i == x//i:
                ans += [x // i]
    return sorted(ans + [1, x]*k)

def count_div(x, k = 0):
    ans = 0
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            ans += 1
            if i != x // i:
                ans += 1
    return ans + 2*k

for i in range(200000, 500000+1):
    if count_div(i, 1) >= 5:
        print(i, sum(div(i)))
"""  # Найти все числа на отрезке [200000, 500000], имеющие хотя бы 5 делителей включая тривиальные. Выведите сами числа на экран, а также сумму их нетривиальных делителей.
"""def prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

ans = 0

for i in range(2, 20000+1):
    if prime(i):
        if 100 <= i ** 2 <= 100100100:
            ans += 1
print(ans)"""  # Найти все числа на отрезке [100, 100100100], имеющие ровно 3 делителя.
"""def prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

ans = 0

for i in range(3, int(100100100**0.25)+1):
    if prime(i):
        t = 0
        while 2**t * i**4 <= 100100100:
            if 100 <= 2 ** t * i ** 4:
                ans += 1
            t += 1
print(ans)
"""  # Найти все числа на отрезке [100, 100100100], имеющие ровно 5 нечетных делителя.
"""def prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

ans = 0

for i in range(3, int(100100100**0.25)+1):
    if prime(i):
        if 100 <= 2 * i**4 <= 100100100:
            ans += 1
print(ans)"""  # Найти все числа на отрезке [100, 100100100], имеющие ровно 5 четных делителя.
"""def num(x):
    ans = []
    while x > 0:
        ans += [x % 10]
        x //= 10
    return sum(ans[::-1])

def prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

ans = 0

for i in range(150000, 450000+1):
    if i % 5 == 0 and prime(num(i)):
        ans += 1

print(ans)"""  # Дан отрезок чисел [150000, 450000]. Требуется найти количество чисел, сумма цифр которых проста и при этом хотя бы один нетривиальный делитель самого числа кратен 5.
"""def count_div(x):
    ans = []
    count = 0
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            if i % 5 == 0:
                count += 1
            ans.append(i)
            if i != x//i:
                if x//i % 5 == 0:
                    count += 1
                ans.append(x//i)

        if count > 3:
            return False

    if count == 3:
        ans = sorted(ans + [1, x])
        for i in range(len(ans)-1, -1, -1):
            if ans[i] % 5 != 0:
                return ans[i]

    else:
        return False

for i in range(750000, 1450000+1):
    k = count_div(i)
    if k:
        print(i, k)"""  # Дан отрезок чисел [750000, 1450000]. Требуется найти числа, у которых ровно 3 нетривиальных делителя, кратных 5. Выведите на экран сами числа, а также наибольший любой делитель числа, некратный 5.
"""def din(x):
    ans = []
    i = 2
    while i < int(x ** 0.5)+1 and x > 0:
        if x % i == 0:
            ans.append(i)
            ans.append(x//i)
            x //= i
        i += 1
    return set(ans)

def div(x):
    ans = []
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            ans += [i]
            if i == x//i:
                ans += [x // i]
    return ans

import time
start = time.time()
for i in range(10000, 100000):
    div(i)
end = time.time()
print(format(end - start))"""

"""def count_div(n):
    c = 0
    maxim = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            c += 1
            maxim = max(maxim, i)
            if i != n//i:
                c += 1
                maxim = max(maxim, n//i)
    return c, maxim

for i in range(int(123456789 ** 0.25), int(223456789 ** 0.25) + 1): # Если перебирать до корня, то тоже посчитает
    x = i ** 4
    t = count_div(x)
    if t[0] == 3:
        print(t[1])"""  # [123456789; 223456789] и имеющие ровно три нетривиальных делителя
"""def count_div(n):
    c = 0
    maxim = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            c += 1
            maxim = max(maxim, i)
            if i != n//i:
                c += 1
                maxim = max(maxim, n//i)
    return c, maxim

for i in range(int(289123456 ** 0.25), int(389123456 ** 0.25) + 1): # Если перебирать до корня, то тоже посчитает
    x = i ** 4 
    if count_div(x)[0] == 3:
        print(x, count_div(x)[1])
# 294499921 2248091
# 352275361 2571353
# 373301041 2685619"""  # Ровно 3 нетривиальных на [289123456, 389123456]
"""def count_div(n):
    c = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                c += 1
            if i != n//i:
                if n//i % 2 == 0:
                    c += 1
    return c
a = (101000000 / 2) ** 0.5
b = (102000000 / 2) ** 0.5
for n in range(int(a), int(b) + 1):
    x = int(n ** 2 * 2)
    if count_div(x) == 3:
        print(x)
# 101075762
# 101417282
# 101588258
# 101645282
 """  # Ровно 3 различных ЧЕТНЫХ делителя на [101000000;102000000]
"""def count_div(n):
    c = 0
    for i in range(1,int(n**0.5) + 1):
        if n % i == 0:
            c += 1
            if i != n//i:
                c += 1
    return c

maxim = -10e16
ans = 0
for i in range(84052, 84130 + 1):
    if count_div(i) > maxim:
        maxim = count_div(i)
        ans = i
print(maxim, ans)
# 72 84084
"""  # макс кол-во делителей
"""def count_div(n):
    a = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            a.append(i)
            if i != n//i:
                a.append(n//i)
    a.sort()
    return a


a = 1234567
b = 7654321
aa = int(a**0.5) + 1
bb = int(b**0.5) + 1
c = 0
for i in range(1, bb):
    x = i*i
    if x % 3 != 0:                      # => Если x не делится на 4, то у него НЕТ НИ ОДНОГО ДЕЛИТЕЛЯ, КРАТНОГО ТРЕМ !!!!!!!!!!!!!!!!!
        arr_del = count_div(x)          # Еще один фан-факт: Сумма цифр числа кратна трем, только если само число кратно трем o_O (из признаком делимости на 3)
        if len(arr_del) == 7:           # Сэледовательно => Сумма цифр числа некратна трем, только если число некратно трем !!!
            while x <= b:
                if a <= x <= b:
                    c += 1
                    print(x)
                x = x * 3
print(c)"""  # ровно 7 делителей, некратных 3 (спойлер p**6 * 3**k)
"""def count_div(n):
    c = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i % 5 == 0:
                c += 1
            if n//i % 5 == 0 and i != n//i:
                c += 1
            if c > 5:
                return 0
    return c

for i in range(int((28916485//5)**0.25), int((49716586//5)**0.25)):
    x = 5 * (i**4)
    t = count_div(x)
    if t == 5:
        print(x)"""  # [28916485; 49716586] ровно 5 делителей, оканчивающихся на 0 или 5
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
        last = i"""  #
# Решето Эратосфена - алгоритм, находящий все простые числа на отрезке от 2 до n быстро
def resheto(n):
    l = []
    for i in range(n+1):
        l.append(True) # l[0] ... l[n] = True
    l[0] = False
    l[1] = False # 0, 1 - не простые числа, поэтому делаем их False
    for i in range(2, n+1): # проверяем диапазон от 2 до n
        if (i*i > n): # если зачеркивать нечего, то надо закончить цикл
            break
        if (l[i]): # если True -> незачеркнутый -> i - простое число
            for j in range(i*i, n+1, i): # от i^2 до n начинаем вычеркивать с шагом i
                l[j] = False # i*i, i*i+i, i*i+2i, i*i+3i - все различаются на i

    ans = [] #массив простых чисел, который вернет функция
    for i in range(n+1):
        if (l[i]): # если так и не зачеркнули, то i простое
            ans.append(i) # сщхраняем простое число в массив

    return ans  # Решето-1


