'''
Дан массив целых чисел candies, на i месте в котором находится количество конфет у i ребенка. Также дано целое число extraCandies. Необходимо для каждого ребенка проверить: если дать ему extraCandies, будет ли у него больше всего конфет?

Примечание: Одновременно может быть несколько детей с одинаково большим количеством конфет.

Пример 1:

Дано: candies = [2,3,5,1,3], extraCandies = 3
Результат: [true,true,true,false,true]
Пример 2:

Дано: candies = [12,1,12], extraCandies = 10
Результат: [true,false,true]
'''

def kidsWithCandies(candies, extraCandies):
    maxCandies=max(candies)
    result=[]
    for value in candies:
        extraValue=value+extraCandies
        if extraValue >=maxCandies:
            result.append(True)
        else:
            result.append(False)
    print(result)

kidsWithCandies([12,1,12], 10)