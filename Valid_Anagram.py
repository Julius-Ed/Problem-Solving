from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        char_hash_map = Counter(list(s))


        for char in t:
            
            if char_hash_map[char] < 1:
                return False
            else:
                char_hash_map[char] -= 1
        
        total = sum(char_hash_map.values())

        if total == 0:
            return True
        else:
            return False



Sol = Solution()
print(Sol.isAnagram("anagram", "anargam"))



"""
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""