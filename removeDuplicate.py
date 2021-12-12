# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 22:34:19 2021

@author: Joshua
"""
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> list:
        length = len(nums)
        print(length-1)
        duplicate = []
        
        for x in range(length):
            current = nums[x]
            
            if x != (length-1):
                if nums[x+1]==current:
                   duplicate.append(nums[x+1])
        
        print(duplicate)
        for y in duplicate:
            nums.remove(y)
        
        return len(nums)

a = Solution()