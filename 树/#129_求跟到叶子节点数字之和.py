#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.getPathNumSum(root, 0)
    def getPathNumSum(self, root, num):
        if not root:
            return 0
        currentNum = root.val + 10 * num
        if root.left == None and root.right == None:
            return currentNum
        left = self.getPathNumSum(root.left, currentNum)
        right = self.getPathNumSum(root.right, currentNum)
        return left + right

