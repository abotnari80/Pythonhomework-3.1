def getSumOdds(aList):
    sum = 0
    for i in range(0, len(aList)):
        if i%2 != 0:
            sum = sum + aList[i]
    return sum

array = [1,3,25,2,7]
result = getSumOdds(array)
print(result)