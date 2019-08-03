"""
实现一个栈的逆序，但是只能用递归函数和这个栈本身的pop操作来实现，而不能自己申请另外的数据结构。

给定一个整数数组A即为给定的栈，同时给定它的大小n，请返回逆序后的栈。

测试样例：
[4,3,2,1],4
返回：[1,2,3,4]
"""

'''
使用操作系统的栈，来存放当前栈底元素，从而利用递归操作进行逆序
两次递归： 主递归：只要当前栈不为空，就不断获取栈底元素，返回条件1：当前栈空，返回栈。或者执行完将栈底元素装入原栈中，并返回栈
         辅递归：获取当前栈的 栈底元素，只要当前栈不为空，就弹出栈顶元素，获取栈底元素后，向上返回，将该层的元素加入栈
                全部退出后，即将除栈底的元素全部装入原栈中，获取栈底元素
'''
# -*- coding:utf-8 -*-

class StackReverse:
    def reverseStack(self, A, n):
        # write code here
        if n ==0 :
            return A
        i = self.get(A)
        self.reverseStack(A,len(A))
        A.append(i)
        return A

    def get(self,A):
        res = A.pop()
        if len(A) == 0:
            return res
        else:
            last =self.get(A)
            A.append(res)
            return last

ob= StackReverse()
re = ob.reverseStack([1,2,4,5,6,6,4],7)
print(re)