'''
编写一个类,只能用两个栈结构实现队列,支持队列的基本操作(push，pop)。

给定一个操作序列ope及它的长度n，其中元素为正数代表push操作，
为0代表pop操作，保证操作序列合法且一定含pop操作，请返回pop的结果序列。

测试样例：
[1,2,3,0,4,0],6
返回：[1,2]

两条原则
1、 POP 栈不空不往里面Push
2、 push栈不完全倒入POP栈不新push，也就是 每次倒入都要完全倒入
'''

class TwoStack:
    def __init__(self):
        self.stackPush=[]
        self.stackPop=[]

    def push(self,item):
        # if len(self.stackPush)==0:
        #     self.stackPush.append(item)
        #  else:
        #     for i in range(len(self.stackPush)):
        #         self.stackPop.append(self.stackPush[i])
        #     self.stackPush.append(item)
        self.stackPush.append(item)

    def pop(self):
        if len(self.stackPop)==0 :
            for i in range(len(self.stackPush)):
                self.stackPop.append(self.stackPush.pop())
            return self.stackPop.pop()
        else:
            return  self.stackPop.pop()


    def twoStack(self, ope, n):
        # write code here
        res = []
        for i in range(n):
            if ope[i]==0:
                res.append(self.pop())
            else:
                self.push(ope[i])
        return res

a= TwoStack()
out =a.twoStack([287,202,181,156,0],5)
print(out)