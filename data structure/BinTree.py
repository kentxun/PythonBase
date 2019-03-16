# !/usr/bin/env python
# -*- coding:utf-8 -*-


# __all__ = ['优先队列(列表)',
#            '优先队列(堆)',
#            '二叉树节点',
#            '统计树中节点个数',
#            '求二叉树的数据和',
#            '先根序遍历(DFS)(递归)',
#            '先根序遍历(DFS)(非递归)',
#            '后根序遍历(非递归)',
#            'BFS遍历所有节点',
#            '二叉树']


# 优先队列(列表)
class PrioQue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)

    def enqueue(self, e):
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i + 1, e)

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise Exception('Empty!')
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise Exception('Empty!')
        return self._elems.pop()


# 优先队列(堆)
class PrioQueue:
    def __init__(self, elist=[]):
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise Exception('Empty!')
        return self._elems[0]

    def enqueue(self, e):
        self._elems.append(None)
        self.siftup(e, len(self._elems) - 1)

    def siftup(self, e, last):
        elems, i, j = self._elems, last, (last - 1) // 2
        while i > 0 and e < elems[j]:
            elems[i] = elems[j]
            i, j = j, (j - 1) // 2
        elems[i] = e

    def dequeue(self):
        if self.is_empty():
            raise Exception('Empty!')
        elems = self._elems
        e0 = elems[0]
        e = elems.pop()
        if len(elems) > 0:
            self.siftdown(e, 0, len(self._elems))
        return e0

    def siftdown(self, e, begin, end):
        elems, i, j = self._elems, begin, begin * 2 + 1
        while i < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            if e < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2 * j + 1
        elems[i] = e

    def buildheap(self):
        end = len(self._elems)
        for i in range(end // 2, -1, -1):
            self.siftdown(self._elems[i], i, end)


# 二叉树节点
class BinTNode:
    def __init__(self, dat, left=None, right=None):
        self.data = dat
        self.left = left
        self.right = right


# 统计树中节点个数
def count_BinTNodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)


# 求二叉树的数据和
def sum_BinTNodes(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BinTNodes(t.left) + sum_BinTNodes(t.right)


# 先根序遍历(DFS)(递归)
def preorder(t, proc):
    if t is None:
        return
    proc(t.data)
    preorder(t.left, proc)
    preorder(t.right, proc)


# 先根序遍历(DFS)(非递归)
from 数据结构与算法.Stack_and_Queue import SStack
def preorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            proc(t.data)
            s.push(t.right)
            t = t.left
        t = s.pop()


# 后根序遍历(非递归)
def postorder_nonrec(t, proc):
    s = SStack()
    while t is not None or not s.is_empty():
        while t is not None:
            s.push(t)
            t = t.left if t.left is not None else t.right

        t = s.pop()
        proc(t.data)
        # pop是取栈最上面一个数但不弹出
        if not s.is_empty() and s.top().left == t:
            t = t.top().right
        else:
            t = None


# BFS遍历所有节点
from 数据结构与算法.Stack_and_Queue import SQueue
def levelorder(t, proc):
    qu = SQueue()
    qu.enqueue(t)
    while not qu.is_empty():
        n = qu.dequeue()
        if n is None:
            continue
        qu.enqueue(n.left)
        qu.enqueue(n.right)
        proc(n.data)


# 二叉树
class BinTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def root(self):
        return self._root

    def leftchild(self):
        return self._root.left

    def rightchild(self):
        return self._root.right

    def set_root(self, rootnode):
        self._root = rootnode

    def set_left(self, leftchild):
        self._root.left = leftchild

    def set_right(self, rightchild):
        self._root.right = rightchild
