

def singleNumberOld(nums):
    nums.sort()

    i = 0
    while i < len(nums) - 1:

        if nums[i] == nums[i + 1]:
            i += 2
            continue
    
        if nums[i] != [i + 1]:
            return nums[i]


    return nums[i]

def singleNumber(nums):
    n = nums[0]
    
    for i in range(1, len(nums)):
        n = n^nums[i]
            
    return n