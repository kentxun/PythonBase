'''
Deque（也称为双端队列）是与队列类似的项的有序集合。 它有两个端部， 首部和尾部， 并且项在集合中保持不变。
Deque不同的地方是添加和删除项是非限制性的。 可以在前面或后面添加新项。 同样， 可以从任一端移除现有项。 在某
种意义上， 这种混合线性结构提供了单个数据结构中的栈和队列的所有能力。 展示了一个Python数据对象的Deque
'''

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items ==[]

    def addFront(self,item):
        self.items.append(item)

    def addRear(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def romveRear(self):
        return  self.items.pop(0)

    def size(self):
        return  len(self.items)