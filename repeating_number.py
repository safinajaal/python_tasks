'''
Дан массив nums, в котором содержится n+1 чисел в промежутке [1, n]. В массиве nums есть только одно число, которое повторяется несколько раз. Выведите это число.
Пример:

Дано: nums = [1,2,4,3,2]
Результат: 2
'''

def numRepeat(nums):
    
    for i in range(max(nums)):
        numCount=nums.count(nums[i])
        if numCount>1:
            print(nums[i])
            break

numRepeat([1,2,4,3,2])
