"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 1:
            return False
        
        return self.isPowerOfTwo(n/2)



Sol = Solution()

print(Sol.isPowerOfTwo(2))



#Input: n = 1
#Output: true
#Explanation: 20 = 1