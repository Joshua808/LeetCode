# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 19:31:21 2021

@author: Joshua
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        words = s.split()
        
        length_of_last_word = len(words[-1])
        
        return length_of_last_word
    

a=Solution()

        