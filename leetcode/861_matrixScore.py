
'''
有一个二维矩阵 A 其中每个元素的值为 0 或 1 。
移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。
在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。
返回尽可能高的分数。

示例：

输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
输出：39
解释：
转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

'''

class Solution:
    def matrixScore(self, A):
        score = 0
        def func1(a):
            return 0 if a else 1
        def str_bin(L):
            return int(''.join(map(str,L)),2)
        for t in range(len(A)):
            if A[t][0]==0:
                A[t] = list(map(func1,A[t]))
                print(A)
        for i in range(1,len(A[0])):
            tmp = 0
            for t in range(len(A)):
                if A[t][i] == 0:
                    tmp -=1
                else:
                    tmp +=1
            if tmp <0:
                for t in range(len(A)):
                    A[t][i] = func1(A[t][i])
        for ele in A:
            score += str_bin(ele)

        return score

# TODO 目前写的是只改变行，下一步考虑列的问题，复杂很多！
# 思路总结： 1。 这里的贪心在于，按照列处理时，最优为 当前列的1 大于 0，一旦作出选择，后续就不再回头
#          2。 这里有个关键点是 把行处理拆出来，一旦明确头元素为1 最大后，不再改变，这也是贪心处理
#          3。 核心还是 将行和列两个行为拆分到同一个 贪心准则上！ 要观察题目
a= Solution()
out = a.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]])
print(out)