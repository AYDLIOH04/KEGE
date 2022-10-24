# кортежи
from functools import lru_cache
'''
# немножно фишек от меня для себя из будущего, чтоб не забыл
# там кароче эээ если число нечетное(на которое делится), то мы его тип должны округлить вниз
def moves(h):
    a,b = h
    return (a-1,b),(a,b-1),(int(a/2),b),(a,int(b/2))
h = 6,9
print(moves(h))



a = [int(i) for i in input().split()]
x,y = [int(i) for i in input().split()]
print(x+y)
print(a)

#Петя и Ваня играют в игру, есть куча камней, можно +1 или +2

def moves(x):
    return x+1,x+2
print(moves(7))

def moves(h):
    #return (h[0]+1,h[1]),(h[0],h[1]+1),(h[0]*2,h[1]),(h[0],h[1]*2)
    #иначе можно так
    a,b = h
    return (a+1,b),(a,b+1),(a*2,b),(a,b*2) #кортеж

def moves(x):
    return x+1,x*2

for i in moves(7):
    if i >= 10:
        print(i,'END')
#h = 7,10 #кортеж (неизменяемый)
#print(moves(h))

a = [(i>=10) for i in moves(7)]
print(a)


def moves(x):
    return x+1,x*2
a = list(moves(7))
print(a)

b = [a[i]>=10 for i in range(2)] #ну типо проверка
print(b)


#Петя и Ваня играют в игру
#есть две кучи камней, можно +1 или *2
def moves(h):
    a,b = h
    return (a+1,b),(a,b+1),(a*2,b),(a,b*2)

for j in range(1,10):
    h = 7,j
    print(h)
    for i in moves(h):
        if(sum(i)>=13):
            print('WIN',i)
        else:
            print('END',i)


def moves(h):
    a,b = h
    return (a+1,b),(a,b+1),(a*2,b),(a,b*2)

h = 2,5
a = [sum(s)>= 10 for s in moves(h)]
print(a)
''' #ВСЯКОЕ
'''
    # ALL & ANY

#на промежутке [1,100000] найдите все числа
#которые делятся на 2,3 на 5, но не делятся на 17,23

c = 0
for i in range(1,100001): #слишком много and,and,and если через if
    a = i%2 == 0,i%3 == 0,i%5 == 0,i%17 != 0,i%23 != 0
    if( all(a) ): #если все в "A" True, то...           #ALL - AND
        c+=1                                            #ANY - OR
print(c)


#тут все понятно
a = [False,True,True,False,False]
print(any(a)) #тру
print(all(a)) #фолс


def ar_all(a):      #как работает ALL
    for i in a:
        if(i != True):
            return False
    return True


#типичная задачка?
def moves(h):
    a,b = h
    return (a+1,b),(a,b+1),(a*2,b),(a,b*2)

for i in range(1,20):
    for j in range(1,20):
        h = i,j
        if (sum(h)>=13):
            pass #пропустить
        
        elif(any([(sum(x)>=13) for x in moves(h)])):
            print(h,'P1')
''' # All & Any
'''
    #норм вебчик пошел-поехал BOOOOOOOM
from functools import lru_cache
# least recently used _ cache
# наимнее недавно использованный _ архив(кэш)


#задача 1
#19 - (a+1,b),(a,b+1),(a*2,b),(a,b*3) >=69 , min S #отв > 7
#20 - P2, но не за P1 #отв > 16,19
#21 - min S, при P1 и P2, но не гарантированно P1 #отв > 18
def moves(h):
    a,b = h
    return (a+1,b),(a,b+1),(a*2,b),(a,b*3)

# P1 - позиция, из которой Петя выигрывает за один ход
#т.е. стартует и имеет выигрышную стратегию из этой позиции,
#повзоляющую за один ход выиграть сразу (к примеру 10,58)
    #P1 - позиция, из которой any move ведет в END
                            # any x in moves f(x) == END

# V1 - поз, из которой если игра начнется(П - первый, В - второй), то
# Bаня выиграет за один ход
    # Петя - проигрывает, как бы ни сходил. Как бы он ни сходил, он не должен >>>
    # A) попасть в END (иначе он выиграет, ну и такие поз. мы уже нашли)
    # B) куда бы он ни шагнул, Ваня должен оттуда за один ход прыгнуть в END
        #получаетя, V1 - такая позиция, из которой все ходы попадают туда
        #откуда Ваня может за раз прыгнуть в END - то есть, все ходы ведут в P1
                        #V1 - pos, из которой ALL x in moves(h) f(x) == 'P1'

# V2 - поз, из которой
@lru_cache(None) #мемоизация, считает БЫСТРЕЕ для рекурсии!
def f(h): #рекурсивная функция
    if (sum(h) >= 69):          #можно без elif, т.к. после ретерна из функции выходит
        return 'END'
    if (any(f(x)=='END' for x in moves(h))):   #(any([sum(x)>=69 for x in moves(h)])):
        return 'P1'
    if (all(f(x)=='P1' for x in moves(h))):
        return 'V1'
    if (any(f(x)=='V1' for x in moves(h))):
        return 'P2'
    if(all(f(x)== 'P1' or f(x) == 'P2' for x in moves(h))):     #НЕГАРАНТИРОВАННО ЗА ОДИН
        return 'V2'


#ПРИКОЛЯМБУЛА!!!
#k = 5,6
#a = [x == (6,6) for x in moves(k)]
#print(a) #True, False, False, False


#for x in range(1,70):       #перебор всех двух кучек, но обычно в задачах дается (10,S) см. ниже
#    for y in range(1,70):
#        h = x,y
#        if(f(h) == 'V1'):
#            print(h,f(h))


for s in range(1,70):
    h = 10,s
    print(s,f(h))



#задача 2
#старт (7,S)
#19 - +1, *2, >= 77, minS - V1 by mistake P1 #ans = 18
#20 - P2 #ans = 31,34
#21 - V1 and V2, not always V1, minS #ans = 30

from functools import lru_cache
def moves(h):
    a,b = h
    return (a+1,b),(a,b+1),(a*2,b),(a,b*2)

@lru_cache(None)
def f(h):
    if(sum(h)>=77):
        return 'END'
    if(any(f(x) == 'END' for x in moves(h))):
        return 'P1'
    if(all(f(x) == 'P1' for x in moves(h))):
        return 'V1'
    if(any(f(x) == 'V1' for x in moves(h))):
        return 'P2'
    if(all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h))):
        return 'V2'

for s in range(1,100):
    h = 7,s
    print(s,f(h))


#задача 3
#start (10,s)
#19 - +2, *3, >= 103, minS-? #ans = 11
#20 - P2 #ans = 11,12
#21 - V1 and V2 but not allways V1, minS - ? #ans = 10

from functools import lru_cache
def moves(h):
    a,b = h
    return (a+2,b),(a,b+2),(a*3,b),(a,b*3)

@lru_cache(None)
def f(h):
    if (sum(h) >= 103):
        return 'END'
    if (any(f(x) == 'END' for x in moves(h))):
        return 'P1'
    if (all(f(x) == 'P1' for x in moves(h))):
        return 'V1'
    if (any(f(x) == 'V1' for x in moves(h))):
        return 'P2'
    if (all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h))):
        return 'V2'
for s in range(1,120):
    h = 10,s
    print(s,f(h))

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
print(f(h))

from functools import lru_cache
def moves(h):
    a,b = h
    return (a+3,b),(a,b+3),(a*2,b),(a,b*2)
@lru_cache(None)
def f(h):
    if sum(h) >= 65:
        return 'END'
    if (any(f(x) == 'END' for x in moves(h))):
        return 'P1'
    if (all(f(x) == 'P1' for x in moves(h))):
        return 'V1'
    if (any(f(x) == 'V1' for x in moves(h))):
        return 'P2'

for s in range(1,100):
    h = 10,s
    print(s,(f(h)))


    #ezDZ
#1
a = list(range(10))
b = tuple(a)
print(b)

#2
def summma(n,b):
    if n == 1:
        return b[0]
    return b[n-1]+summma(n-1,b)

b = tuple(int(i) for i in input().split())
n = len(b)
print(summma(n,b))
print(sum(b)) # for check

#3
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
t = tuple(arr)
a = (t*n)
b = tuple(reversed(a))
c = tuple(a+b)
print(a,b,c,sep="\n")

#4
def prod(n):
    return (n**2,n**3,round(n**0.5,2))
print(prod(int(input())))

#5
a = ['AR','','','','']
def f(a):
    if any((len(i) > 0) for i in a):
        return True
    else:
        return False
print(f(a))

#6
def proverka(a): 
    if all([x%1 == 0 for x in a]):
        return True
    return False
a = [float(i) for i in input().split()]
print(proverka(a))

#7
a = []
m,n,k = map(int,input().split())
for i in range(m,n+1,k):
    a.append(i)
print(a)
if any([x%5 == 0 for x in a]):
    print(True)
else:
    print(False)
if all([x>0 for x in a]):
    print(True)
else:
    print(False)

#8
def moves(h):
    return (h+1,h+3,h+5,h+25)

def f(h,k):
    if h == k:
        return True
    if any(x == k for x in moves(h)):
        return True
    return False

h,k = map(int,input().split())
print(f(h,k))


# exc 1-3 ans 9,56,34
def moves(h):
    return h+2, h*3

def f(h):
    if h>=27:
        return 'END'
    if (any(f(x) == 'END' for x in moves(h))):
        return 'P1'
    if (all(f(x) == 'P1' for x in moves(h))):
        return 'V1'
    if (any(f(x) == 'V1' for x in moves(h))):
        return 'P2'
    if (all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h))):
        return 'V2'

for h in range(1,100):
    print(h,f(h))
    
# xc 4-6 ans 11,4,6
def moves(h):
    return h+2, h*2, h*3

def f(h):
    if h>=31:
        return 'END'
    if (any(f(x) == 'END' for x in moves(h))):
        return 'E1'
    if (all(f(x) == 'E1' for x in moves(h))):
        return 'V1'
    if (any(f(x) == 'V1' for x in moves(h))):
        return 'E2'
    if (all(f(x) == 'E2' or f(x) == 'E1' for x in moves(h))):
        return 'V2'

for h in range(1,100):
    print(h,f(h))

# exc 7-9, ans 12,6910,78
def moves(h):
    return h+2, h*2

def f(h):
    if h>=25:
        return 'END'
    if (all(f(x) == 'END' for x in moves(h))):
        return 'P1'
    if (any(f(x) == 'P1' for x in moves(h))):
        return 'V1' # для 7 задачи
        
    #if (any(f(x) == 'V1' for x in moves(h))):
    #    return 'P2'
    #if (all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h))):
    #    return 'V2'
    
for h in range(1,50):
    print(h,f(h))

# exc 10-12, ans 14,713,12
def moves(h):
    return h+1, h*2
@lru_cache(None)
def f(h):
    if h >= 29:
        return 'END'
    if (any(f(x) == 'END' for x in moves(h))):
        return 'P1'
    if (all(f(x) == 'P1' for x in moves(h))):
        return 'V1'
    if (any(f(x) == 'V1' for x in moves(h))):
        return 'P2'
    if (all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h))):
        return 'V2'
for h in range(1,50):
    print(h,f(h))

#exc 13-15 ans 4,10,9
def moves(h):
    return h+1, h*3
@lru_cache(None)
def f(h):
    if h >= 36:
        return 'END'
    if (any(f(x) == 'END' for x in moves(h))):
        return 'P1'
    if (all(f(x) == 'P1' for x in moves(h))):
        return 'V1'
    if (any(f(x) == 'V1' for x in moves(h))):
        return 'P2'
    if (all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h))):
        return 'V2'
for h in range(1,50):
    print(h,f(h))

#exc 16-18 ans 5,4911,810
def moves(h):
    return h+1, h*3, h+3

@lru_cache(None)
def f(h):
    if h >= 39:
        return 'END'
    if (any(f(x) == 'END' for x in moves(h))):
        return 'P1'
    if (all(f(x) == 'P1' for x in moves(h))):
        return 'V1'
    if (any(f(x) == 'V1' for x in moves(h))):
        return 'P2'
    if (all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h))):
        return 'V2'

for h in range(1,50):
    print(h,f(h))

# exc 19-21 ans 17,1618,19
def moves(h):
    return h-1, h-3

@lru_cache(None)
def f(h):
    if h <= 11:
        return 'END'
    if (any(f(x) == 'END' for x in moves(h))):
        return 'P1'
    if (all(f(x) == 'P1' for x in moves(h))):
        return 'V1'
    if (any(f(x) == 'V1' for x in moves(h))):
        return 'P2'
    if (all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h))):
        return 'V2'
for h in range(1,50):
    print(h,f(h))

# exc 22-24 ans 14,2126,0(нет значений)
def moves(h):
    a,b = h
    return (a+1,b),(a,b+1),(a*2,b),(a,b*2)
@lru_cache(None)
def f(h):
    if sum(h) >= 66:
        return 'END'
    if (any(f(x) == 'END' for x in moves(h))):
        return 'P1'
    if (all(f(x) == 'P1' for x in moves(h))):
        return 'V1'
    if (any(f(x) == 'V1' for x in moves(h))):
        return 'P2'
    if (all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h))):
        return 'V2'

for s in range(1,100):
    h = 11,s
    print(s,f(h))

    # DZ LVL NORM
# exc 1-3 ans 23,111421,0(такого нету)
def moves(h):
    a,b = h
    return (a+1,b),(a,b+1),(a*2,b),(a,b*2)

@lru_cache(None)
def f(h):
    if sum(h) >= 55:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' for x in moves(h)):
        return 'V2'

for s in range(1,100):
    h = 10,s
    print(s,f(h))

# exc 4-6 ans 4,3,13
def moves(h):
    a,b = h
    return (a+1,b),(a,b+1),(a*3,b),(a,b*3)

@lru_cache(None)
def f(h):
    if sum(h) >= 49:
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
    h = 5,s
    print(s,f(h))

# exc 7-9 ans 31,1028,29
def moves(h):
    a,b = h
    return (a+2,b),(a,b+2),(a*3,b),(a,b*3)

@lru_cache(None)
def f(h):
    if sum(h) >= 99:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'

for s in range(1,105):
    h = 7,s
    print(s,f(h))

# exc 10-12 ans 11,4,16
def moves(a):
    return a+1,a+2,a+3,a*2

@lru_cache(None)
def f(h):
    if h >= 42:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h)):
        return 'V2'

for s in range(1,105):
    print(s,f(s))


# немножно фишек от меня для себя из будущего, чтоб не забыл
# там кароче эээ если число нечетное(на которое делится), то мы его тип должны округлить вниз
def moves(h):
    a,b = h
    return (a-1,b),(a,b-1),(int(a/2),b),(a,int(b/2))
h = 6,9
print(moves(h))
''' # Вебы + DZ

"""
from functools import lru_cache
def moves(h):
    if h % 2 == 0:
        return h+1, h+3
    return [h*3]

@lru_cache(None)
def f(h):
    if h >= 51:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h)):
        return 'V2'
for s in range(1,60):
    print(s,f(s))


def moves(h):
    if h < 3:
        if h % 2 == 0:
            return h/2, h-1
        else:
            return [h - 1]
    else:
        if h % 2 == 0:
            return h-3, h/2, h-1
        else:
            return h-3, h-1

@lru_cache(None)
def f(h):
    if h == 0:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h)):
        return 'V2'
for s in range(1,100):
    print(s,f(s))
"""




'''
#########################################################
# 27774
def moves(h):
    a, b = h
    arr = []
    if a > 1:
        arr.append((a-1, b))
        arr.append((a//2 + (a%2==1), b))
    if b > 1:
        arr.append((a, b-1))
        arr.append((a, b//2 + (b%2==1)))

    return arr

@lru_cache(None)
def f(h):
    if sum(h) <= 20:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'

for s in range(100):
    h = 10, s
    print(s, f(h))
#########################################################
''' # Гроб 1
"""from functools import lru_cache
def moves(h):
    a, b = h
    arr = []
    if a > 0:
        arr.append((a-1, b))
        arr.append((a//2, b))
    if b > 0:
        arr.append((a, b-1))
        arr.append((a, b//2))

    return arr

@lru_cache(None)
def f(h):
    if sum(h) <= 20:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h)):
        return 'V2'

for s in range(100):
    h = 10, s
    print(s, f(h))
""" # Прототип -1 или //2 (Гроб 2)
"""from functools import lru_cache
def moves(h):
    a, b = h
    arr = []
    if a > 1:
        arr.append((a - 1, b))
        arr.append((a//2 + (a % 2 != 0), b))
    if b > 1:
        arr.append((a, b - 1))
        arr.append((a, b//2 + (b % 2 != 0)))
    return arr

@lru_cache(None)
def f(h):
    if sum(h) <= 40:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h)):
        return 'V2'

for s in range(21,200):
    h = 20, s
    print(s, f(h))""" # Гроб 3
"""
def moves(h): 
    if 20 <= h <= 29:
        return (h+1), (h*2)
    if h >= 30:
        return [h+1]
    return (h+1), (h*2), (h*3)
    
@lru_cache(None)
def f(h):
    if h >= 36:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'

for s in range(1,40):
    print(s,f(s))

# 19 >>> 34
# 20 >>> 1
# 21 >>> 11 32
""" # ГРОБ 4 куча победа от 36 до 60
"""def moves(h):
    return h+1, h*2, h*3

from functools import cache
@cache
def f(h):
    if h >= 39 and h <= 69:
        return 'END'
    if h > 69:
        return 'YOU LOST'
    if any(f(x) == 'END' for x in moves(h)):
        return 'WIN1'
    if all(f(x) == 'WIN1' or f(x) == 'YOU LOST' for x in moves(h)):
        return 'LOSE1'
    if any(f(x) == 'LOSE1' for x in moves(h)):
        return 'WIN2'
    if all(f(x) == 'WIN1' or f(x) == 'WIN2' or f(x) == 'YOU LOST' for x in moves(h)):
        return 'LOSE2'
for s in range(1,100):
    print(s,f(s))
""" # победа от 39 до 69
"""def moves(h):
    return h+1, h*2, h*3

from functools import cache
@cache
def f(h):
    if h >= 43 and h <= 72:
        return 'END'
    if h > 72:
        return 'GG'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' or f(x) == 'GG' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P1' or f(x) == 'GG' for x in moves(h)):
        return 'V2'
for s in range(1,100):
    print(s,f(s))""" # победа от 43 до 72
"""def moves(h):
    a, b = h
    return (a+1, b), (a, b+1), (a+b, b), (a, b+a)
@lru_cache(None)
def f(h):
    if sum(h) >= 81:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h)):
        return 'V2'
for s in range(1,80):
    h = 7, s
    print(s,f(h))

# 19 >>> 23
# 20 >>> 22 36
# 21 >>> 35""" # Две кучи a+b



    # Гробы
# ЛАЙФКАХ >>> Чтоб прога работала быстрее, нужно в муве перебирать сначала самые больше ходы

"""def moves(h):
    a, b, code = h
    if code == 0:
        return (a, b*2, 1), (b, a, 2)
    if code == 1:
        return (a, b*2, 1), (b, a, 2)
    if code == 2:
        return [(a, b*2, 1)]
def f(h):
    if h[0] + h[1] >= 199:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h)):
        return 'V2'

for i in range(1,100):
    h = 99, i, 0
    if f(h) == 'V1':
        print(i)""" # Что-то статградское
"""

from functools import lru_cache


def moves(h):
    a, b = h
    arr = []
    if a > 0:
        arr.append((a - 1, b))
        arr.append((a // 2, b))
    if b > 0:
        arr.append((a, b - 1))
        arr.append((a, b // 2))
    return arr


@lru_cache(None)
def f(h):
    if sum(h) <= 18:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'


# Для 19, 21 задачки
for s1 in range(1, 100):
    for s2 in range(1, 100):
        h = s1, s2
        if sum(h) >= 19:
            if f(h) == 'V2':
                print(s1, s2, f(h))

# Для задачки 20
for s in range(1, 100):
    h = 13, s
    print(s, f(h))""" # 19 V1 найти M в паре (M;M) >>> 13  ГРОБ НА УМЕНЬШЕНИЕ
                # 20 P2 min&max при K=13 >>> 11 22
                # 21 V2 min N в паре (N;N) >>> 14
"""from functools import lru_cache

def moves(heap):
    return heap + 3, heap * 2

@lru_cache(None)
def game(heap):
    if heap >= 60:
        return 'END'
    elif any(game(x) == 'END' for x in moves(heap)):
        return 'P1'
    elif all(game(x) == 'P1' for x in moves(heap)):
        return 'V1'
    elif any(game(x) == 'V1' for x in moves(heap)):
        return 'P2'
    elif all(game(x) == 'P1' or game(x) == 'P2' for x in moves(heap)):
        return 'V2'

for s in range(1, 58):
    print(s, game(s))""" # Двоичное число и каунтер единичек в нем
"""from functools import lru_cache

def moves(heap):
    return heap + 1, heap + 2, heap + 3, heap * 3

@lru_cache(None)
def game(heap):
    if 50 <= heap <= 100:
        return 'END'
    elif heap > 100:
        return 'P1'
    elif any(game(x) == 'END' for x in moves(heap)):
        return 'P1'
    elif all(game(x) == 'P1' for x in moves(heap)):
        return 'V1'
    elif any(game(x) == 'V1' for x in moves(heap)):
        return 'P2'
    elif all(game(x) == 'P1' or game(x) == 'P2' for x in moves(heap)):
        return 'V2'

for s in range(1, 50):
    print(s, game(s))
""" # От 50 до 100 (немного другой способ)
"""from functools import lru_cache
def moves(heap):
    m = []
    if heap % 2 == 0:
        m += [heap // 2]
    elif heap > 1:
        m += [heap - 2]
    if heap % 3 == 0:
        m += [heap // 3]
    elif heap > 2:
        m += [heap - 3]
    return m
@lru_cache(None)
def game(heap):
    if heap == 1:
        return 'END'
    elif any(game(x) == 'END' for x in moves(heap)):
        return 'P1'
    elif all(game(x) == 'P1' for x in moves(heap)):
        return 'V1'
    elif any(game(x) == 'V1' for x in moves(heap)):
        return 'P2'
    elif all(game(x) == 'P1' or game(x) == 'P2' for x in moves(heap)):
        return 'V2'

for s in range(1, 38):
    print(s, game(s))""" # Условие: //2, если не делится, то -2 ИЛИ //3, если не делится, то -3
"""from functools import lru_cache

def moves(heap):
    m = []
    if (heap + 1) % 2 != 0:
        m += [heap + 1]
    if (heap + 3) % 2 != 0:
        m += [heap + 3]
    if (heap * 3) % 2 != 0:
        m += [heap * 3]
    return m

@lru_cache(None)
def game(heap):
    if heap >= 51:
        return 'END'
    elif any(game(x) == 'END' for x in moves(heap)):
        return 'P1'
    elif all(game(x) == 'P1' for x in moves(heap)):
        return 'V1'
    elif any(game(x) == 'V1' for x in moves(heap)):
        return 'P2'
    elif all(game(x) == 'P1' or game(x) == 'P2' for x in moves(heap)):
        return 'V2'

for s in range(1, 51):
    print(s, game(s))""" # Подлое условие: можем ходить только в нечетное количество кучек
"""from functools import lru_cache

def moves(heap):
    a, b, c = heap
    m = []
    if a > 1:
        m += [(a - 1, b, c), (a // 2 + (a%2), b, c)]
    if b > 1:
        m += [(a, b - 1, c), (a, b // 2 + (b%2), c)]
    if c > 1:
        m += [(a, b, c - 1), (a, b, c // 2 + (c%2))]
    return m

@lru_cache(None)
def game(heap):
    if sum(heap) <= 32:
        return 'END'
    elif any(game(x) == 'END' for x in moves(heap)):
        return 'P1'
    elif all(game(x) == 'P1' for x in moves(heap)):
        return 'V1'
    elif any(game(x) == 'V1' for x in moves(heap)):
        return 'P2'
    elif all(game(x) == 'P1' or game(x) == 'P2' for x in moves(heap)):
        return 'V2'

for s in range(12, 100):
    print(s, game((11, 11, s)))""" # 3 кучи: -1 или //2 +1 если не делится


############################################
"""from functools import lru_cache

# -1, //2+1
def moves(heap):
    a, b, c = heap
    return (a-1, b, c), (a, b-1, c), (a, b, c-1), ((a+1)//2, b, c), (a, (b+1)//2, c), (a, b, (c+1)//2)

@lru_cache(None)
def game(heap):
    if sum(heap) <= 32:
        return 'END'
    if heap[0] <= 1 or heap[1] <= 1 or heap[2] <= 1:
        return 'WE LOST THIS GAME'
    if any(game(x) == 'END' for x in moves(heap)):
        return 'P1'
    if all(game(x) == 'P1' for x in moves(heap)):
        return 'V1'
    if any(game(x) == 'V1' for x in moves(heap)):
        return 'P2'
    if all(game(x) == 'P1' or game(x) == 'P2' for x in moves(heap)):
        return 'V2'

for s in range(12, 100):
    print(s, game((11, 11, s)))""" # 3 кучи уменьшение ЛУЧШЕ ПИСАТЬ ТАК!!!
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
# Тут нужно ручками подумать и понять, что ответ 24 P2""" # Сумма камней 60
"""
# Закодируем ходы:
# 1) +1
# 2) +2
# 0) *2
from functools import lru_cache

def moves(h):
    heap, my_move, opp_move = h

    if my_move == 0: # прошлый ход >>> *2 => НЕЛЬЗЯ *2 !!!
        return (heap+1, opp_move, 1), (heap+2, opp_move, 2)
    if my_move == 1: # прошлый ход >>> +1 => НЕЛЬЗЯ +1 !!!
        return (heap+2, opp_move, 2), (heap*2, opp_move, 0)
    if my_move == 2: # прошлый ход >>> +2 => НЕЛЬЗЯ +2 !!!
        return (heap+1, opp_move, 1), (heap*2, opp_move, 0)

    return (heap + 1, opp_move, 1), (heap + 2, opp_move, 2), (heap * 2, opp_move, 0)


@lru_cache(None)
def f(h):
    if h[0] >= 21:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P1' or f(x) == 'P2' for x in moves(h)):
        return 'V2'
    if any(f(x) == 'V2' for x in moves(h)):
        return 'P3'

for s in range(1, 25):
    h = s, -1, -1
    print(s, f(h))""" # СТАТГРАД 8.02.2022 >>> 1 куча, +1, +2, *2 нельзя повторять СВОЙ ПРОШЛЫЙ ход
"""def moves(h):
    a, move = h

    if move == 0:
        return (a + 1, 1), (a + 2, 2), (a * 2, 3)
    if move == 1:
        return (a + 2, 2), (a * 2, 3)
    if move == 2:
        return (a + 1, 1), (a * 2, 3)
    if move == 3:
        return (a + 1, 1), (a + 2, 2)

@lru_cache(None)
def f(h):
    if h[0] >= 43:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'WIN1'""" # 1 куча, +1, +2, *2 нельзя повторять ПРОШЛЫЙ ход
############################################


"""from functools import lru_cache

def moves(heap):
    a, b = heap
    return (a * 4, b), (a, b * 4), (a + 1, b), (a, b + 1)

@lru_cache(None)
def game(heap):
    a, b = heap
    if a * b >= 1056:
        return 'END'
    elif any(game(x) == 'END' for x in moves(heap)):
        return 'P1'
    elif all(game(x) == 'P1' for x in moves(heap)):
        return 'V1'
    elif any(game(x) == 'V1' for x in moves(heap)):
        return 'P2'
    elif all(game(x) == 'P1' or game(x) == 'P2' for x in moves(heap)):
        return 'V2'

for s in range(132, 0, -1):
    print(s, game((8, s)))""" # Победа если произведение кучек >= 1056.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"""def moves(h):
    return h + 3, h * 2

@lru_cache(None)
def game(h):
    if h >= 60:
        return 0  # 0 ходов до победы
    steps = [game(x) for x in moves(h)]  # количество ходов до победы для следующих ходов
    if any(x % 2 == 0 for x in steps):  # если хотя бы один ход приводит нас к победе
        return 1 + min(x for x in steps if x % 2 == 0)  # возвраащем кол-во ходов до победы
    return 1 + max(steps)  # мы поняли что мы проиграли, растягиваем игру

for s in range(1, 58):
    t = game(s)
    if t % 2 == 0:
        print(s, f"V{t//2}") # По определению
    else:
        print(s, f"P{(t + 1) // 2}")""" # Вывод ВСЕХ ВЫИГРЫШНЫХ ПОЗИЦИЙ - имба алгоритм
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
