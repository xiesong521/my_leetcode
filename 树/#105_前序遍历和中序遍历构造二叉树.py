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
    def buildTree(self, preorder, inorder) :
        if preorder == [] or inorder == []:
            return None
        root = preorder[0]
        pos = inorder.index(root)
        root = TreeNode(root)
        left_inorder = inorder[0:pos]
        right_inorder = inorder[pos+1 :]
        left_preorder = preorder[1:pos+1]
        right_preorder = preorder[pos+1 :]
        root.left = self.buildTree(left_preorder,left_inorder)
        root.right = self.buildTree(right_preorder,right_inorder)
        return root
