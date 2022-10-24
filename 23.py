'''
# exc 1 >>>>>
#+2,*5
# сколько программ, которые из 2 преобразуют 50

def f(start,finish): # показывает количество программ, которые число start --> finish
    #base
    if start == finish:
        return 1
    if start>finish:
        return 0
    #transition
    return f(start+2,finish) + f(start*5,finish)

print(f(2,50)) #ans >>> 7

#exc 2 >>>>>
#+2,*5
# сколько программ, которые из 2 преобразуют 50
# НЕ ПРОХОДЯТ через число 10

def f(start,finish):
    if start == finish:
        return 1
    if start > finish:
        return 0
    if start == 10:
        return 0

    return f(start+2,finish)+f(start*5,finish)

# exc 3 >>>>>
# +2,*5
# сколько программ, которые из 2 преобразуют 50
# ПРОХОДЯТ через число 10
def f(start,finish,flag):
    if start == finish:
        return 1
    if start > finish:
        return 0

    if start > 10 and flag == False: # soryan, takoe ne katit
        return 0
    # 1 способ записи >>>
#    if start == 10:
#        x = f(start + 2, finish, True)
#        y = f(start * 5, finish, True)
#   else:
#        x = f(start + 2, finish, flag)
#        y = f(start * 5, finish, flag)
#    return x+y

    # 2 способ записи, более короткий >>>
    if start == 10:
        flag = True

    x = f(start + 2, finish, flag)
    y = f(start * 5, finish, flag)
    return x+y

print(f(2,50,False)) #сначала мы стоим в 2 и не проходим через 10
''' # Рекурсия от крабов до крабоедов

"""# 1
def f(x,y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x+1,y) + f(x+2,y) + f(x*3,y)
print(f(3,9) * f(9,14))

# 2
def f(x, y):
    if x > y: return 0
    if x == y: return 1
    return f(x + 1, y) + f(x * 2, y)
print(f(1, 10) * f(10, 20))""" # Лучший способ решения !!!














































