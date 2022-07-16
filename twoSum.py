

def twoSum(nums, target):
    lacking = {}
    for i, number in enumerate(nums):
        if i != (len(nums)-1):
            sumOfActualAndNext = number+nums[i+1]
            if (target - sumOfActualAndNext) == 0:
                return [i, (i+1)]
        try:
            index = lacking[number]
            return [index, i]
        except KeyError:
            lacking[(target-number)]=i
            continue

print(twoSum([-3,4,3,90],0))