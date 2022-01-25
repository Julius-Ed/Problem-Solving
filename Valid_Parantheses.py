
from distutils.log import error


class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        c_dict = {"]":"[", "}":"{", ")":"("}

        for c in s:
    
            if c not in c_dict:
                stack.append(c)
            
            elif stack and stack[-1] == c_dict[c]:
                stack.pop()
            
            else:
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False




Sol = Solution()

print(Sol.isValid('()]{}'))

"""
Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""