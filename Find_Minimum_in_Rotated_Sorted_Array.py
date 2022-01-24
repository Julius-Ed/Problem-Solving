class Solution:
    def findMin(self, nums) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if l == r:
                return nums[0]

            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return min(nums[0], nums[mid + 1])
            
            if nums[l] < nums[mid]:
                l = mid
            else:
                r = mid

        return nums[0]
        
Sol = Solution()
print(Sol.findMin([1, 2, 3]))
print(Sol.findMin([3, 1, 2]))
print(Sol.findMin([3,4,5,1,2]))
print(Sol.findMin([0,1,2,4,5,6,7]))
print(Sol.findMin([11,13,15,17]))
print(Sol.findMin([4, 5, 1, 2, 3]))