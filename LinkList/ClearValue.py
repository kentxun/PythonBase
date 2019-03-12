'''
 第8节 链表指定值清除练习题
现在有一个单链表。链表中每个节点保存一个整数，再给定一个值val，把所有等于val的节点删掉。
给定一个单链表的头结点head，同时给定一个值val，请返回清除后的链表的头结点，
保证链表中有不等于该值的其它值。请保证其他元素的相对顺序。
测试样例：
{1,2,3,4,3,2,1},2
{1,3,4,3,1}
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ClearValue:
    def clear(self, head, val):
        # write code here
        headNode = ListNode(0)
        headNode.next = head
        pre = headNode
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return headNode.next