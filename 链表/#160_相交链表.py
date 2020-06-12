#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        A_length = self.getListLength(headA)
        B_length = self.getListLength(headB)

        sub_length = abs(A_length - B_length)

        if A_length > B_length:
            while(sub_length != 0):
                headA = headA.next
                sub_length -= 1
        if A_length < B_length:
            while(sub_length != 0):
                headB = headB.next
                sub_length -= 1
        while(headA and headB):
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None

    def getListLength(self,head):
        count = 0
        while(head):
            count += 1
            head = head.next
        return count
