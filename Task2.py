a = [1,3,5,2,4]
x = 0
y = len(a) - 1
while (x < y):
    print(a[x]*a[y], end=' ')
    x = x + 1
    y = y - 1
if (x == y):
    print(a[x]*a[y])