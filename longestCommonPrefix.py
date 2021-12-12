# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 18:53:57 2021

@author: Joshua
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        sorted_strs = sorted(strs, key=len)
        c=0
        
        for x in sorted_strs[0]:
            sorted_strs[0]= sorted_strs[0].replace('"', " ")
            first_word = sorted_strs[0]
            pre = first_word[:c+1]
            prefix.append(pre) 
            c+=1
        
        if len(sorted_strs) == 1:
           return sorted_strs[0] 
        
        if len(sorted_strs[0]) == len(sorted_strs[1]):    
            prefix.pop()
    
        d = len(prefix) - 1

 
        for y in sorted_strs:                   
            while prefix[d] != y[0:len(prefix[d])]:
                prefix.pop()

                d = len(prefix) - 1     

                if d == -1:
                    return ""
                
        d = len(prefix) - 1        
        return prefix[d]                
a=Solution()            
        
        
        
        
        
        
     