'''
#6
s = 15
n = 0
while 50 < (2*s*s):
    s = s - 1
    n = n + 2
print(n)

#12
a = '1'*99
while '111' in a:
    a = a.replace('111', '22', 1)
    a = a.replace('222', '11', 1)
print(a)

#14
a = 4 * (125**91) + 2*(25**30) - 5**41 - 144
c = 0
while a > 0:
    if a%5 == 4:
        c+=1
    a//=5
print(c)

#15
for A in range(0,10000):
    GG = True
    for x in range(0,100):
        for y in range(0, 100):
            if ((x <= A) or (y < A) or ((x*y)%4 == 0) or (y*y > 10**6) or (x*x > 10**4)) == False:
                GG = False
                break
    if GG == True:
        print(A)
        break

#16
def f(n):
    if n == 0:
        return 0
    if n > 0 and n%3 == 0:
        return n+f(n-3)
    if n%3 > 0:
        return n+f(n-(n%3))
print(f(22))

#17
f = open('Задание_17__b7ri.txt')
minim = 1000000000000
c = 0
a = [int(i) for i in f]
for i in range(len(a)-1):
    if a[i]%5 == 0 and a[i+1]%5 == 0:
        c+=1
        if a[i]*a[i+1] < minim and (a[i]*a[i+1])%3 == 0 :
            minim = a[i]*a[i+1]
print(c,minim)

#19-21
# +1, *2, >=77
from functools import lru_cache
def moves(h):
    a,b = h
    return (a+1,b),(a,b+1),(a*2,b),(a,b*2)
@lru_cache(None)
def f(h):
    if sum(h)>= 77:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'

for s in range(1,80):
    h = 7,s
    print(s,f(h))

#22
for i in range(1,100000):
    x = i
    a = 9
    b = 100000
    while x > 0:
        a = a - 3
        b = b * (x%100)
        x = x//100
    if a == 0 and b == 0:
        print(i)

#23
def func(s,f):
    if s == f:
        return 1
    if s > f:
        return 0
    return func(s+2,f)+func(s*10,f)
print(func(2,40))

#24
f = open('Задание_24__b7rk.txt')
n = f.readline()
maxim = -100000000
c = 1
for i in range(len(n)-1):
    if not(n[i] == n[i+1] == 'P'):
        c+=1
        if c > maxim:
            maxim = c
    else:
        c=1
print(maxim)

#25
def is_prosto(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

for i in range(607262,607357):
    if is_prosto(i):
        print(i,end=' ')

#27
f = open('Задание_27B__b7rj.txt')
n = int(f.readline())
s = 0
difMIN = 1000000000
for i in range(n):
    a,b = [int(i) for i in f.readline().split()]
    s += max(a, b)
    diff = abs(a-b)
    if diff % 2 != 0:
        difMIN = min(difMIN,diff)
if s%2 == 0:
    print(s-difMIN)
else:
    print(s)

#A - 139587
#B - 399762093
'''
for A in range(1,500):
    GG = True
    for x in range(1,500):
        for y in range(1,500):
            f = ((y >= -4*x + 12) and (y >= 4*x - 12)) == (y >= A*abs(x - 3))
            if f == 0:
                GG = False
                break
        if GG == False:
            break
    if GG == True:
        print(A)

















