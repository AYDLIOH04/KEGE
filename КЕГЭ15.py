# 2
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x == (not(y))) <= ((x and w) == z)
                if f == 0:
                    print(x,y,z,w,int(f))
#6
for i in range(-100,100):
    s = 1
    k = 0
    n = i
    while s + n < 155:
        s = 4*s
        k += n
    if k == 88:
        print(i)
        break

#12
a = '8'*1000
while '999' in a or '888' in a:
    if '888' in a:
        a = a.replace('888','9',1)
    else:
        a = a.replace('999', '8', 1)
print(a)

#14
c = 0
a = 5**14 + 25**3 - 117
while a>0:
    if a%5 == 4:
        c+=1
    a//=5
print(c)

# 15
dlin = 100
for a in range(1, dlin):
    GG = True
    for x in range(1, dlin):
        f = (x % a == 0) <= ((x % 21 != 0) or (x % 35 == 0))
        if f == 0:
            GG = False
            break
    if GG == True:
        print(a)
        break

#16
def f(n):
    if n <= 2:
        return n*2
    return  f(n-2) + g(n-2)

def g(n):
    if n <= 3:
        return n
    return g(n-1) + f(n-2)*f(n-2)
print(f(6) + g(8))

f = open('KEK15.txt')
#a = [int(i) for i in f]
a = [2,423,999,69,213,15]
n = len(a)
c = 0
for i in range(n-1):
    if (a[i] + a[i+1]) % 6 == 0 \
            and (a[i] + a[i+1]) % 9 != 0 \
            and (a[i] + a[i+1]) % 10 == 2:
        c = +1
for i in range(n):
    for j in range(n):

print(c,pmax*maxim)

#19-21
def moves(h):
    a,b = h
    return (a+1,b+2),(a*2,b),(a,b*2)

def f(h):
    if sum(h) >= 41:
        return 'END'
    if any(f(x) == 'END' for x in moves(h)):
        return 'P1'
    if all(f(x) == 'P1' for x in moves(h)):
        return 'V1'
    if any(f(x) == 'V1' for x in moves(h)):
        return 'P2'
    if all(f(x) == 'P2' or f(x) == 'P1' for x in moves(h)):
        return 'V2'

for s in range(1,35):
    h = 8,s
    print(s,f(h))

#h = 8,11
#print(f(h))

#23
def f(s,f,GG):
    if s == f:
        return 1
    if s > f:
        return 0

    if s > 10 and GG == False:
        return 0

    if s == 10:
        flag = True
    return f(s + 1, f, GG) + f(s + 5, f, GG) + f(s**2, f, GG)

print(f(2,50,False))

for i in range(1,30000):
    x = i
    L,M = 0,0
    while x > 0:
        M = M + 1
        if x % 2 == 0:
            L = L + M
        x = x // 10
    if L == 9 and M == 5:
        print(i)
'''

