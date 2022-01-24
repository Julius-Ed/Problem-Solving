class Solution:
    def search(self, nums, target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid
        return - 1


Sol = Solution()

print(Sol.search([5, 1, 3], 3))
print(Sol.search([4,5,6,7,0,1,2], 2))