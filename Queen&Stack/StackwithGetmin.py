'''
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。


'''

class Solution:
    def __init__(self):
        self.stack = []
        self.stackmin = []

    def push(self, node):
        if len(self.stack)==0:
            #self.stack.append(node)
            self.stackmin.append(node)
            # 最小栈里，存着当前位置最小值，加入新元素如果不比最小值小，就重复加入最小值
            # 要同步出栈进栈
        elif node < self.stackmin[-1]:
            self.stackmin.append(node)
        else:
            self.stackmin.append(self.stackmin[-1])
        self.stack.append(node)
        # write code here

    def pop(self):
        if len(self.stack)!=0:
            out = self.stack.pop()
            self.stackmin.pop()
            return out
        else:
            return
        # write code here
    def top(self):
        return len(self.stack)
        # write code here
    def min(self):
        # write code here
        return self.stackmin[-1]