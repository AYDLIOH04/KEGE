#2
print('x y z|f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = (not x or y or (not z)) and (not x == (not y or z))
            if f == 1:
                print(x,y,z,int(f))