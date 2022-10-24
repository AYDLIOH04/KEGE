"""maxim = 0
ans = 0
for i in range(100, 10000):
    s = i * '1'
    while '111' in s or '88888' in s:
        if '111' in s:
            s = s.replace('111', '88', 1)
        else:
            s = s.replace('88888', '8', 1)
    if s.count('8') > maxim:
        maxim = s.count('8')
        ans = i
print(ans) # 102""" # Длина строки из 1 не меньше 100. Найти мин. количество единиц в начале, чтоб было макс число восьмерок
"""s = 3 * 64 ** 1073 - 2 * 16 ** 1131 + 4 ** 1173 - 484
ans = ''
while s > 0:
    ans = str(s%4) + ans
    s //= 4
maxim = 0
minim = 10000000
for i in range(4):
    j = str(i)
    maxim = max(ans.count(j), maxim)
    minim = min(ans.count(j), minim)
print(maxim-minim)""" # В 4 СС. Найти разность суммы самых частых и суммы самых нечастых чисел

