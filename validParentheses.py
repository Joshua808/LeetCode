# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 17:58:53 2021

@author: Joshua
"""

class Solution:
    def isValid(self, s: str) -> bool:
        open_list = ["(","[","{"]
        close_list = [")","]","}"]
        track_open = [] 
        print(s)
        
# =============================================================================
#  iterarting through every character in the string       
# =============================================================================
        for x in s:
            print("current character is ", x)
# =============================================================================
#             if the character is an open bracket, log it
# =============================================================================
            if x in open_list:
                print("added", x , " to track_open")
                track_open.append(x)
# =============================================================================
#                 if character is in the close bracket, check to see if it matches order, if it does delete last item in list, if not return False
# =============================================================================
            if x in close_list:
                
# =============================================================================
#                 If there is no opening character when a closing character is detected, return false
# =============================================================================
                if not track_open:
                    return False
                
                
                print("found closing character", x)
# =============================================================================
#                 if ] is found, makes sure that [ is at the end of the track_open, if it is, delete it and move on, if not return false]
# =============================================================================
                if x == "]":
                    if track_open[-1] == "[":
                        print("found  ]")
                        track_open.pop()

                    else:
                        print("mismatch with [")
                        return False
                    
                if x == ")":
                    print("found )")
                    if track_open[-1] == "(":
                        track_open.pop()

                    else:
                        print("mismatch with (")
                        return False    
                    
                if x == "}":
                    if track_open[-1] == "{":
                        print("found }")
                        track_open.pop()

                    else:
                        print("mismatch with }")
                        return False    
                    
# =============================================================================
#                 at the end of track_open is empty, all closing characters matched the correct order, return true
#               if track_open still contains stuff, there was a missing closing character
# =============================================================================
        if not track_open:
            return True
        else:
            print("did not find closing character", track_open)
            return False
a=Solution()