# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 18:37:59 2021

@author: Joshua
"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        counter = 0
        
        for x in nums:
            if x == val:
                counter +=1
        
        for y in range(counter):
            nums.remove(val)
            
        
        return len(nums)


a = Solution()