'''
#6
for i in reversed(range(1000)):
    s = 0
    k = 1
    n = i
    while s + k < 47 :
        s = s + k
        k = k + n
    if s == 36:
        print(i)
''' # 6
''' 
#8
a = int('540540',6)
b = int('510510',6)
print(a-b)
''' # 8
'''
#9
c = 0
f = open('123123123')
a = [i for i in f]
print(a)
CHISL = ['1','2','3','4','5','6','8','9','0']
for i in a:
    for j in i:
        if j in CHISL:
            c+=1
            break
print(c)
''' # 9
'''
#12
a = '8'*70
while '2222' in a or '8888' in a:
    if '2222' in a:
        a = a.replace('2222','88',1)
    else:
        a = a.replace('8888','22',1)
print(a)
''' # 12
'''
#13
c = 0
a = 4**512 + 8**512 - 2**128 - 250
while a > 0:
    if a%2 == 0:
        c+=1
    a //= 2
print(c)
''' # 13
'''
#15
for A in range(1,1000):
    flag = True
    for x in range(1,1000):
        for y in range(1,1000):
            f = (y - x != 5) or (A < 2*(x**3) + y) or (A < y**2 + 16)
            if f == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
''' # 15
'''
#16
def f(n):
    if n <= 1:
        return n*3
    return f(n-2)+2*g(n-1)

def g(n):
    if n <= 2:
        return n
    return g(n-2) + 2*f(n-2)*f(n-2)
print(f(5) + g(6))
''' # 16
'''
#17
c,m = 0,100000000000000
f = open('Задание_17__d0ra.txt')
a = [int(i) for i in f]
for i in range(len(a) - 1):
    if a[i]%11 == 0 and a[i+1]%11 == 0:
        c+=1
        if (a[i]+a[i+1])% 101 == 0 and (a[i]+a[i+1]) < m:
            m = (a[i]+a[i+1])
print(c,m)
''' # 17
'''
from functools import lru_cache
#19-21
def moves(h):
    return h+1,h+5,h*3

@lru_cache(None)
def f(h):
    if h >= 78:
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
''' # 19-21
'''
#22
for i in range(10000):
    x = i
    Q = 1
    R = 1
    while x > 0 :
        Q = Q + 3
        if (x%2 == 1) :
            R = R * (x%6)
        x = x//6
    if Q == 10 and R == 25:
        print(i)
''' # 22
'''
#23
def f(x,y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x+1,y) + f(x+2,y) + f(x*3,y)
print(f(3,9) * f(9,14))
''' # 23
'''
#24
f = open('Задание_24__d0rb__d95d.txt')
a = f.readline()
alf ='abcdefghijklmnopkrstuvwxyz'
COUNT = [0]*26
for i in range(26):
    COUNT[i] = a.count(alf[i])
print(max(COUNT) - min(COUNT))
''' # 24
''' 
#25
def prime(n):
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

c = 0
for i in range(55556,55777):
    if prime(i):
        c+=1
print(c)
''' # 25
'''
#27
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
''' # 27













