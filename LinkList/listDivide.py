'''
对于一个链表，我们需要用一个特定阈值完成对它的分化，使得小于等于这个值的结点移到前面，
大于该值的结点在后面，同时保证两类结点内部的位置关系不变。

给定一个链表的头结点head，同时给定阈值val，请返回一个链表，
使小于等于它的结点在前，大于等于它的在后，保证结点值不重复。

测试样例：
{1,4,2,5},3
{1,2,4,5}
'''

# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Divide:
    def listDivide(self, head, val):
        # write code here
        # 边界情况 空链表或只有一个节点
        if not head or head.next is None:
            return head

        # 设置临时
        node = head
        Min = None
        Minhead = None
        Max = None
        Maxhead = None

        # 循环条件，node不为空，将列表拆开为 两部分
        while node:
            if node.val <= val:
                if Min == None:
                    Minhead = node
                else:
                    Min.next = node
                Min = node
            else:
                if Max == None:
                    Maxhead = node
                else:
                    Max.next = node
                Max = node
            node = node.next
        # 再合并列表
        if Min == None:
            head = Maxhead
        elif Max == None:
            head = Minhead
        else:
            Min.next = Maxhead
            Max.next = None
            head = Minhead
        return head
