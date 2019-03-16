# !/usr/bin/env python
# -*- coding:utf-8 -*-


# __all__ = ['栈(顺序表)',
#            '栈(链接表)',
#            '队列']


# 栈(顺序表)
class SStack:
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise Exception('Empty!')
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise Exception('Empty!')
        return self._elems.pop()


class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


# 栈(链接表)
class LStack:
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise Exception('Empty!')
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise Exception('Empty!')
        p = self._top
        self._top = p.next
        return p.elem


# 队列
class SQueue:
    def __init__(self, init_len=8):
        self._len = init_len
        self._elems = [0] * init_len
        self._head = 0
        self._num = 0

    def is_empty(self):
        return self._num == 0

    def peek(self):
        if self._num == 0:
            raise Exception('Empty!')
        return self._elems[self._head]

    def dequeue(self):
        if self._num == 0:
            raise Exception('Empty!')
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e

    def enqueue(self, e):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = e
        self._num += 1

    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0
