# CC
num = 8
dvoich = bin(num)[2:]
vosmerich = oct(num)[2:]
shesterich = hex(num)[2:]
print(dvoich,vosmerich,shesterich)

print(int('1111',2))
print(int(dvoich,2), int(vosmerich,8), int(shesterich,16))

print(dvoich,vosmerich)
# ПРИКОЛЬНАЯ КОНСТРУКЦИЯ
n = 98
print(True if n % 2 == 0 else False)
print(n if n % 5 == 0 else 'OOOOPS')
'''
      #ЧТО-ТО

n = int(input())
for i in range(n):
    a = int(input())
    if a < 0:
        print('Встретилось отрицательное число', a)
        break
else:
    print('Ни одного отрицательного числа не встретилось')

#abs - модуль
#[x % 10 == 0 for x in range(2, 100) if x >= 10] <действия>,<для чего применяется>,<условие>

#Ввод двух (или более) переменных через пробел >>>
a,b = map(int,input().split())

def f(n): #факториал
    if n == 1:
        return 1
    return f(n-1)*n

#поиск дробного числа в списке(если есть, то выводит FALSE)
def proverka(a):
    if all(x%1 == 0 for x in a):
        return True
    return False
a = [float(i) for i in input().split()]
print(proverka(a))

#ЭМОДЖИ?!
from emoji import emojize
print(emojize(":thumbs_up:"))

#ввод чисел в массив в одну строчку
l=[int(i) for i in input().split()]

s,n = map(int,input().split())
#хз что
from random import *
n = uniform(100,999)
print(n)
#Без округления
print("Разрвернутая запись числа: ",int(n/100//1*100),'+',
      int(n//10%10*10),'+',int(n%10/1),'+',((n*10//1)%10)/10)
#Если с округлением
a = [int(x) for x in str(round(n*10))]
print("Разрвенутая запись числа: ",a[0]*100,'+',
      a[1]*10,'+',a[2],'+',a[3]/10)

#максимальное и минимальное из введенных
print(min(int(input()),int(input()),int(input())))
print(max(int(input()),int(input()),int(input())))

#задача по нахождению максимального произведения двух любых введенных чисел(не по порядку)
a=[]
for i in range(int(input())):
    a.append(int(input())) #вводим в массив числа
x=max(a) #находим первый максимум
a.remove(x) #удаляем первый максимум из массива
print(x*max(a)) #умножаем старый максимум на новый и получаем ответ

#проверка элементов массива на их тип(str,int)
from itertools import product
for j in product(['A','B',5,6,7],repeat=4):
    if (type(j[0]) == str) and (type(j[1]) == int)\
            and (type(j[2]) == str) and (type(j[3]) == int):
        print(*j,sep='')
'''
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    #Способы перебора элементов
# функция "list" для МАССИВА
print(list('12345qwe'))
a = [i for i in input().split()]
print(list(reversed(a))) # перебор с конца
# функция "tuple" для КОРТЕЖА
print(tuple('12345qwe'))

# Работа с числами массива
n = [int(i) for i in input().split()]
print(sum(n))   #сумма элементов
print(max(n))   #макимальный элемент
print(min(n))   #минимальный элемент
print(sorted(n))#сортировка по возрастанию
print(sorted(n,reverse=True)) #соритровка по убыванию

# any&all применимо в функциях
print(all([False,True,False])) #возвращает True, если все элементы истинные
print(any([False,True,False])) #возвращает True, если хотяб 1 элемен истинный

#ord, chr
print(ord('a'))
print(chr(97))

#запись чего-то
a=int(input())
print('The next %s is %s.' %(a,next))
print('The previous %s is %s.' %(a,a-1))
#конструктор
a = [1,2,3,5,1,1.4,123]
GG = any([print(False) for x in a if type(x) == float])
'''
#FIBONACHI рекурсия и адекватное решение
def f(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return f(n-1) + f(n-2)
print(f(int(input())))

while True:
    n = int(input())
    if n == 0:
        print(0)
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        print(b)
'''
