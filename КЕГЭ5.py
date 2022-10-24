"""
import math
a = int(input())
b = int(input())
print((a**2+b**2)**0.5)
print(math.sqrt(a**2+b**2))

    #ВАРИАНТ 5
#задача 6
for s in range(200):
    n=1
    print(s,end=" ")
    while s>0:
        s=s-n-1
        n = n*2+1
    print(n)
#126

#задача 12
a = ('492'*143)
while ('49' in a) or ('2222' in a):
    a = a.replace('49','2',1)
    a = a.replace('2222','2',1)
print(a)

#задача 14
a = 2**20+4**15-2**3-12
c = 0
while a>0:
    if a%2==1:
        c+=1
    a//=2
print(c)

#задача 16
def f(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 3
    elif n>3:
        return f(n-1)+f(n-3)
print(f(8))

#задача 17
f = open('17__86bc (1).txt')
#x=f.readlines()
#print(len(x))
n = 10000
a = []
count = 0
min = 100000000000000
ans = 0
for i in range(n):
    a.append(int(f.readline()))
for i in range(n-1):
    if a[i]>50 or a[i+1]>50:
        count+=1
        if a[i]+a[i+1]<min:
            min = a[i]+a[i+1]
            ans = min*(max(a))

print(count,ans)

#задание 22
c = 0
for x in range(255):
    a = 0
    b = 1
    print(x,end=" ")
    while x>0:
        a+=1
        b=b*(x%16)
        x//=16
    if a==2 and b==30:
        c+=1
    print(" ",a,b)
print(c)
"""

