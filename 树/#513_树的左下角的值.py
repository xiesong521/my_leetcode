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
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def dfs(root,depth):
            if not root:
                return
            if depth > self.maxdepth:
                self.maxdepth = depth
                self.ret = root.val
            dfs(root.left,depth+1)
            dfs(root.right,depth+1)
        self.maxdepth,self.ret = -1, 0
        dfs(root,0)
        return self.ret