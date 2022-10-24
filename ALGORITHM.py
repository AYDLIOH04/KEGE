'''
#КВАДРАТ
#Просто квадрат 29.12.2021 2:42
n = int(input())
a = [[0]*n for i in range(n)]

print('  ',end='')
for i in range(n):
    print('j',end=' ')
print()

for i in range(len(a)):
    print('i',end=' ')
    for j in range(len(a[i])):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 1
        print(a[i][j],end=' ')
    print()
'''
'''
n,m = map(int,input().split())
A = []
for i in range(n):
    A.append(list(map(int,input().split())))
print(A)
'''
'''
SOLO = [int(i) for i in input().split()]
print(SOLO)
DUO = [list(map(int,input().split())) for i in range(int(input()))]
print(DUO)
'''
'''
n = int(input()) + 1
GENERATOR = [[i * j for j in range(n)] for i in range(n)]
print(GENERATOR, end='\n\nТабличка умножения\n')
for i in range(1, n):  # от 1, чтоб в моей табличке не было нулей))
    for j in range(1, n):
        print(GENERATOR[i][j], end='\t')
    print()
'''
