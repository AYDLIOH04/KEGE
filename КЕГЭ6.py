'''
#2
print('x y z | F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = ((x<= (not(y))) <= (not(z))) == (x and (not(y)))
            if F==1:
                print(x,y,z,int(F))

#6
for s in range(1000):
    i = s
    n = 5
    while s>0:
        s//=2
        n = n+s+1
    if n == 132:
        print(i)

#12
a = '>' + ('1'*15) + ('2'*20) + ('3'*8)
print(a)
while ('>1' in a) or ('>2' in a) or ('>3' in a):
    if ('>1' in a):
        a = a.replace('>1','41>',1)
    if ('>2' in a):
        a = a.replace('>2','5>',1)
    if ('>3' in a):
        a = a.replace('>3','44>',1)
print(a)
a = a.replace('>', '0', 1)
print(a)
c = 0
for i in a:
    i = int(i)
    c+=i
print(c)

#14
c = 0
a = 27**9 - 2*(9**5) - 3**3
while a>0:
    if a%3==2:
        c+=1
    a//=3
print(c)

#15
for A in range(1,100):
    GG = True
    for x in range(1, 100):
        if ((x&A != 0) <=((x&14==0)<= (x&3!=0))) == False:
            GG = False
            break
    if GG == True:
        print(A)

#16
def G(n):
    if n <= 1:
        return n+1
    elif n>1:
        return G(n-2)+F(n-2)+n

def F(n):
    if n <= 3:
        return n*n
    elif n>3:
        return F(n-2) + G(n-1)*F(n-3)
print((F(5) + G(4))**0.5)

#17
f = open('17__8pne.txt')
a = []
min = 100000000000000000
c = 0
n = 10000
for i in range(n):
    a.append(int(f.readline()))
for i in range(n-1):
    if (a[i] < 40) and (a[i+1] < 40) and (a[i]%3==0 or a[i+1]%3==0):
        c+=1
        if a[i]+a[i+1] < min:
            min = a[i]+a[i+1]
print(c,min)

#22
for x in range(100000000):
    i = x
    a = 1
    b = 0
    while x>0:
        a=a*(x%4)
        b = b+1
        x = x//4
    if a*b==42:
        print(i)
        break
#5467
'''
#24
