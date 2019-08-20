'''
输出所有和为 S 的连续正数序列。

例如和为 100 的连续序列有：

[9, 10, 11, 12, 13, 14, 15, 16]
[18, 19, 20, 21, 22]。
'''
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        small = 1
        big = 2
        middle = (tsum + 1)>>1
        curSum = small + big
        output = []
        while small < middle:
            if curSum == tsum:
                output.append(range(small, big+1))
                big += 1
                curSum += big
            elif curSum > tsum:
                curSum -= small
                small += 1
            else:
                big += 1
                curSum += big
        return output