'''
    #ЗАДАНИЕ 2
#1
print('x y z|F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = (not(z) and x) or (x and y)
            if f == True:
                print(x,y,z,f)
#2
print('a b c|F')
for a in range(2):
    for b in range(2):
        for c in range(2):
            F = not(a) or (b and not(c))
            if F == False:
                print(a,b,c,int(F))

print('x y z|F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = (x or y) <= (z == x)
            if f == 0:
                print(x,y,z,int(f))
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x == (w or y)) or ((w <= z) and (y <= w))
                if f == 0:
                    print(x,y,z,w,int(f))

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x <= y ) == (y <= z)) and (y or w)
                if f == 1:
                    print(x,y,z,w,int(f))
'''  # ЗАДАНИЕ 2
"""c = 0
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                for x5 in range(2):
                    for x6 in range(2):
                        for x7 in range(2):
                            for x8 in range(2):
                                f = 12323
                                if f == 1:
                                    print(x1,x2,x3,x4,x5,x6,x7,x8)
                                    c += 1
print(c)"""

'''
    #ЗАДАНИЕ 15
#ALGORITHM

def f(x,y,A):
    return сюда вписываем лог. функцию

for A in range(разумный диапазон):
    GG = True
    for x in range(разумный диапазон):
        for y in range(размуный диапазон):
            if(f(x,y,A) == False:
                GG = False
                break 
        if GG == False:
            break
    if GG == True:
        это подходящее A, выведем его на экран
        print(A)

# прототип 1
# min A - ? #ANS >>> 21
for A in range(-100,100):
    GG = True
    for x in range(0,100):
        for y in range(0,100):
            if ((5*x+3*y != 60) or ((A > x) and (A > y))) == False:
                GG = False

    if (GG == True):
        print(A)

#прототип 2
# del(m,n)
#maxA - ? #ANS >>> 12
for A in range(1,100):
    GG = True
    for x in range(1,100):
        if ((not(x%18 == 0)) <= ((not(x%A == 0)) <= (not(x%12 == 0)))) == False:
            GG = False
    if GG == True:
        print(A)

#прототип 3
# P = [2,10], Q = [6,14]
# max_len_A - ? #ANS
def f(x,A): # отрезки и ретерним функцию
    P = [2,10]
    Q = [6,14]
    return (inn(x,A) <= inn(x,P)) or (inn(x,Q))

def inn(x,A):   # создаем функцию, которая принимает массив с началом и концом отрезка
    return (x>=A[0]) and (x<=A[1])

maxim = 0
for a in range(0,20):
    for b in range(a,20):
        A = [a,b] #перебираем граници отрезка A
        GG = True
        for x in range(1,100):
            if(f(x,A) == False):
                GG = False
                break
        if GG == True:
            dlina = A[1]-A[0]
            if dlina > maxim:
                maxim = dlina
print(maxim)

#прототип 4
#count A - ?
def f(x,y,A):
    return ((y * y < A) <= (y <= 8)) and ((x <= 5) <= (x * x <= A))

c = 0 #каунтер
for A in range(0,100):
    GG = True
    for x in range(0,100):
        for y in range(0, 100):
            if f(x,y,A) == False:
                GG = False
                break
        if GG == False:
            break
    if GG == True:
        c+=1
print(c)

# прототип 5
# наибольшее количество элементов в A
def f(x,A):
    P = [2,4,6,8,10,12,14,16,18,20]
    Q = [3,6,9,12,15,21,24,27,30]
    return ((x in A) <= (x in P)) or ((not(x in Q)) <= (not(x in A)))

ans = []
for elem in range(50):
    A = [elem]
    GG = True
    for x in range(50):
        if f(x,A) == False:
            GG = False
            break
    if GG == True:
        ans.append(elem)
print(len(ans))


#сложный прототип 6

P1, P2 = 10, 40
Q1, Q2 = 5, 15
R1, R2 = 35, 50
minim = 1000000000000000
for A1 in range(1, 200):
    for A2 in range(A1 + 1, 200):
        GG = True
        k = 3
        for x in range(1, 200):
            x /= k
            f = ((A1<=x<=A2) or (P1<=x<=P2)) or ((Q1<=x<=Q2) <= (R1<=x<=R2))
            if f == False:
                GG = False
                break
        if GG == True:
            minim = min(abs(A1 - A2), minim)
print(minim)
'''  # ЗАДАНИЕ 15 ВСЕ ПРОТОТИПЫ
"""P1, P2 = 1, 39
Q1, Q2 = 23, 58
maxim = 0
for A1 in range(1,100):
    for A2 in range(A1+1,100):
        GG = True
        for x in range(1,300):
            x /= 3
            f = ((P1<=x<=P2) <= (not(Q1<=x<=Q2))) <= (not(A1<=x<=A2))
            if f == False:
                GG = False
                break
        if GG == True:
            maxim = max(A2-A1,maxim)
print(maxim)

maxim = 0
P1, P2 = 15, 30
Q1, Q2 = 5, 60
for A1 in range(1, 150):
    for A2 in range(A1 + 1, 150):
        GG = True
        for x in range(-400, 400):
            x /= 2
            f = ((not (Q1 <= x <= Q2)) or (P1 <= x <= P2)) and (A1 <= x <= A2)
            if f == True:
                GG = False
                break
        if GG == True:
            maxim = max(maxim, A2 - A1)
print(maxim)
P1, P2 = 130, 171
Q1, Q2 = 150, 185
minim = 10e16

for A1 in range(1,400):
    for A2 in range(A1+1, 400):
        gg = True
        for x in range(1,400):
            x += 0.1
            f = ((P1 <= x <= P2) <= (((Q1 <= x <= Q2) and not(A1 <= x <= A2)) <= (not(P1 <= x <= P2))))
            if f == 0:
                gg = False
                break
        if gg == True:
            minim = min(minim, A2-A1)
print(minim)

"""  # 15 ОТРЕЗКИ
"""minim = -1000000
for A1 in range(-100,100):
    for A2 in range(A1+1, 100):
        GG = True
        for x in range(-100,100):
            x += 0.1
            f = ((A1<=x<=A2) <= (x**2 - 16*x <= 57) ) and ( (x**2 - 21 <= 4*x) <= (A1<=x<=A2) )
            if f == False:
                GG = False
        if GG == True:
            minim = max(A2-A1,minim)
print(minim)

for a in range(1, 1000):
    GG = True
    for x in range(1, 1000):
        f = (a % 7 == 0) and ((240 % x == 0) <= ((a % x != 0) <= (780%x != 0)))
        if f == 0:
            GG = False
    if GG == True:
        print(a)
        
        
for A in range(1,1000):
    GG = True
    for x in range(1,1000):
        if((((x&13!=0) or (x&39==0)) <= (x&13!=0)) or ((x&A==0) and (x&13==0))) == False:
            GG = False
    if (GG == True):
        print(A)
#maxA=47


for A in range(1,100):
    GG = True
    for x in range(1,100):
        for y in range(1,100):
            if ((x+(y*13/9) >= A) or (x<y) or (y<7))== False:
                GG = False
                break
        if(GG == False):
            break
    if (GG == True):
        print(A)
#maxA=17


for A in range(1,100):
    GG = True
    for x in range(1,100):
        for y in range(1,100):
            if (((x+y/6)>A) or (x<18/27) or (y<5)) == False:
                GG = False
                break
        if GG==False:
            break
    if(GG==True):
        print(A)


for A in range(1,100):
    GG =True
    for x in range(1,100):
        for y in range(1,100):
            if ((6*x+10*y != 240) or (A>x) or (A>=y)) == False:
                GG = False
                break
        if GG == False:
            break
    if GG == True:
        print(A)
        break
"""  # 15 НЕРАВЕНСТВА
'''
P = {2,4,6,8,10,12,14,16,18,20}
Q = {3,6,9,12,15,18,21,24,27,30}
A = set ()
for x in range(1,100):
    f = ((x in P) <= (x in A)) or ((x not in A) <= (x not in Q))
    if f == 0:
        A.add(x)
print(A,sum(A))

P = {1,3,7}
Q = {1,2,4,5,6}
A = set ()
for x in range(-100,100):
    f = (x not in A) <= (x not in P) or ((x not in Q) and (x in P))
    if f == 0:
        A.add(x)
print(A,len(A))

P = {1,12}
Q = {12,13,14,15,16}
A = set ()
for x in range(-100,100):
    f = (x not in A) <= ((x not in P) and (x not in Q))
    if f == 0:
        A.add(x)
ans = 1
for i in A:
    ans *= i
print(A,ans)
'''  # 15 ЧИСЕЛКИ
"""P1, P2 = 10, 45
Q1, Q2 = 35, 78
len = 999999
for A1 in range(-100, 100):
    for A2 in range(A1+1, 100):
        gg = 1
        for x in range(-100, 100):
            F = ((not(P1 <= x <= P2)) <= (Q1 <= x <= Q2)) and (not(A1 <= x <= A2))
            if F == 1:
                gg = 0
                break
        if gg == 1:
            len = min(len, A2-A1)
print(len)"""
"""
c = 0
for x1 in range(2):
    for x2 in range(2):
        for x3 in range(2):
            for x4 in range(2):
                for x5 in range(2):
                    for x6 in range(2):
                        for x7 in range(2):
                            f = x1 or not x2 or (x3 and not x4) or not x5 or (not x6 and not x7)
                            if f == 0:
                                c += 1
print(c)"""

"""def f(x, A):
    return (x % A != 0) <= ((x % 6 == 0) <= (x % 9 != 0))


for A in range(1, 1000):
    if (all(f(x, A) for x in range(1, 1000))):
        print(A)
"""
"""p1, p2 = 0, 10
q1, q2 = 25, 50
maxim = 100000

k = 3
for A1 in range(0, 100):
    for A2 in range(A1+1, 100):
        gg = True
        for x in range(0, 100):
            x += 0.1
            f = (not(A1 <= x <= A2)) <= ((not(p1 <= x <= p2)) and (not(q1 <= x <= q2)))
            if f == 0:
                gg = False
        if gg == True:
            maxim = min(maxim, A2-A1)
print(maxim)""" # x += 1