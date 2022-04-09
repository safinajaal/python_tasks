"""
Дан массив целых чисел nums. Необходимо посчитать количество «хороших пар». Пара (i, j) называется хорошей, если:

nums[i] == nums[j]
i < j
Пример 1:
Дано: nums = [1,2,3,1,1,3]
Результат: 4
Пример 2:
Дано: nums = [1,1,1,1]
Результат: 6
Пример 3:
Дано: nums = [1,2,3]
Результат: 0
"""

def numIdenticalPairs(nums):
    good=0
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i]==nums[j] and i<j:
                good+=1
    print(good)
        
numIdenticalPairs([1,2,3,1,1,3])