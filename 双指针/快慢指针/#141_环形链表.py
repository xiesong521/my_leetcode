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
#计数法
class Solution:
    def hasCycle(self,head):
        hashset = []
        while(head):
            if head in hashset:
                return True
            else:
                hashset.append(head)
            head = head.next
        return False
#快慢指针
class Solution:
    def hasCycle(self,head):
        if head == None:
            return False
        fast = head
        low = head

        while(fast):
            if fast.next and fast.next.next:
                fast = fast.next.next
                low = low.next
            else:
                return False
            if fast == low:
                return True
if __name__ == '__main__':

    l1 = ListNode(3)
    l2 = ListNode(2)
    l3 = ListNode(1)
    l4 = ListNode(5)
    # l5 = ListNode(3)
    # l6 = ListNode(2)
    # l7 = ListNode(1)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l1
    # l5.next = l6
    # l6.next = l7
    s = Solution()
    ret,re,_ = s.hasCycle(l1)
    print(ret,re)

