'''
#1
def f(n):
    if n == 0:
        return 3
    return f(n-1)+1

#2
def f(n):
    if n == 0:
        return 1
    return f(n-1)+f(n-1)

#3
def f(n):
    if n == 0 or n == 1:
        return 1
    return f(n-1)+f(n-2)

#4
def f(n):
    if n == 0 or n == 1:
        return n
    return f(n-2)-f(n-1)

#5
def f(n):
    if n < 3:
        return n
    return f(n-1)-f(n-1)

#6
def f(n):
    if n < 4:
        return n-1
    return f(n-1)//f(n-2)

#7
def f(n):
    if n > 50:
        return n//10
    return f(n+2)+f(n+3)

#8
def f(n):
    if n > 30:
        return  n
    return f(n+1)*f(n+2)

#9
def f(n):
    if n == 1:
        return 13
    return f(n-1)+5
print(f(100))

#10
def f(n):
    if n == 1:
        return 13
    return f(n-1)+5
print(f(100)+f(99)+f(98))
''' # EZ 16
'''
#6 >>> 776576776574
def f(n):
    if n < 8:
        f(n+2)
        f(n+1)
        f(n+3)
        print(n)
print(f(3))

#7 >>> 18
def f(n):
    if n > 3:
        f(n//2)
        print('LOX')
        f(n-2)
        print('LOX')
print(f(12))
#8 >>> 22
def f(n):
    print('LOX')
    if n > 4:
        f(n//3)
        f(n-2)
        f(n-4)
print(f(12))

#9 >>> 512
def f(n):
    if n == 1 or n == 2:
        return n
    return f(n-1)+f(n-1)*3
print(f(6))

#10 >>> 34
def f(n):
    if n == 1:
        return '**'
    if n == 2:
        return '***'
    return f(n-2)+f(n-1)
a = f(7)
arr2 = [i for i in a]
print(arr2)
print(arr2.count('*'))


#1 - модуль числа
def f(n):
    if n >= 0:
        return n
    return -n
n = int(input())
print(f(n))

#2
def f(n):
    if n > 5:
        return f(n-1)*f(n-1)
    elif 3<=n<=5:
        return f(n-2)+f(n-1)
    return 3
print(f(6))

#3
def f(n):
    return '*'*n
print(f(9))

#4
def f(n):
    if n == 1:
        return 'krabstvo'
    return f(n-1)+f(n-1)
print(f(3))

#5
#нет базы
#6
def f(n):
    if n == 10:
        return 10
    return f(n+1)+f(n+1)
print(f(7))

#7
def f(n):
    if n%3 == 0:
        return f(n-1)+f(n//3)
    if n > 2:
        return f(n-1)+f(n-2)
    return 2
print(f(8))

#8
def f(n):
    if n == 1:
        return 2
    return n+f(n-1)
print(f(5))

#9
def f(n):
    if n > 2:
        return f(n-2)*g(n-2)
    return 2
def g(n):
    if n == 1:
        return 1
    return g(n-1)+g(n-1)
print(f(6))


# 1
def larger(a,b):
    if a>=b:
        return True
    return False
# 2
def sum(a,b):
    return a+b

a,b = map(int,input().split())
print(larger(a,b), sum(a,b))

# 3
def last_num(a):
    return a%10

print(last_num(int(input())))

# 4
def mod_dif(a,b):
    if (a-b) < 0:
        return 'dif is >>>', (-1)*(a-b), 'and Max is >>>', b
    return 'dif is >>>', (a-b), ' and Max is >>>', a

a,b = map(int,input().split())
print(*(mod_dif(a,b)))

# 5
def arifm_progres(x,n,k): # n - число до, k - шаг
    if x >= n:
        return 0
    else:
        print(x)
        arifm_progres(x+k,n,k)

n,k = map(int,input().split())
print(arifm_progres(1,n,k))

# 6
def f(n): #факториал
    if n == 1:
        return 1
    return f(n-1)*n
print(f(6))

def f(x):
    return x*2

k = 1
for i in range(10):
    k = f(k)
print(k)

def f(x): #всегда выводит 0
    if x == 0:
        return 0
    if x>0:
        return f(0)

print(f(3))
print(f(-3)) #выведет None

def f(x):
    if x == 0:
        return 1
    if x > 0:
        return 2*f(x-1) #типо 10 раз вызовется и получится 1024 f(x) при x = 10
n = int(input())
print(f(n)) #сверху прога типо 2^n

''' # NORM 16
'''

# exc 1 >>> the SUM of the sequence from 1 to n (formula 1+2+...+n = n*(n+1)/2)

def sum(n):
    # INDUCTION BASE, without a base there will be a collapse
    if n == 1:
        return 1
    # TRANSITION INDUCTION
    return n+sum(n-1)

print(sum(10))

# exc 2 >>> 2^n

def degree(n):
    if n == 0:
        return 1
    return 2*degree(n-1)

n = int(input())
print(degree(n))

# exc 3 >>> n!

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

n = int(input())
print(fact(n))

# exc 4 >>> C_nk

def comb(n,k):
    #BASE
    if k == 0:
        return 1
    if k == n:
        return 1
    #TRANSITION
    return comb(n-1,k)+comb(n-1,k-1)

print(comb(5,2))

# exc 5 >>>
def f(n):
    #base
    if n == 0:
        return 5
    #transition
    return f(n-1)+3

print(f(100))

# exc 6 >>> sequence output from 1 to n
def seq(n):
    for i in range(1,n+1):
        print(i)

seq(10) #ROFL

# exc 7 >>> поочередный вызов функции (для понятности)
def f(n):
    s = '   '*(7-n)
    print(s,'f',n)
    if n <= 2:
        return 1
    return f(n-1)+g(n-2)
def g(n):
    s = '   ' * (7 - n)
    print(s,'g',n)
    if n <= 2:
        return 1
    return g(n-1)+f(n-2)

print(f(7))''' # HARD 16

    # ГРОБЫ >>>
"""#степени двойки #ПРИ 1024 НЕ РАБОТАЕТ(((
def stepen(n):
    if n == 0:
        return 1
    return stepen(n-1)*2
n = int(input())
print(stepen(n))

#бинарное возведение в степень (делает меньше операций) #ПРИ 1024 РАБОТАЕТ
def binStep(n):
    if n == 0:
        return 1
    if n%2 == 0:
        x = binStep(n//2)
        return x*x
    if n%2 == 1:
        x = binStep(n//2)
        return x*x*2
n = int(input())
print(binStep(n))

# бинарное возведение в степень (2^n)
def f(n): #НЕРАБОЧИЙ ШЛАГ
    if n == 0:
        return 1
    if n%2 == 0: #если четное
        return f(n//2)*f(n//2)
    else:   #если нечетное
        return f(n//2)*f(n//2)*2 #BUUUTT!!! есть код получше
print(f(100000))

def f2(n):  #вот это и есть бинарное возведение в степерь
    if n == 0:
        return 1
    x = f2(n//2)
    if n%2 == 0:
        return x*x
    else:
        return x*x*2
print(f2(100000))

""" # Бинарное возведение в степень
"""#мемоизация - запоминание предыдущих полученных значений в рекурсии
#кеширование, запись, сохранение в массив

#числа фибоначи
n = int(input())

a = [0]*n
a[0], a[1] = 1, 1
for i in range(2, n):
    a[i] = a[i-1] + a[i-2]
print(f'Цикл >>> {a[n-1]}')""" # Числа Фибоначи
"""# PRODUCT
def product(a,repeat):
    if repeat == 0:
        return []
    if repeat == 1:
        b = []
        for i in range(len(a)):
            t = a[i]
            b.append(t)
        return b

    b = product(a,repeat-1)
    c = []
    for i in b:
        for j in a:
            c.append(i+j)
    return c

a = ['A','B']
print(product(a,2))
print(product(a,3))
print(product(a,4))
print(len(product(a,10)))

b = ['0','1'] #<------ TOPCHIK, BUT I DONT UNDERSTAND BECAUSE 12 HOURS ON THE CLOCK
for i in product(b,8):
    print(i)
""" # Типо itertools.product своими руками
"""# вычислить C_n^k

def fact(n): #обычный вывод факториала факторил
    if n == 1:
        return 1
    return n*fact(n-1)

n = int(input())
k = int(input())
ans = fact(n)//(fact(k)*fact(n-k)) #1 СПОСОБ - чисто формула C из n по k
print(ans)

# решение покруче рекурсивно
#с_n^k = c_(n-1)^k + c_(n-1)^(k-1)
#c_n^0 = 1 and c_n^n = 1

def comb(n,k):
    if k == 0 or k == n:
        return 1
    return comb(n-1,k)+comb(n-1,k-1)

ans = comb(n,k) #2 СПОСОБ
print(ans)
""" # Комба
'''
a = 'ABCD'
for x in a:
    for y in a:
        for z in a:
            for w in a:
                for j in a:
                    print(x,y,z,w,j)
'''  # Хер знает что

    # Самоделки
"""def ar_product(s,r,ans):#<----------------\
    if(r==0):                             #|
        print(ans)                        #|
    else:                                 #|
        for i in range(len(s)):           #|
            ar_product(s,r-1,ans+s[i])#---/
        # рекурсионно уменьшаем r (репит)
        # ans прибавляется ишный элемент массива s"""  # itertools.product
'''
def ar_permutations(ans,s):
    if(len(s)==0):
        print(ans)
    else:
        for i in range(len(s)):
            s_new = ''
            for j in range(len(s)):
                if(j!=i):
                    s_new += s[j]
            #s_new - строка s без 1-й буквы (s.remove(i))
            ar_permutations(ans+s[i],s_new)

ar_permutations('A','ABC')
#как же работает?!

#длина строки 3 >>>

ar_per('1','23')
    ar_per('12','3')
        ar_per('123','') ---> print('123')
    ar_per('13','2')
        ar_per('132','') ---> print('132')

ar_per('2','13')
    ar_per('21','3')
        ar_per('213','') ---> print('213')
    ar_per('23','1')
        ar_per('231','') ---> print('231')

ar_per('3','12')
    ar_per('31','2')
        ar_per('312','') ---> print('312')
    ar_per('32','1')
        ar_per('321','') ---> print('321')
'''  # itertools.permutations
'''
def ar_combinations(ans,s,r):
    if (r==0):
        print(ans)
    elif (r<= len(s)):
        n = len(s)
        for i in range(n):
            s_new = ''
            for j in range(i+1,n):
                s_new += s[j]
            ar_combinations('Hello world','',1)

ar_combinations('A','ABCD',0)

#как работает ???!!!
ar_combinations('','ABCD',1) #--> A,B,C,D
    ar_comb('A','BCD',0)
    ar_comb('B','CD',0)
    ar_comb('C','D',0)
    ar_comb('D','',0)

ar_combinations('','ABCDE',2)
    ar_combinations('A','BCDE',1) #--> AB,AC,AD,AE
    ar_combinations('B','CDE',1) #--> BC,BD,BE
    ar_combinations('C','DE',1) #--> CD,CE
    ar_combinations('D','E',1) #--> DE
    ar_combinations('E','',1) #--> ничего

ar_combinations('','1234567890',5)
    ar_combinations('1','234567890',4)
        ar_combinations('12','34567890',3)
    ar_combinations('2','34567890',4)
    ar_combinations('3','4567890',4)
    ar_combinations('4','567890',4)
    ar_combinations('5','67890',4)
    ar_combinations('6','7890',4)
        ar_combinations('67','890',3)
            ar_combinations('678','90',2)
                ar_combinations('6789','0',1)
                   ar_combinations('67890','',0) --> 67890
                ...
            ...
        ar_combinations('68','90',3) --> ничего
        ar_combinations('69','0',3) --> ничего
        ar_combinations('60','',3)  --> ничего
    ar_combinations('7','890',4) --> ничего
    ar_combinations('8','90',4) --> ничего
    ar_combinations('9','0',4) --> ничего
    ar_combinations('0','',4) --> ничего
'''  # itertools.combinations
'''   
ar_product('ABCD',1,'') # ---> A,B,C,D
ar_product('ABCD',1,'A') # ---> AA,AB,AC,AD
ar_product('ABCD',7,'')

s = "ABCD"
r = 3
for i in range(len(s)):
    ar_product(s,r-1,s[i])

s = 'ABCD'
r = 3
for i in range(len(s)):
    ar_product(s,r-1,s[i])
        #ar_product(s,r-1,s[0]) # --> трехбуквенные вида A__ (AAA,AAB,AAC,AAD,ABA,ABB...)
        #ar_product(s,r-1,s[1]) # --> все трехбуквенные вида B__
        #ar_product(s,r-1,s[2]) # --> все трехбуквенные вида С__
        #ar_product(s,r-1,s[3]) # --> все трехбуквенные вида D__


    #НЕМНОГО ТЕОРИИ
s = 'HELLO WORLD'
i = 5 # 5-ый элемент s (т.е. пробел)
s_new = ''
for j in range(len(s)):
    if(j!=i):               # если i не равно переброному элементу,
        s_new = s_new +s[j] # то перебранный элемент попадает в новый s
print(s_new) #без 5 элемента (т.е. без пробела)

s = 'HELLO WORLD'
for i in range(len(s)): #вложенный цикл, перебирает элемент с другими элементами массива
    s_new = ''          # когда в переборе появляется такой же элемент, то он не берется (см. ниже)
    ans = ''
    for j in range(len(s)): # ELLO WORLD, HLLO WORLD, HELO WORLD, HELO WORLD, HELL WORLD, HELLOWORLD, HELLO ORLD и т.д.
        if(j!=i):               # если i не равно переброному элементу,
            s_new = s_new +s[j] # то перебранный элемент попадает в новый s
    ans += s[i] #прибавляется перебираемый элемент i
    print(ans,"   ",s_new)
'''  # Убийственные гробы

'''
def f(n):
    k = 0
    if n < 0: k = -n
    elif n%2==0: k = 2*n+1+f(n-3)
    else: k = 4*n+2*f(n-4)
    return k
print(f(33))

def f(n):
    k = 0
    if n < 3: k = n + 3
    elif n%3==0: k =(n+2)*f(n-4)
    else: k = n + f(n-1) + 2*f(n-2)
    return k
print(f(20))

def f(n):
    k = 0
    if n==1: k = 1
    elif n>1: k = 2*f(n-1)+g(n-1)-2*n
    return k
def g(n):
    l = 0
    if n==1: l = 1
    elif n>1: l = f(n-1)+2*g(n-1)+n
    return l
print(f(14)+g(14))

def f(n):
    k = 0
    if n==1: k = 1
    elif n>1: k = 3*f(n-1)-g(n)-n+5
    return k
def g(n):
    l = 0
    if n==1: l = 1
    elif n>1: l = f(n-1)+3*g(n-1)-3*n
    return l
print(f(5)+g(5))

def F( n ):
    global k
    k += 1
    if n >= 1:
        k += 1
        F(n-1)
        F(n-3)
        k += 1
    return k
k = 0
F(40)
print(k)

def F( n ):
    global k
    k += 1
    if n >= 1:
        k += 1
        F(n-1)
        F(n//3)
        k += 1
    return k
k = 0
F(280)
print(k)

def F( n ):
    global k
    k += 1
    if n >= 1:
        k += 1
        F(n-1)
        F(n//2)
    return k
k = 0
F(140)
print(k)

def F( n ):
    global k
    k += n+1
    if n > 1:
        k += n+5
        F(n-1)
        F(n-2)
    return s
i = 0
while True:
    i += 1
    k = 0
    if F(i)>1000000:
        break
print(i, F(i))
'''
def F( n ):
    global s
    s+=n*n
    if n > 1:
        s+=(2*n+1)
        F(n-2)
        F(n//3)
    return s
i = 0
while True :
    i+=1
    s = 0
    if F(i)>3200000:
        break
print(i, s)









