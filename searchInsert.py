# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 19:26:32 2021

@author: Joshua
"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        length = len(nums)
        
        start = int(length/2)
        
   
        
        while nums[start] > target:
            if start == 0:
                return 0
            start +=-1
            
        while nums[start] < target:
            if start+1 == length:
                return length
            start +=1
        
            
        return start
        
    

a=Solution()