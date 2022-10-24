c = 0
for i in range(10, 1001):
    n = bin(i)[3:]
    if '1' in n:
        while n[0] != '1':
            n = n[1:]
    b = int(n, 2)
    print(i - b)
    c += 1
print(c)