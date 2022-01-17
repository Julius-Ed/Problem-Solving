"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product 
of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed 
to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) 
time and without using the division operation.
"""


def productExceptSelf(nums) -> list:

    prod = 1
    prod_without_zeros = 1
    zero_counter = 0

    for num in nums:
        prod *= num

        if num == 0:
            zero_counter += 1
        else:
            prod_without_zeros *= num

    if zero_counter == 0:

        for i in range(len(nums)):
            nums[i] = prod // nums[i]

        return nums

    if zero_counter > 1:

        for i in range(len(nums)):
            nums[i] = 0
        return nums

    for i in range(len(nums)):

        if nums[i] != 0:
            nums[i] = 0
        else:
            nums[i] = prod_without_zeros

    return nums


def productExceptSelf(nums) -> list:

    prefix = [0] * len(nums)
    suffix = [0] * len(nums)
    result = [0] * len(nums)

    acc = 1
    for index, num in enumerate(nums):

        acc *= num
        prefix[index] = acc

    acc = 1
    for index in range(len(nums) - 1, -1, -1):

        acc *= nums[index]
        suffix[index] = acc

    for i in range(len(nums)):

        if i == 0:
            result[i] = suffix[i + 1]
            continue
        if i == len(nums) - 1:
            result[i] = prefix[i - 1]
            break

        result[i] = prefix[i-1] * suffix[i+1]

    return result
