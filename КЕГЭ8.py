'''
#7
a = 86*0.9+48*0.7+120*0.4+145*0.2+120*0.45
a *= 1024*8
print(a/180224)

#17
f = open('Задание_17__9va3.txt')
#x = f.readlines()
n = 100000
a = []
for i in range(n):
    a.append(int(f.readline()))

c = 0
maxim = -100000000000
for i in range(n-2):
    if (a[i]+a[i+1]+a[i+2])%13 == 0 and  (a[i]+a[i+1]+a[i+2])%17 == 0:
        c+=1
    if (a[i]*a[i+1]*a[i+2]) % 1589 == 0:
        if (a[i] * a[i + 1] * a[i + 2]) > maxim:
            maxim = (a[i]*a[i+1]*a[i+2])
print(c,maxim)
#505 813745968

def ravno(s,ss):
    if (s.count('A') == ss.count('A')):
        if (s.count('B') == ss.count('B')):
            if (s.count('C') == ss.count('C')):
                return True
    return False

f = open('Задание_24__9va1.txt')
s = f.readline()
a = s.split('=')
c = 0
for i in range(len(a)-1):
    x = a[i]
    y = a[i+1]
    if (ravno(x,y)):
        c+=1
print(c)
#2595

#25 числа палиндромы в троичной СС
def troich(t):
    x = t
    s = ''
    while x>0:
        s = str(x%3)+s
        x = x//3
    return s

def is_polindrom(s): #НО МОЖНО ПРОШЕ!!!
    n = len(s)
    for i in range(n):
        if s[i] != s[n-1-i]:
            return False
    return True

for i in range(600,1001):
    if(troich(i) == troich(i)[::-1]): #проверка на полиндром в одной строке без функций? ВАУ!!!
        print(i,'   ',troich(i))
    #if(is_polindrom(troich(i))): #через функцию
    #    print(i,'   ',troich(i))

#26
f = open('Задание_26__9v9w.txt')
n = int(f.readline())
k3,k4=0,0
for i in range(n):
    x = int(f.readline())
    if(x%2==0):
        k4+=1
    else:
        k3+=1
if(k4>k3):
    print('YES',k4)
else:
    print('No',k3)
#No 349

#27 НЕЭФФЕКТИВНАЯ
f = open('Задание_27B__9va4.txt')
#x = f.readlines()
n = int(f.readline())
a = []
for i in range(n):
    a.append(int(f.readline()))

c = 0
for i in range(n):
    for j in range(i+1,n):
        if a[i]*a[j]%39 == 0:
            c+=1
print(c)

#1 >> 19
#2 >> 145971277 полжизни

#27 ЭФФЕКТИВНАЯ
f = open('Задание_27B__9va4.txt')
#x = f.readlines()
n = int(f.readline())
a = []
k3,k13,k39=0,0,0
nk = 0
ans = 0
for i in range(n):
    x = int(f.readline())
    a.append(x)
    if x%39==0:
        ans+= k39+k13+k3+nk
        k39+=1
    elif x%13==0:
        ans+= k3+k39
        k13+=1
    elif x%3==0:
        ans+= k13+k39
        k3+=1
    else:
        ans+=k39
        nk+=1
print(ans)
'''


