"""
O(N)
"""


def maxSubArray(nums):

    max_subarray = nums[0]
    current_sum = 0


    for candidate_number in nums:
        if current_sum < 0:
            current_sum = 0
        
        current_sum += candidate_number

        max_subarray = max(max_subarray, current_sum)
    
    return max_subarray