# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 16:43:02 2021
Kadane's Algorithm'
@author: Joshua
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
# =============================================================================
#         Iteirate through the list
# =============================================================================
        for i in range(1, len(nums)):
# =============================================================================
#               always start with positive number
# =============================================================================
            if nums[i-1] > 0:
# =============================================================================
#                 add previous number
# =============================================================================
                nums[i] += nums[i-1]
        
                print(nums)
        return max(nums)


a=Solution()