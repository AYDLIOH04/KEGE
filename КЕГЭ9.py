'''
#6
for i in range(-1000,1000):
    s = i
    n = 30
    while s<1000:
        s = s+5
        n = n-9
    if (n+s) == -230:
        print(i)

#14
c = 0
a = 125**91+25**43-5**120-11
while a>0:
    if a%5 == 4:
        c+=1
    a//=5
print(c)
#otvet >>> 238

#15
for A in range(1,100):
    GG = True
    for x in range(1,100):
        if (((x&29!=0) and (x&18!=0)) <= ((x&A!=0) and (x&29!=0))) == 0:
            GG = False
    if(GG == True):
        print(A)
#otvet >>> 18

#16
def F(n):
    if n <= 2:
        return n+2
    else:
        return F(n-1)+G(n-1)
def G(n):
    if n<= 2:
        return n+1
    else:
        return G(n-1)+F(n-2)

y = (G(4)+G(3))**0.5
print((16*y)**0.5 + 10)
#otvet >>> 18

#17
min = 10000000
f = open('Задание_17__afjn.txt')
n = 100000
c = 0
a = [int(i) for i in f]
for i in range(n-1):
    if (a[i]+a[i+1])%21 == 0:
        c+=1
        if (a[i]*a[i+1]) < min:
            min = (a[i]*a[i+1])
print(c*2,min)
#otvet >>> 9592 83

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

#25 типо максимальный делитеть палиндром
def is_palindrom(n):
    s = str(n)
    if(s == s[::-1]):
        return True
    else:
        return False

def one_of_divs_palindrom(n):
    pal = False
    for j in range(11,n+1):
        if(n%j==0):
            if(is_palindrom(j)):
                pal = j
    return pal

a = 12345
b = 12425

for i in range(a,b+1):
    if(one_of_divs_palindrom(i)!=False):
        print(i,one_of_divs_palindrom(i),end=", ")
'''
#26



























