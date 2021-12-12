# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 18:47:48 2021

@author: Joshua
"""
# =============================================================================
# 
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         
#         haystack_index = -1
#         dummy = -1
#         needle_index = -1
#         
#         if needle == "":
#             return 0
#         
#         if len(haystack) < len(needle):
#             return -1
#         
#         if needle == haystack:
#             return 0
# 
#         for x in haystack:
#             
#             dummy+=1
#             haystack_index = dummy
#             
#             for y in needle:
#                 
#                 haystack_index = dummy
#                 needle_index +=1
# 
#                 
#                 while haystack[haystack_index] == needle[needle_index]:
#                    
#                    haystack_index +=1
#                    needle_index +=1
# 
#                    if needle_index >= len(needle):
#                        return dummy
#                    
#                    if haystack_index >= len(haystack):
# 
#                        return -1
#                    
#     
# 
#                 needle_index = -1
#                 break
#                             
#                 
# 
#         return -1
# a = Solution()
# 
# =============================================================================

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        haystack_index = -1
        dummy = -1
        needle_index = -1
        
        if needle == "":
            return 0
        
        if len(haystack) < len(needle):
            return -1
        
        if needle == haystack:
            return 0

        for x in haystack:
            dummy += 1
            
            if haystack[dummy:dummy+len(needle)] == needle:
               return dummy
                            
                

        return -1
a = Solution()