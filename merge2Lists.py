# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:53:27 2021

@author: Joshua
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
         
         
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list =[]
        x=0
        y=0



        while len(list1) > x and len(list2) > y:
            print("This is x ", x)
            print("this is y ", y)
            
            if list1[x] <= list2[y]:
                merged_list.append(list1[x])
                x+=1
            
            else:
                merged_list.append(list2[y])
                y+=1

        
        if len(list1) > x:            
            merged_list.append(list1[x])
            x+=1
        
        if len(list2) > y:            
            merged_list.append(list2[y])
            y+=1
                
        
        
        return merged_list


    def mergeTwoLinkedLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2
        if list2 is None:
            return list1
    
        if list1.val < list2.val:
            temp=head=ListNode(list1.val)
            list1 = list1.next
        
        else:
            temp=head=ListNode(list2.val)
            list2 = list2.next
            
        while list1 is not None and list2 is not None:
        
            if list1.val < list2.val:
                temp.next = list1.val
                list1 = list1.next
               
            else:
                temp.next = list2.val
                list2 = list2.next
             
        while list1 is not None:
            temp.next = list1.val
            list1 = list1.next
            
        while list2 is not None:
            temp.next = list2.val
            list2 = list2.next
            
        return head
          

a = Solution()