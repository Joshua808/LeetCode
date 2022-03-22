# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 19:57:07 2021
My Solution fo leetcode #67
@author: Joshua
"""
from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #iterative
        # prev, curr = None, head
        #
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev

        #recursive

        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead


a=Solution()
a.reverseList([1,2,3,4,5])