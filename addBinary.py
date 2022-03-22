# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 19:57:07 2021
My Solution fo leetcode #67
@author: Joshua
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length_a = len(a)
        length_b =len(b)
        a_value = 0
        b_value = 0
# =============================================================================
#         convert a into numerical form
# =============================================================================
        for x in a:
            print(x)
            if x =="1":
                a_value += pow(2,length_a-1)
                print("adding to a: ", a_value)
            length_a += -1
            
# =============================================================================
#             convert b into numerical form
# =============================================================================
        for y in b:
            print(y)
            if y=="1":
                b_value += pow(2,length_b-1)
                print("adding to b: ", b_value)
            length_b += -1
        
        
        c_value = a_value + b_value
        
        
        c_value = format(c_value,"b")
        
        
        
        
        return c_value
    

a=Solution()