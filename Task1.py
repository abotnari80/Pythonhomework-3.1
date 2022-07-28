#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
#стоящих на нечётной позиции.

def getSumOdds(aList):
    sum = 0
    for i in range(0, len(aList)):
        if i%2 != 0:
            sum = sum + aList[i]
    return sum

array = [1,3,5,9,3]
result = getSumOdds(array)
print(result)