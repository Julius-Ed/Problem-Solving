

def maxProduct(nums) -> int:

    min_prod = 1
    max_prod = 1

    global_max = max(nums)

    for index in range(len(nums)):

        if nums[index] == 0:
            max_prod = 1
            min_prod = 1

        temp = max_prod
        max_prod = max(max_prod * nums[index],
                       min_prod * nums[index], nums[index])
        min_prod = min(temp * nums[index], min_prod * nums[index], nums[index])

        if max_prod > global_max:
            global_max = max_prod

    return global_max
