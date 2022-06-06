a = [1.1, 1.2, 3.1, 5, 10.01]
for i in range(0, len(a)):
    a[i] = a[i] % 1
print(a)
maxA = 0
minA = 1
for i in range(0, len(a)):
    if maxA < a[i]:
        maxA = a[i]
    if minA > a[i]:
        minA = a[i]
print(maxA - minA)