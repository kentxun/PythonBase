'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

思路：
动态规划： 拆分成 2*2 和2*1 叠加上去,每多一个就是多一个 2*1 
'''
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 2:
            return number
        pre1 ,pre2 = 1,2
        res = 0
        for i in range(3, number+1):
            res = pre1 + pre2
            pre1 = pre2
            pre2 = res
        return res




