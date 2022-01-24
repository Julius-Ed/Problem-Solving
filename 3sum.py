"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such 
that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
"""

class Solution:

    def threeSum(self, nums):

        res = []

        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                
                elif threeSum < 0:
                    l += 1
                
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l -1] and l < r:
                        l+= 1
        
        return res


Sol = Solution()

print(Sol.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))