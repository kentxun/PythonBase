'''
有一个整数val，如何在节点值有序的环形链表中插入一个节点值为val的节点，并且保证这个环形单链表依然有序。

给定链表的信息，及元素的值A及对应的nxt指向的元素编号同时给定val，请构造出这个环形链表，并插入该值。

测试样例：
[1,3,4,5,7],[1,2,3,4,0],2
返回：{1,2,3,4,5,7}
'''

# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class InsertValue:
    def insert(self, A, nxt, val):
        # write code here
        # 先将插入值，转换为 链表节点
        nodeInsert = ListNode(val)
        if len(A)==0:
            return nodeInsert

        # 转换元素和Index为 链表
        # 创建头结点
        head = ListNode(A[0])
        # 创建 向下的指针
        current  = head
        for i in range(len(A)-1):
            current.next = ListNode(A[nxt[i]])
            current= current.next # 指向下一个
        current.next = head
        # 插入值
        # 先处理边界情况，分别是 小于所有的元素和大于所有的元素
        if nodeInsert.val < head.val:
            nodeInsert.next = head
            return nodeInsert

        elif nodeInsert.val > current.val:
            current.next = nodeInsert
            return head
        else:
            pre , now = head, head.next
            while now != head:
                if nodeInsert.val>= pre.val and nodeInsert.val< now.val:
                    pre.next = nodeInsert
                    nodeInsert.next = now
                    return head
                else:
                    now = now.next
                    pre = pre.next