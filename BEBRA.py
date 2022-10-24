# AYDL1OH
# include <iostream>

# Всякое
"""alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
message = input("Сообщение для шифровки: ").upper()
for j in range(1,20):
    smeshenie = j
    itog = ''
    for i in message:
        mesto = alfavit_EU.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit_EU:
            itog += alfavit_EU[new_mesto]
        else: itog += i
    print(itog)"""  # Щифр Цезаря
import time

"""import win10toast

toast = win10toast.ToastNotifier()
toast.show_toast(title= 'БЭэбра...', msg='Ты в муте животное', duration= 10)"""  # Уведомляйзер
"""
from collections import Counter # Счетчик букв

def anagram(str1, str2): # Анаграмма - словосочетание из одинх и тех же букв
    if Counter(str1) == Counter(str2):
        return True
    return False

print(anagram('бЭбра', 'Эббар'))
print(anagram('Лох', 'лох'))"""  # Анаграмма
"""s = 'PyTHon is A veRy good lanGuAge!'
print(s.title()) # Python Is A Very Good Language!
print(s.upper()) # PYTHON IS A VERY GOOD LANGUAGE!
print(s.lower()) # python is a very good language!"""  # Изменение регистра строки
"""s = 'Pyth On very good           '
print(s.strip())
"""  # Удаление лишних пробелов
"""s = "Python!"
print(list(s))
"""  # Строку в массив
"""numbers = ['maxim', 2, 2, 3, 3, 'maxim', 3, 'maxim', 4, 5, 'maxim', 6, 6]

    # Stupid решение
def most_common_stupid(list):
    return max(set(list), key = list.count)

print(most_common_stupid(numbers))

    # Smart решение
from collections import Counter

def most_common_smart(list):
    data = Counter(list)
    return data.most_common(1)[0][0]

print(most_common_smart(numbers))
"""  # Элемент в списке, появляющийся чаще всего
"""def non_recurring(list):
    if len(list) == len(set(list)):
        return True
    return False

a = [i for i in input().split()]
print(f'{a} уникальный >>> {non_recurring(a)}')"""  # Проверка списка на уникальность
"""a = [1, 2, 3, 4, 4, 4, 'lena', 'lena']
print(list(set(a)))
"""  # Делаем массив уникальным
"""a = [1, 2, 3, '', 0, 0, ' ']
print(list(filter(bool, a)))
"""  # Очистка массива от None и 0 значений
"""def diff(list1, list2):
    return list(set(list1).symmetric_difference(list2)) # разница в симметрии

a = [1, 2, 3, 5]
b = [1, 2, 3, 6]
print(diff(a, b))"""  # Разница между двумя списками

# Интересные функции и модули
"""
def list_error(error):
    match error:
        case 400:
            return 'Bad request'
        case 404:
            return 'Not found'
        case 401 | 402 | 403:
            return 'hz chto napisat'
        case _:
            return 'What?'

print(list_error(402))
 

x = int(input())
y = int(input())
point = x, y
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y = {y}")
    case (x, 0):
        print(f"X = {x}")
    case (x, y):
        print(f"X = {x}, Y = {y}")
    case _:
        raise ValueError("Not a point")
"""  # match (аналог switch)
"""a = 100
if a < 50:
    print('OK')
else:
    raise ValueError('Very BIG')

while True:
    try:
        a = int(input())
        print('Ваш ответ записан!')
        break
    except ValueError: print('Ошибка: Введите число!')
"""  # raise, try except (обработки ошибок)
"""import bisect
a = [1, 2, 3, 4, 5, 6, 67, 7, 123123, 12323, 98978, 1231231923, 9999000]
a.sort()
print(67 == a[bisect.bisect(a, 67)-1])"""  # Встроенный Бин-поиск (import bisect)
"""from numba import njit
from datetime import datetime

@njit()
def f():
    c = 0
    n = 10000
    for i in range(n):
        for j in range(n):
            if i * j % 3 == 0:
                c += 1
    return c


st = datetime.now()
print(f())
print(datetime.now() - st)

# 0:00:01.143201 с @njit
# 0:00:55.781836 без @njit
# Очевидно...
 """  # from numba import njit >>> оптимизация влож. циклов в 100 РАЗ!!!

# CodeWars
"""def reverse_str(string):
    return ' '.join(string.split()[::-1])
print(reverse_str('qwerty 123 qweeqeqwe'))"""  # Реверс слов в строке
"""
def get_planet_name(id):
    return {1:"Mercury", 2:"Venus", 3:"Earth", 4:"Mars", 5:"Jupiter", 6:"Saturn", 7:"Uranus", 8:"Neptune"}[id]
"""  # Вывод планет по индексу (как метод match)
"""def count_sheeps(sheep):
    return sheep.count(True)
print(count_sheeps([True, True, True, False,
                    True,  True, True, True,
                    True,  False, True, False,
                    True,  False, False, True,
                    True,  True,  True,  True,
                    False, False, True,  True
                    ]))"""  # Овцы
"""def format_money(amount):
    return f'${amount:.2f}'
for i in range(0,10):
    for j in range(0,10):
        i += 0.11
        print(format_money(i))"""  # Формат денег (округление)
"""def create_array(n):
    return [i for i in range(1, n+1)]
print(create_array(5))"""  # генератор массива
"""def build_string(*args):
    return f"I like {', '.join(args)}!"
print(build_string('Cheese','Milk','Chocolate'))"""  # Сочетания функции формата и join
"""def weather_info(temp):
    c = convert_to_celsius(temp)
    if (c < 0):
        return (str(c) + " is freezing temperature")
    else:
        return (str(c) + " is above freezing temperature")


def convert_to_celsius(fareng):
    celsius = (fareng - 32) * (5 / 9)
    return celsius"""  # Из фаренгейта в цельсию
"""def get_grade(s1, s2, s3):
    return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) / 30, 'F')

def gett_grade(*s):
    return 'FFFFFFDCBAA'[sum(s)//30]"""  # перевод оценок A,B,C по ср.значению трех баллов (Очень интересные способы)
"""def combine_names(f, l): 
    return f'{f} {l}'
print(combine_names("James", "Stevens"))
"""  # Фамилия + Имя
"""def stringy(size):
    if size % 2 == 0:
        return '10'* (size//2)
    return '10' * (size//2) + '1'

def string(size):
    return ('10' * size)[:size]
print(string(3))"""  # }{ня сложная
"""def two_decimal_places(n):
    return float(f'{n:.2f}')
print(two_decimal_places(4.575757))

def two_two_two(n):
    return round(n, 2)
print(two_two_two(4.575757))"""  # Округление через строчку и через функцию
"""def most_frequent_item_count(collection):
    c = 0
    for i in set(collection):
        c = max(c, collection.count(i))
    return c
print(most_frequent_item_count([5, -7, 10, -5]))


def chto_chto(collection):
    return max([collection.count(i) for i in set(collection)] + [0])
print(chto_chto([5, -7, 10, -5]))"""  # Кол-во макс. встречающихся чисел


"""# gcd, ncd
# 50, 25
# 25, 25
# 0, 25

# 34, 14
# 6, 14
# 6, 2
# 0, 2

def gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a %= b
        else:
            b %= a
    return max(a, b)


def ncd(a, b):
    return a * b / gcd(a, b)


# НОД(a,b) * НОК(a, b) = a * b
# НОК(a, b) = a * b / НОД(a,b)

print(ncd(25, 50))""" # Алгоритм Евклида



