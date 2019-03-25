'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

思路：
1. pop_stack 不空 不放入 push_stack 的内容
2. push_stack 要全部放入 pop_stack 才能放入新的
'''
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.pop_stack =[]
        self.push_stack=[]

    def push(self, node):
        # write code here
        self.push_stack.append(node)

    def pop(self):
        # return xx

        if not self.pop_stack:
            while self.push_stack:
                self.pop_stack.append(self.push_stack.pop())
            return self.pop_stack.pop()

        if not self.pop_stack:
            return False
        else:
            return self.pop_stack.pop()