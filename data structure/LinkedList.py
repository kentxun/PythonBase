# !/usr/bin/env python
# -*- coding:utf-8 -*-


# __all__ = ['单链表节点',
#            '单链表',
#            '循环单链表',
#            '双链表节点',
#            '双链表']


# 单链表节点
class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


# 单链表
class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        p = self._head
        n = 0
        while p is not None:
            n += 1
            p = p.next
        return n

    # 表头插入
    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    # 表头弹出
    def pop(self):
        if self._head is None:
            raise Exception('There is no nodes.')
        e = self._head.elem
        self._head = self._head.next
        return e

    # 表尾插入
    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    # 表尾弹出
    def pop_last(self):
        if self._head is None:
            raise Exception('empty list!')
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    # 查找
    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    # 遍历
    def for_each(self, proc):
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next

    # 迭代器
    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    # 筛选生成器
    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next

    # 反转
    def reverse(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p

    # 排序
    def sort(self):
        p = self._head
        if p is None or p.next is None:
            return
        rem = p.next
        p.next = None
        while rem is not None:
            p = self._head
            q = None
            while p is not None and p.elem <= rem.elem:
                q = p
                p = p.next
            if q is None:
                self._head = rem
            else:
                q.next = rem
            q = rem
            rem = rem.next
            q.next = p

    # 打印
    def printall(self):
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next
        print('')


# 循环单链表
class LCList:
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    # 前端插入
    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    # 尾端插入
    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    # 前端弹出
    def pop(self):
        if self._rear is None:
            raise Exception('Empty!')
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next
        return p.elem

    # 输出表元素
    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next


# 双链表节点
class DLNode:
    def __init__(self, elem, prev=None, next_=None):
        self.elem = elem
        self.next = next_
        self.prev = prev


# 双链表
class DLList(LList):
    def __init__(self):
        super(DLList, self).__init__()
        self._rear = None

    def prepend(self, elem):
        p = DLNode(elem, None, self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._head = p

    def append(self, elem):
        p = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise Exception('Empty!')
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise Exception('Empty!')
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e
