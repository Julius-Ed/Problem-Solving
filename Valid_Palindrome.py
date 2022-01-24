
from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        lst = deque([])

        for char in s:
            char = char.lower()
            if 97 <= ord(char) <= 122 or 48 <= ord(char) <= 57:
                lst.append(char)

        while lst:
            left = lst.popleft()

            if len(lst) == 0:
                return True
    
            right = lst.pop()

            if left != right:
                return False

        return True

Sol = Solution()

print(Sol.isPalindrome("A man, a plan, a canal: Panama"))