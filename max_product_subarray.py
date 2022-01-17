"""
Given an integer array nums, find a contiguous non-empty subarray within the array 
that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.
"""


def maxProduct(nums) -> int:


    min_prod = 1
    max_prod = 1

    global_max = max(nums)

    for index in range(len(nums)):
    
        if nums[index] == 0:
            max_prod = 1
            min_prod = 1

        temp = max_prod
        max_prod = max(max_prod * nums[index], min_prod * nums[index], nums[index])
        min_prod = min(temp * nums[index], min_prod * nums[index], nums[index])

        if max_prod > global_max:
            global_max = max_prod

    return global_max
        




print(maxProduct([-4, -3, -2])) 

