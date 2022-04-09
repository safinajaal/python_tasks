"""
Дан массив целых чисел nums. Найти количество чисел, у которых четное число цифр в записи числа.
Пример:
Дано: nums = [12,345,2,6,7896]
Результат: 2
"""

def findNumbers(nums):
    count=0
    for i in range(len(nums)):
        numberList=list(str(nums[i]))
        if len(numberList)%2==0:
            count+=1
    print(count)    

findNumbers([12,345,2,6,7896])