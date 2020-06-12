#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
# class Solution:
#     def sortedListToBST(self,head):
#         if not head:
#             return head
#         mid = self.midNode(head)
#         root = TreeNode(mid.val)
#         if head == mid:
#             return root
#         root.left = self.sortedListToBST(head)
#         root.right = self.sortedListToBST(mid.next)
#         return root
#
#     def midNode(self,head):
#         prev = None
#         fast = head
#         slow = head
#         while fast and fast.next:
#             prev = slow
#             slow = slow.next
#             fast = fast.next.next
#         if prev:
#             prev.next = None
#         return slow


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return head
        res = []
        while (head):
            res.append(head.val)
            head = head.next
        root = self.sortedarrayToBST(res)
        return root

    def sortedarrayToBST(self,res):

        mid = len(res) / 2
        root = TreeNode(res[mid])
        root.left = self.sortedarrayToBST(res[:mid])
        root.right = self.sortedarrayToBST(res[mid + 1:])
        return root



