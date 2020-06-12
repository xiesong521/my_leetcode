#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        stack = []
        cur = head

        while cur.next or cur.child or stack != []:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                child = cur.child
                cur.child = None
                cur.next = child
                child.pre = cur
                cur = cur.child
            elif cur.next:
                cur = cur.next
            else:
                stack_item = stack.pop()
                cur.next = stack_item
                stack_item.pre = cur
                cur = cur.next
        return head


# 上边是我写的代码，搞不懂为啥不对呢，感觉跟下边的没啥不一样呀


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        cur = head
        temp = []
        while cur.child or cur.next or temp != []:
            if cur.child:
                if cur.next:
                    temp.append(cur.next)
                t = cur.child
                cur.child = None
                cur.next = t
                t.prev = cur
                cur = cur.next
            elif temp != [] and cur.next == None:
                t = temp.pop()
                cur.next = t
                t.prev = cur
                cur = cur.next
            else:
                cur = cur.next
        return head
