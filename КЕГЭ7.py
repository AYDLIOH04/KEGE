'''
#4
s = int(input())
n = 1
while s > 20 :
    s = s - 3
    n = n * 3 + 1
print(n)

#12
a = "8"*69
while ('222' in a) or ('8888' in a):
    if ('222' in a):
        a=a.replace('22','8',1)
    else:
        a = a.replace('888', '2', 1)
print(a)

#14
for i in range(6,31):
    c = 0
    x = i
    a = 9**30 + 9**x - 9**6
    while a>0:
        if a%9==0:
            c+=1
        a//=9
    if c == 12:
        print(i)

#16
def G(n):
    if n <= 2:
        return n+1
    elif n > 2:
        return f(n-1)+2*G(n-1)
def f(n):
    if n <= 1:
        return n*2
    elif n > 1:
        return f(n-1)**G(n-1)

print(  (f(3)/G(1))  + (  ((2*G(3)+G(2)+G(1) )**0.5))  / (2*G(1)+1) )

#17
from math import *
f = open('Задание_17__9cop.txt')
a = []
min = 100000000000000
n = 100000
c = 0
for i in range(n):
    a.append(int(f.readline()))
for i in range(n-1):
    if (a[i]*a[i+1])%153 == 0:
        c+=1
        SR = floor((a[i]+a[i+1])/2) #для округления в меньшую сторону
        if SR < min:
            min = SR
print(c,min)

#19-21
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

#22
x = 65525
S = 0
Q = 0
while x > 0 :
    Q = Q + 5
    S = S + (x % 16)
    x = x//16
print(S,Q)

#23
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
#ответ 4

#задание 24
f = open('Задание_24__9p3h.txt')
s = f.readline()
n = len(s)
cp = 0
ct = 0
ck = 0
i = 0
while i<n-1:
    if(s[i]==s[i+1]):
        if (s[i]== 'P'):
            cp+=1
        if (s[i] == 'T'):
            ct += 1
        if (s[i]== 'K'):
            ck+=1
        i=i+2 #эта пара больше не участвует, по усл крч
    else:
        i=i+1
print(min(cp,ct,ck))

# ЗАДАНИЕ 24 БОЛЕЕ ПРОСТЫМ СПОСОБОМ
f = open('Задание_24__9p3h.txt')
s = f.readline()
n = len(s)
p = s.count("PP")
t = s.count("TT")
k = s.count("KK")
print(min(p,t,k))
#6672

#25
for i in range(10000):
    x = i
    if (9*(x**5) - 6246*(x**4) - 25686*(x**3) + 388296*(x**2) + 830925*x - 1187298) == 0:
        print(i)

#26
f = open('Задание_26__9p3i.txt')

s,n = map(int,f.readline().split())
a = []
for i in range(n):
    a.append(int(f.readline()))
a.sort()
t = 0
i = 0
while (t<=s):
    t+=a[i]
    i+=1
# после цикла набранные файлы превысили s, t>s
# i указывает на следующий файл, то есть как раз показывает количетсво набранных файлов.
i = i - 1
t -=a[i]
#теперь t - сумма не превыщающая s, а i - количетсво файлов в этой сумме
print(i)
zh = a[i-1]
t = t-zh

for j in range(i-1,n):
    if(t+a[j]<=s):
        zh = a[j]
print(zh+a[0])
'''
#27
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


