'''
现在有两个无环单链表，若两个链表的长度分别为m和n，请设计一个时间复杂度为O(n + m)，
额外空间复杂度为O(1)的算法，判断这两个链表是否相交。

如果没有 空间复杂度限定，就使用hashmap 检查

给定两个链表的头结点headA和headB，请返回一个bool值，代表这两个链表是否相交。保证两个链表长度小于等于500。
'''

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class CheckIntersect:
    def chkIntersect(self, headA, headB):
        # write code here
        pHead1 = headA
        lengthA= 0
        while pHead1:
            lengthA+=1
            pHead1 = pHead1.next
        pHead2 = headB
        lengthB=0
        while pHead2:
            lengthB+=1
            pHead2=pHead2.next
        cur1 =headA
        cur2 = headB

        if lengthA >= lengthB:
            for i in range(lengthA-lengthB):
                cur1=cur1.next
        else:
            for i in range(lengthB-lengthA):
                cur2=cur2.next

        while cur1!=cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        # 讨巧，如果相同就返回了非空，如果不同就返回None=False
        return cur1