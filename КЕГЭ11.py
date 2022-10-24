'''
#2
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((not x and y) == z) and w
                if f == 1:
                    print(x,y,z,w,int(f))

#6
for i in range(1,100000000):
    x = i
    s = 100
    n = 1000
    while n > 0:
        s = s - 15
        n = n - x
    if s == 25:
        print(i)

#14
a = 512**64 + 64**8 - 8**100
c = 0
while a > 0:
    if a%8 == 0:
        c+=1
    a//=8
print(c)

#15
for A in range(1,1000):
    GG = True
    for x in range(1,1000):
        for y in range(1,1000):
            if ((x < A) or (y <= A) or ((x*y)%2 == 1) or (y*x > 39999)) == False:
                GG = False
                break
        if GG == False:
            break
    if GG == True:
        print(A)
        break

#16
def g(n):
    if n == 1:
        return 1
    return f(n-1)+2*g(n-1)

def f(n):
    if n == 1:
        return 1
    return f(n-1)-2*g(n-1)
print(g(21)+f(10))


#17.1
f = open('Задание_17__asfc.txt')

a = [int(i) for i in f]
n = len(a)
c = 0
maxim = -10000000000000
for i in range(n-1):
    if (str(a[i]*a[i+1])[-2]) == 6:
        c+=1
    if (a[i]+a[i+1]) % 137 == 0 and (a[i]+a[i+1]) > maxim:
            maxim = a[i]+a[i+1]
print(c,maxim)

#17.2
f = open('Задание_17__asfc.txt')

a = [int(i) for i in f]
n = len(a)
c = 0
maxim = -10000000000000
for i in range(n-1):
    t = a[i]*a[i+1]
    if (str(t)[-2]) == '6':
        c+=1
    if (a[i]+a[i+1]) % 137 == 0 and (a[i]+a[i+1]) > maxim:
            maxim = a[i]+a[i+1]
print(c,maxim)

#19
from functools import lru_cache
def moves(h):
    return h+1,h+8

@lru_cache(None)
def f(h):
    if h >= 35:
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
    print(s,f(s))

#22
for i in range(1,100000):
    x = i
    a = 95
    b = 1
    while x > 0:
        a = a + 1
        b = b * (x % 6)
        x = x//6
    if a == 100 and b == 100:
        print(i)

#23.1
def f(start,finish):
    if start == finish:
        return 1
    if start > finish:
        return 0
    if start == 9 or start == 24 or start == 32:
        return 0

    return f(start+1,finish)+f(start*2,finish)+f(start*3,finish)

print(f(1,38))

#23.2
a = [0]*100
a[1] = 1
b = [9,24,32]
for i in range(2,39):
    a[i] = a[i-1] + a[i//2] * (i % 2 == 0) + a[i//3] * (i % 3 == 0)
    if i in b:
        a[i] = 0
print(a[38])

#24

f = open('Задание_24__b21b.txt')
s = f.readline()
c = 0
MAX = 0
preMAX = 0
for i in range(len(s)):
    if s[i] == 'C':
        c+=1
    else:
        if c > MAX:
            preMAX = MAX
            MAX = c
        elif c > preMAX:
            preMAX = c
        c = 0
if c > MAX:
    preMAX = MAX
    MAX = c
elif c > preMAX:
    preMAX = c

print(MAX - preMAX)
#ans >>> 24

#25
def is_happy(n):
    s = [int(i) for i in str(n)]
    if (s[0]+s[1]+s[2] == s[3]+s[4]+s[5]):
        return True
    return False

max = 0
c = 0
for n in range(111111, 119020):
    if (is_happy(n)):
        c+=1
        max = n # ну типо мы идем от минимального до максимального => последнее нужное число is_happy и будет max
print(c,max)
'''
#27
f = open('Задание_27_A__asf6.txt')
n = int(f.readline())
s = 0
md = 100000000000000000
for i in range(n):
    a,b = [int(s) for s in f.readline().split()]
    s += max(a,b)
    diff = abs(a-b)
    if diff % 7 != 0:
        md = min(md,diff)

if s % 7 != 0:
    print(s)
else:
    print(s-md)
# ans A = 150214
# ans B = 52303520
