"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

"""



class SolutionBruteForce:
    def smallerNumbersThanCurrent(self, nums):
        result = []
        for i in range(len(nums)):

            counter = 0
            for j in range(len(nums)):

                if nums[j] < nums[i]:
                    counter += 1
            result.append(counter)

        return result

class SolutionLn:
    def smallerNumbersThanCurrent(self, nums):

        num_dict = {}

        sorted_arr = sorted(nums)

        for index in range(len(sorted_arr)):
            if sorted_arr[index] not in num_dict:
                num_dict[sorted_arr[index]] = index
        
        for index in range(len(nums)):
            nums[index] = num_dict[nums[index]]
        
        return nums

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        buckets = [0] * (max(nums) + 1)
        
        for num in nums:
            buckets[num] += 1
            
        previous = 0    
        for i, bucket in enumerate(buckets):
            if bucket != 0:
                buckets[i] = previous 
                previous += bucket 

        return [buckets[num] for num in nums]