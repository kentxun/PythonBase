'''
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数
'''

# 粗暴方法，每次插入都排序，直接找中位数
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.l = []

    def Insert(self, num):
        # write code here
        self.l.append(num)
        self.l.sort()

    def GetMedian(self, l):
        # write code here
        n = len(self.l)
        if n % 2 == 1:
            return self.l[n // 2]
        else:
            return (self.l[n // 2 - 1] + self.l[n // 2]) / 2.0


'''
思路：构建一棵"平衡二叉搜索树 "。
每个结点左子树均是小于等于其value的值，右子树均大于等于value值。
每个子树均按其 “结点数” 调节平衡。 这样根节点一定是中间值中的一个。
若结点数为奇数，则返回根节点的值；若结点个数为偶数，则再从根结点左子数或右子数中个数较多的子树中选出最大或最小值既可。
'''


'''
#Python版
#该题Python版牛客有问题
#一直提示 def GetMedian(self)函数多给了一个参数 ，然后自己def GetMedian(self,n=None):
#多给它加了一个默认参数，就过了。。。我擦
#思路：两个堆，自己实现，一个最大堆，一个最小堆

'''
class Solution:
    def __init__(self):
        self.minNums = []
        self.maxNums = []

    def maxHeapInsert(self, num):
        self.maxNums.append(num)
        lens = len(self.maxNums)
        i = lens - 1
        while i > 0:
            if self.maxNums[i] > self.maxNums[(i - 1) / 2]:
                t = self.maxNums[(i - 1) / 2]
                self.maxNums[(i - 1) / 2] = self.maxNums[i]
                self.maxNums[i] = t
                i = (i - 1) / 2
            else:
                break

    def maxHeapPop(self):
        t = self.maxNums[0]
        self.maxNums[0] = self.maxNums[-1]
        self.maxNums.pop()
        lens = len(self.maxNums)
        i = 0
        while 2 * i + 1 < lens:
            nexti = 2 * i + 1
            if (nexti + 1 < lens) and self.maxNums[nexti + 1] > self.maxNums[nexti]:
                nexti += 1
            if self.maxNums[nexti] > self.maxNums[i]:
                tmp = self.maxNums[i]
                self.maxNums[i] = self.maxNums[nexti]
                self.maxNums[nexti] = tmp
                i = nexti
            else:
                break
        return t

    def minHeapInsert(self, num):
        self.minNums.append(num)
        lens = len(self.minNums)
        i = lens - 1
        while i > 0:
            if self.minNums[i] < self.minNums[(i - 1) / 2]:
                t = self.minNums[(i - 1) / 2]
                self.minNums[(i - 1) / 2] = self.minNums[i]
                self.minNums[i] = t
                i = (i - 1) / 2
            else:
                break

    def minHeapPop(self):
        t = self.minNums[0]
        self.minNums[0] = self.minNums[-1]
        self.minNums.pop()
        lens = len(self.minNums)
        i = 0
        while 2 * i + 1 < lens:
            nexti = 2 * i + 1
            if (nexti + 1 < lens) and self.minNums[nexti + 1] < self.minNums[nexti]:
                nexti += 1
            if self.minNums[nexti] < self.minNums[i]:
                tmp = self.minNums[i]
                self.minNums[i] = self.minNums[nexti]
                self.minNums[nexti] = tmp
                i = nexti
            else:
                break
        return t

    def Insert(self, num):
        if (len(self.minNums) + len(self.maxNums)) & 1 == 0:
            if len(self.maxNums) > 0 and num < self.maxNums[0]:
                self.maxHeapInsert(num)
                num = self.maxHeapPop()
            self.minHeapInsert(num)
        else:
            if len(self.minNums) > 0 and num > self.minNums[0]:
                self.minHeapInsert(num)
                num = self.minHeapPop()
            self.maxHeapInsert(num)

    def GetMedian(self, n=None):
        allLen = len(self.minNums) + len(self.maxNums)
        if allLen == 0:
            return -1
        if allLen & 1 == 1:
            return self.minNums[0]
        else:
            return (self.maxNums[0] + self.minNums[0] + 0.0) / 2


t = Solution()
t.Insert(5)
t.GetMedian()
t.Insert(2)
t.GetMedian()
