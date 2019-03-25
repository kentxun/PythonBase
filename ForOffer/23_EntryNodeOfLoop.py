'''
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return
        Fast = pHead
        Slow = pHead

        while Fast and Fast.next:
            Fast = Fast.next.next if Fast.next else None
            Slow = Slow.next
            if Fast == Slow:
                Fast=pHead
                while Fast!= Slow:
                    Fast = Fast.next
                    Slow = Slow.next
                return Fast