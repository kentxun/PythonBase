'''
请编写一个程序，按升序对栈进行排序（即最大元素位于栈顶），
要求最多只能使用一个额外的栈存放临时数据，但不得将元素复制到别的数据结构中。

给定一个int[] numbers(C++中为vector&ltint>)，其中第一个元素为栈顶，
请返回排序后的栈。请注意这是一个栈，意味着排序过程中你只能访问到第一个元素。

测试样例：
[1,2,3,4,5]
返回：[5,4,3,2,1]

双栈结构
原则1
'''

class TwoStacks:
    def __init__(self):
        self.stack =[]
        self.stackmin=[]

    def twoStacksSort(self, numbers):
        # write code here
        self.stack=numbers
        while len(self.stack)!=0:
            if len(self.stackmin)==0:
                self.stackmin.append(self.stack.pop())
            else:
                if self.stack[-1] < self.stackmin[-1]:
                    self.stackmin.append(self.stack.pop())
                else:
                    tmp = self.stack.pop()
                    while len(self.stackmin) >=0:
                        if len(self.stackmin)==0:
                            self.stackmin.append(tmp)
                            break
                        if self.stackmin[-1]<tmp:
                            self.stack.append(self.stackmin.pop())
                        else:
                            self.stackmin.append(tmp)
                            break

        return self.stackmin

a= TwoStacks()
out = a.twoStacksSort([2,1,4,3,4,6,1,5])
print(out)