'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点）。
'''
# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        # 链表为空
        if not pHead:
            return pHead

        current = pHead
        # 第一遍遍历链表，复制每个元素，添加在原来后面
        while current:
            node = RandomListNode(current.label)
            node.next = current.next
            current.next = node
            current = current.next

        # 第二遍遍历链表，同时遍历两个链表,current 是复制的元素
        pre = pHead
        while pre :
            current = pre.next
            if pre.random :
                current.random = pre.random.next # 复制结点的random 等于 原本结点的random指向的结点的下一个（复制结点）
            pre = pre.next.next

        # 分流两个链表
        newHead = pHead.next
        pre =pHead  #原节点
        current = newHead #复制节点

        #分成了两个链表
        while pre:
            if pre.next.next:
                pre.next=pre.next.next
                current.next=current.next.next
            else:
                pre.next=None
                current.next=None
            pre = pre.next
            current = current.next
        return newHead