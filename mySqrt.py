# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 20:20:37 2021
My solution to leetcode problem 69
@author: Joshua
"""

# =============================================================================
# Brute Force Implementation
# =============================================================================
# =============================================================================
# 
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         
#         last_number = 0
#         current_number = -1
#         current_sq = 0
#         last_sq =0
#         
#         while True:
#             
#             current_number +=1
#             
#             current_sq = current_number * current_number
#             
#             if current_sq == x:
#                 return current_number
#             
#             if current_sq > x and last_sq < x:
#                 
#                 return last_number
#             
#             else:
#                 last_number = current_number
#                 last_sq = current_sq
#     
# =============================================================================

# =============================================================================
# Brute force binary search method
# =============================================================================
# =============================================================================
# 
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         
#         start = 1
#         end = x
#         mid = 0
#         counter =0
#         
#         while (start <= end):
#             counter +=1
#             mid = (start + end) // 2
#             print("this is the mid", mid)
#             print("this is the start", start)
#             print("this is the end", end)
#             
#             if mid*mid == x:
#                 return mid
#             
#             if mid*mid > x:
#                 end = mid
#             
#             else:
#                 start = mid
#             
#             if counter >= 32
#                 return mid
#             
#         return mid
# =============================================================================


class Solution:
    def mySqrt(self, x: int) -> int:
        
        start = 1
        end = x
        mid = 0
        
        while (start <= end):
            mid = (start + end) // 2
            print("this is the mid", mid)
            print("this is the start", start)
            print("this is the end", end)
            

            if mid*mid > x:
                end = mid - 1
            
            elif mid*mid < x:
                start = mid +1
            
            else:
                return mid
        
        return end
            

a=Solution()