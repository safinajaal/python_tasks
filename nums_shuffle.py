'''
Дан массив целых чисел nums размерности 2n. Элементы массива расположены в следующем порядке: [x1,x2,...,xn,y1,y2,...,yn]. Необходимо преобразовать массив к виду [x1,y1,x2,y2,...,xn,yn].

Пример:

Дано: nums = [2,5,1,3,4,7], n = 3
Результат: [2,3,5,4,1,7]
'''


def shuffle(nums, n):
    
    num1=nums[0:n]
    num2=nums[n:len(nums)+1]
    num3=[]
    
    for i in range(n):
        num3.append(num1[i])
        num3.append(num2[i])
    
    print(num3)
    
   

shuffle([2,5,1,3,4,7], 3)