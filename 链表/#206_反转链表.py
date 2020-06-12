#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
#definition for singly-linked list
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        left = None
        current = head
        right = None
        while (current):
            right = current.next
            current.next = left
            left = current
            current = right
        print(left.next.val)

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l1.next = l2
l2.next = l3
l3.next = l4
s = Solution()
s.reverseList(l1)

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution():
    def reversedlist(self,head):
        left = None
        current = head
        right = None
        while(current):
            right =current.next
            current.next = left
            left = current
            current = right
        return left
    def biabli(self,head):
        current = head
        while(current):
            print(current.val)
            current = current.next
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l1.next = l2
l2.next = l3
s  = Solution()
new_head = s.reversedlist(l1)
s.bianli(new_head)

