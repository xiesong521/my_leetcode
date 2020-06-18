#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p== None and q == None:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        else:
            left = self.isSameTree(p.left,q.left)
            right = self.isSameTree(p.right,q.right)
            return left and right
