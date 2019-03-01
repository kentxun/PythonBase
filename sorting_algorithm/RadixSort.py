# -*- coding:utf-8 -*-

class RadixSort:
    def radixSort(self, A, n):
        # write code here

        for i in range(4):
            Radix = [[], [], [], [], [], [], [], [], [], []]
            for j in A:
                Radix[self.getNum(j,i)].append(j)
            index = 0
            for l  in Radix:
                for k in l:
                    A[index] = k
                    index +=1
        return A

    def getNum(self,m,k):
        if k == 3 :
            return int(m/1000)
        if k == 2 :
            return int(m%1000/100)
        if k == 1 :
            return int(m%1000%100/10)
        if k == 0 :
            return int(m%10)


class RadixSort1:
    def radixSort(self, A, n):
        for i in range(4):
            # 生成是个空列表，使用迭代
            s = [[] for _ in range(10)]
            for j in A:
                # 获取 相应位数（比如十位）的数
                s[j / (10 ** i) % 10].append(j)

            # 继续迭代，依次读入 两层列表的数
            A = [a for b in s for a in b]
        return A
