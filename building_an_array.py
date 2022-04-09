'''
Дан упорядоченный массив target и целое число n. На каждой итерации Вы будете считывать одно число из набора list = {1, 2, ..., n}. Необходимо сконструировать массив из команд "Push" и "Pop", которые позволят из list получить target. Если на какой-то итерации Вы получили target, то нужно остановить вычисления.
Пример 1:
Дано: target = [1,3], n = 3
Результат: ["Push","Push","Pop","Push"]
Объяснение:
Считываем число 1 и помещаем его в массив target ("Push") -> [1]
Считываем число 2, помещаем в массив target ("Push") и вынимаем ("Pop") -> [1]
Считываем число 3 и помещаем его в массив target ("Push") -> [1, 3]
Требуемый массив target получен, необходимый набор команд: ["Push", "Push", "Pop", "Push"]
Пример 2:
Дано: target = [1, 2, 3], n = 3
Результат: ["Push", "Push", "Push"]
Пример 3:
Дано: target = [1, 2], n = 4
Результат: ["Push", "Push"]
Объяснение:
Для формирования массива target достаточно считать всего 2 числа. После этого вычисления останавливаются.
'''

def buildArray(target,n):
    resultArray=[]
    for i in range (1,n+1):
        resultArray.append('Push')
        if len(resultArray)!=len(target):
            if i not in target:
                resultArray.append('Pop')
            else:continue
        else:break
    print(resultArray)

buildArray([1, 2],4)