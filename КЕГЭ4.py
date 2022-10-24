
#задание 12
a = ("1"*39) + ("2"*14)
print(a)
print(a.count("1"),a.count("2"))
while ("11" in a) or ("2" in a):
    while("12" in a):
        a = a.replace("12","11",1)
    if ("11" in a):
        a = a.replace("11", "2", 1)
    elif ("2" in a):
        a = a.replace("2", "0", 1)
print(a)
print(a.count("0"))

#задача 16
def G(n):
    if n < 4:
        return n+1
    elif n>3:
        return G(n-2)+G(n-3)

def F(n):
    if n < 3:
        return n
    elif n>2:
        return F(n-1) + G(n-2)
print(F(7) + G(5))

#задача 17
f = open('17__7n8u.txt')
n = 20000 #находим через x=f.readlines() , print(len(x))
a = []
c = 0
max = -10000000000
for i in range(n):
    a.append(int(f.readline()))

for i in range(n-1):
    if ((a[i]%6==0 or a[i]%7==0) and a[i]>1000)\
            or ((a[i+1]%6==0 or a[i+1]%7==0) and a[i+1]>1000) :
        c+=1
        if a[i]*a[i+1]>max:
            max = a[i]*a[i+1]
print(c,max)  #ВЕРНОЕ РЕШЕНИЕ!!!!!!!!!!!
#4754 97740230

#задание 22
for i in range(1000):
    L = 0
    M = 0
    print(i)
    while i > 0 :
        if i % 2 == 0 :
            L = L + 1
        else :
            M = M + i%6
        i = i // 6
    if L == 2 and M == 5:
        print("      ",L,M)

#задание 24.1
f = open('24__7n8n.txt')
s = f.readline() #print(len(s))
g = 0
c = 0
for i in range(len(s)-1):
    if s[i]!=s[i+1]:
        c+=1
    else:
        c=0
    if c>g:
        g=c
print(g) #НЕВЕРНОЕ РЕШЕНИЕ!!

#задача 24.2
f = open('24__7n8n.txt')
s = f.readline() #print(len(s))
n = len(s)
maxim = 1 #тк первый символ уже входит в объект
c = 1
for i in range(1,n):
    if(s[i]!=s[i-1]):
        c += 1
        if c>maxim:
            maxim = c
    else:
        c=1
print(maxim)

#задание 25.1 МОЕ
for i in range(84684,84741): #про +1 не забываем
    a = [int(x) for x in str(i)] #цифры числа в массив
    b = a[0]+a[1]+a[2]+a[3]+a[4]
    if i%b ==0:
        print(i)

#задание 25.2 АР
x,s = 0,0
for i in range(84684,84741):
    x = i
    s = 0
    while x>0:
        s+=x%10
        x//=10
    if i%s==0:
        print(i)

#задание 27A,B
#f = open('ну крч мне впадлу было качать файл, поэтому')
#считываем цифры из файла и назначаем их в 3 переменные
#но я не качал файл, поэтому просто введу их
#А - 40,12,14
#B - 12349,342,346
a,b,c = 12349,342,346
d = c-b
while(b>0):
    b = b-d #так мы дойдем до нулевого члена прогрессии - первого неположительного
b = b+d
k = 1
s = 0
while k<a:
    b = b+d
    k = k+1
    if k%2==0:
        s+=b
print(s)
