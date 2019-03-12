'''
对于一个没有重复元素的整数数组，请用其中元素构造一棵MaxTree，
MaxTree定义为一棵二叉树，其中的节点与数组元素一一对应，同时对于MaxTree的每棵子树，
它的根的元素值为子树的最大值。现有一建树方法，对于数组中的每个元素，
其在树中的父亲为数组中它左边比它大的第一个数和右边比它大的第一个数中更小的一个。
若两边都不存在比它大的数，那么它就是树根。请设计O(n)的算法实现这个方法。

给定一个无重复元素的数组A和它的大小n，请返回一个数组，其中每个元素为原数组中对应位置元素在树中的父亲节点的编号，若为根则值为-1。

[3,1,4,2],4
返回：[2,0,-1,2]
'''
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-

class MaxTree:
    # 思想，每个结点的父节点都是它左右两边第一个最大值中较小的那个，所以先找每个值左右两边的最大值，再建立树
    def maxLeft(self, A):
        dictLeft = []  # 记录每个数左边的第一个最大值
        stack = []  # 辅助用栈，第一个值先进栈，若当前值小于栈顶值，则当前值进栈，进栈前的栈顶值为当前值左边第一个最大，否则，栈顶值出栈
        for i in A:
            while len(stack) != 0:
                if i > stack[-1]:
                    stack.pop()
                else:
                    dictLeft.append(stack[-1])
                    stack.append(i)
                    break
            if len(stack) == 0:
                dictLeft.append(-1)  # 用-1代表左侧没有值比它大的情况
                stack.append(i)
        return dictLeft

    def buildMaxTree(self, A, n):
        # write code here
        left = self.maxLeft(A)
        right = self.maxLeft(A[::-1])[::-1]  # 右侧最大值计算方法同左侧
        res = []
        for i in range(n):
            if left[i] != -1:
                if right[i] != -1:
                    res.append(min(left[i], right[i]))
                else:
                    res.append(left[i])
            else:
                if right[i] != -1:
                    res.append(right[i])
                else:
                    res.append(-1)
        for i in range(n):
            if res[i] != -1:
                res[i] = A.index(res[i])  # 返回索引值
        return res