#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        Node_list = []
        current = head
        pos = -1
        while(current):
            if current not in Node_list:
                Node_list.append(current)
            else:
                pos = Node_list.index(current)
                break
            current = current.next
        return current
