"""
Given an integer array nums, return true if any value appears at 
least twice in the array, and return false if every element is distinct.
"""

from collections import Counter


def containsDuplicate(nums) :
        
    count_ocurrences_dict = Counter(nums)

    for num in count_ocurrences_dict:
        if count_ocurrences_dict[num] > 1:
            return True

    return False

print(containsDuplicate([1,2,3]))