'''
请编写一个函数，检查链表是否为回文。
给定一个链表ListNode* pHead，请返回一个bool，代表链表是否为回文。

测试样例：
{1,2,3,2,1}
返回：true
{1,2,3,2,3}
返回：false
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 额外空间复杂度为O(n)
class Palindrome:
    def isPalindrome(self, pHead):
        # write code here
        stack = []
        headNode = ListNode(0)
        headNode.next=pHead
        while pHead:
            stack.append(pHead.val)
            pHead = pHead.next
        pHead = headNode.next
        for i in range(len(stack)):
            if pHead.val != stack.pop():
                return False
            else:
                pHead = pHead.next
        return True
# 额外空间复杂度为O（N/2)

class Palindrome1:
    def isPalindrome(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return True
        stack = []

        pHead1 = pHead
        pHead2 = pHead

        # 边界有先后顺序，奇偶情况的边界有别，当pHead已经为None时就直接退出
        while pHead1 and pHead1.next:
            stack.append(pHead2.val)
            pHead2 = pHead2.next
            pHead1 = pHead1.next.next if pHead1.next else None
        if pHead1:
            pHead2 = pHead2.next

        while pHead2:
            if pHead2.val != stack.pop():
                return False
            else:
                pHead2= pHead2.next

        return True if len(stack)==0 else False