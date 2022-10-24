from itertools import permutations #перестановки (буквы ТОЛЬКО ОДИН РАЗ)
from itertools import combinations #сочетания (БЕЗ ПОВТОРЯЮЩИХСЯ)
from itertools import product      #декартовое произведение (буквы СКОЛЬКО УГОДНО РАЗ)
from itertools import combinations_with_replacement
"""
for j in combinations('ABD',2):
    print(*j,sep="",end=" ")
print()
for j in permutations('ABD',2):
    print(*j,sep="",end=" ")
print()
for j in product('ABD', repeat = 2):
    print(*j, sep="", end=" ")
    
# A B D двухбуквенные
#combinations >>> AB AD BD - ЭЛЕМЕНТЫ БЕЗ ПОВТОРЕНИЙ
#permutations >>> AB AD BA BD DA DB - перебор (БУКВЫ БЕЗ ПОВТОРЕНИЙ)
#product >>> AA AB AD BA BB BD DA DB DD - полный перебор

s = [[1,2,3],[4,5,6],[7,8,9]]
for i in s:
    for j in i:
        print(j,end=' ')
    print()


#print(list(permutations([1,2,3]))) #перестановки кортежей

ans = 0
for j in permutations([1,2,3,4,5]): 
    print(j)
    ans+=1
print(ans) #5!
"""
"""
#задача 1:
# Артем составляет все возможные пятибуквенные слова из букв ARTEM
# при этом каждую букву можно использовать ровно один раз.
# Сколько существует таких слов, в которых вторая буква - R или T?

ans = 0                             #если ручками, то >>> 4*2*3*2*1 = 48
for j in permutations("ARTEM"):
    if(j[1] == "R" or j[1] == "T"):
        ans+=1
print(ans)

#задача 2:
# Артем составляет все возможные пятибуквенные слова из букв ARTEM
# при этом каждую букву можно использовать ровно один раз.
# Сколько существует таких слов, в которых вторая буква - R или T?
# а последняя обязательно R или A?

ans = 0                             #если ручками, то >>> 3*1*2*1*2 = 12
for j in permutations('ARTEM'):     #                     3*1*2*1*1 = 6
    if(j[1] == 'R' or j[1] == 'T') and (j[4] == 'R' or j[4] == 'A'):
        ans+=1
print(ans)

#задача 3:

# Артем составляет все возможные пятибуквенные слова из букв ARTEM
# при этом каждую букву можно использовать ровно один раз.
# Сколько существует таких слов, в которых буквы A и E стоят рядом?

ans = 0                         #ручками >>> AE*3*2*1 всего позиций для AE - 4, для EA тоже 4 => 3*2*1*(4+4)
for j in permutations("ARTEM"):
    for i in range(4):
        x = j[i]
        y = j[i+1]
        if(x=='A' and y=='E') or (x=='E' and y=='A'):
            ans+=1
            print(j)
            break
print(ans)

#задача 4

# Артем составляет все возможные ШЕСТИБУКВЕННЫЕ слова из букв ARTEM
# при этом каждую букву можно использовать СКОЛЬКО УГОДНО РАЗ.
# Сколько существует таких слов?

ans = 0                     #ручками >>> 5*5*5*5*5*5
for j in product('ARTEM',repeat=6): #(что перемножаем, repeat = сколько раз)
    ans+=1
print(ans)

#задача 5

# Артем составляет все возможные ШЕСТИБУКВЕННЫЕ слова из букв ARTEM
# при этом каждую букву можно использовать СКОЛЬКО УГОДНО РАЗ.
# Сколько существует таких слов, в которых буква A встречается ровно 2 раза?
    
ans = 0                     #ручками >>> С из6по2 = 6*5/2 = 15 => 15*4*4*4*4 = 3840
for j in product("ARTEM",repeat=6):
    if(j.count('A') == 2):
        ans+=1
print(ans)

#задача 6

# Артем составляет все возможные ШЕСТИБУКВЕННЫЕ слова из букв ARTEM
# при этом каждую букву можно использовать СКОЛЬКО УГОДНО РАЗ.
# Сколько существует таких слов, в которых буква A встречается ровно 2 раза?
# а буквы R,T,E,M не повторяются

ans = 0                     #ручками >>> С из6по2 = 6*5/2 = 15 => 15*4*3*2*1 = 360
for j in product("ARTEM", repeat=6):
    if(j.count('A') == 2):
        if(j.count('R') == 1) and (j.count('T') == 1) and (j.count('E') == 1):
            ans+=1
print(ans)

        #DZ
#1
for j in permutations('ABCDE',3):
    print(*j,sep="",end=" ")

#2
for j in permutations('ABDE25',4):
    print(*j,sep="",end=" ")

#3
for j in combinations_with_replacement('ADVF',r=3):
    print(*j,sep="",end=" ")

#4
for j in product('ADVF',repeat=3):
    print(*j,sep="",end=" ")

#5
for j in permutations('ABC',2):
    print(*j,sep="")
print()
#6
ans = 0
for j in permutations('ABDE',3):
    ans+=1
print(ans)

#7.1
for i in range(10,31):
    print(i)

#7.2
for j in product('0123456789',repeat=2):
    if j[0] != '0':
        if(j[0] == '3' and j[1] == '1'):
            break
        else:
            print(*j,sep="")

#8
ans = 0
for j in product([0,1,2,3,4,5,6,7,8,9],repeat=3):
    if 156 <= (j[0]*100 + j[1]*10 + j[2]) <= 189:
        print(*j,sep="")
        ans+=1
print(ans)
#для проверки 8
ans = 0
for i in range(156,190):
    ans+=1
print(ans)

#9
print('x y z|F')
for j in product([0,1],repeat=3):
    x,y,z = j
    F = (x <= y) and not(z)
    if F==0:
        print(x,y,z,int(F))

#10
for j in product(['A','B',5,6,7],repeat=4):
    if (type(j[0]) == str) and (type(j[1]) == int)\
            and (type(j[2]) == str) and (type(j[3]) == int):
        print(*j,sep='')

#11
for j in combinations(['Метеор','Ракета','Пушка','Искра'],2):
    if not(j[0] == "Метеор" and j[1] == 'Пушка') \
            and not(j[0] == "Ракета" and j[1] == 'Искра'):
        print(*j)

#12
for j in product('123456',repeat=3):
    print('K1:'+j[0],'K2:'+j[1],'K3:'+j[2])
""" # Задачки БАЗА
"""
import itertools
s = 'КОРАБЛИ'
A= itertools.permutations(s,6) 
n = 0
for a1 in A :
    if a1[0] in ('К','Р','Б','Л'):
        f = True
        for i in range (5):
            if a1[i] in ('О','А','И') and  a1[i+1] in ('О','А','И') or a1[i] in ('К','Р','Б','Л') and a1[i+1] in ('К','Р','Б','Л'):
                f = False
                break
        if f : n+=1
print(n)

import itertools
s = 'КАБИНЕТ'
A= itertools.permutations(s,7) 
n = 0
for a1 in A :
    s1=''
    for i in range (7): s1+= a1[i]
    if s1[0] != 'Б' and s1.count ('ЕА') == 0:
        n+=1
print(n)

import itertools
s = 'АЙСБЕРГ'
A= itertools.permutations(s,7) 
n = 0
for a1 in A :
    if a1[0] != 'Й':
        f = True
        for i in range (6):
            if a1[i] =='Й' and  a1[i+1] in ('А','Е'):
                f = False
                break
        if f : n+=1
print(n)

import itertools
s = 'АВРОРА'
A= itertools.permutations(s,6)
B = set()
for a1 in A :
    f = True
    for i in range (5):
        if a1[i]==a1[i+1]: f = False; break
    if f: B.add(a1)
print(len(B))   

import itertools
s = 'МАГИСТР'
A= itertools.permutations(s,5)
n = 0
for a1 in A:
    if a1.count('А') + a1.count('И')<=1: n+=1
print(n)

f= open('26-n1.txt','r')
N,K,M = map(int,f.readline().split())
A = []
for i in range (N):
    a = int(f.readline())
    A.append(a)
A = sorted(A,reverse = True)
print(A[M+K-1],A[K-1])

import itertools
s = 'ПИРОГ'
A= itertools.permutations(s,4) 
n = 0
for a1 in A :
    f = True
    for i in range(1,5):
        if a1.count('О')>2 and a1[i-1] in ('И','О'):
            f = False
            break
    if f: n+=1
print(n)

import itertools
s = 'АБРИКОС'
A = itertools.permutations(s,7)
n = 0
for a1 in A:
    f = True
    for i in range(6):
        if a1[i] in ('А', 'И' ,'О') and a1[i+1] in ('А', 'И' ,'О'):
            f = False
            break
    for i in range(6):
        if a1[i] in ('Б', 'Р' ,'К','С') and a1[i+1] in ('Б', 'Р' ,'К','С') :
            f = False
            break
    if f: n+=1
print(n)

import itertools
s = 'ТРАТАТА'
A = itertools.permutations(s,7)
B = set()
for a1 in A :
    B.add(a1)
print(len(B))


import itertools
s = 'ВОРОТА'
A= itertools.permutations(s,6)
B = set()
for a1 in A :
    f = True
    for i in range (5):
        if a1[i] in ('О','А') and a1[i+1] in ('О','А') : f = False; break
    if f: B.add(a1)
print(len(B))       

import itertools
s ='ЕНИСЙ'
A = itertools.product(s,s,s,s)
n = 0
for a1 in A:
    f = True
    if a1[1] == 'Й' and a1.count('Е')+a1.count('И')<1:
        f = False
        break
    if f: n+=1
print(n)

import itertools
s = 'РАЗМАХ'
A = itertools.permutations(s,6)
B = set()
for a1 in A:
    f = True
    if a1.count('Р')+a1.count('З')+a1.count('М')+a1.count('Х')<2:
        f = False
        break
    if f: B.add(a1)
print(len(B))

import itertools
s = 'URDL'
A = itertools.product(s,s,s,s,s)
n = 0
for a1 in A:
    if a1[0] != 'U' and a1[0]!=a1[2] and a1[1]!=a1[3] and a1[2]!=a1[4]:
        n+=1
print(n)

""" # Задачки СЛОЖНО

"""c = 0
for i in product('MART', repeat=6):
    if i.count('R') == 2:
        c += 1
print(c)""" # 1
"""c = 0
for s1 in 'ЖАЛЕ':
    for s2 in 'ЖАЛЕЙ':
        for s3 in 'ЖАЛЕЙ':
            for s4 in 'ЖАЛЕЙ':
                for s5 in 'ЖАЛЕ':
                    s = s1+s2+s3+s4+s5
                    if (s.count('Й') <= 1) and ('ЙЕ' not in s) and ('ЕЙ' not in s):
                        c += 1
print(c) # 1456
""" # 2.1
"""c = 0
for i in product('ZALEY', repeat=5):
    s = ''.join(i)
    if s.count('Y') <= 1 and ('YE' not in s) and ('EY' not in s) and s[0] != 'Y' and s[-1] != 'Y':
        c += 1
print(c)""" # 2.2
"""c = 0
for i in permutations('КАБИНЕТ', r=7):
    s = ''.join(i)
    if s[0] != 'Б' and 'EA' not in s:
        c += 1
print(c) """ # КАБИНЕТ
"""c = 0
a = [''.join(j) for j in product('БРКС', repeat=2)]
b = [''.join(j) for j in product('АИО', repeat=2)]
for i in permutations('АБРИКОС', r=7):
    s = ''.join(i)
    if all(j not in s for j in a) and all(m not in s for m in b):
        c += 1
print(c)""" # АБРИКОС
"""c = 0
for i in permutations('АЙСБЕРГ', r=7):
    str = ''.join(i)
    if (str[0] != 'Й') and ('ЙА' not in str) and ('ЙЕ' not in str) and ('АЙ' not in str) and ('ЕЙ' not in str):
        c += 1
print(c)""" # АЙСБЕРГ
"""c = 0
for a in permutations('АВРОРА', r=6):
    gg = True
    for j in range(len(a) - 1):
        if ord(a[j]) == ord(a[j+1]):
            gg = False
    if gg == True:
        print(a)
        c += 1
print(c)
""" # АВРОРА избегаем РР и АА
"""c = 0
for i in permutations('МАГИСТР', r=5):
    s = ''.join(i)
    if (s.count('А') + s.count('И')) < 2:
        print(s)
        c += 1
print(c)""" # МАГИСТР нельзя > 1 гласной
"""a = [''.join(j) for j in product('ОАO', repeat=2)]
print(a)
c = 0
for i in permutations('ВОРОТА', r=6):
    s = ''.join(i)
    if all(j not in s for j in a):
        print(s)
        c += 1
print(c)""" # ВОРОТА
"""c = 0
for i in product("ЕНИСЙ", repeat=4):
    s = ''.join(i)
    if s[0] != 'Й' and (s.count('Е') + s.count('И')) >= 1:
        c += 1
print(c) """ # ЕНИСЕЙ
"""c = 0
for i in product('РАЗМХ', repeat=6):
    s = ''.join(i)
    if (s.count('Р') + s.count('З') + s.count('М') + s.count('Х')) >= 3:
        c += 1
print(c)""" # РАЗМАХ
"""c = 0
for i in product('АРСЕНИЙ', repeat=4):
    s = ''.join(i)
    if s[0] != 'Й' and (s.count('А') + s.count('И') + s.count('Е')) >= 1:
        c += 1
print(c)""" # 1866
"""c = 0
for i in product('СВЕТЛАН', repeat=8):
    s = ''.join(i)
    if s.count('С') == 1 and s.count('В') == 1 and s.count('Е') == 1 \
       and s.count('Т') == 1 and s.count('Л') == 1 and s.count('А') == 2 \
       and s.count('Н') == 1 and s.count('АА') == 0:
        c += 1
print(c)""" # СВЕТЛАНА
"""c = 0
for i in product('СОТКА', repeat=5):
    a = ''.join(i)
    if (a[0] == 'А') and ('АТ' not in a) and ('ТА' not in a):
        c += 1
print(c)
""" # СОТКА без АТ и ТА











