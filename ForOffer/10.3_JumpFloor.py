'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

思路：
动态规划：  1级=1 2级=2 3级= 2+1 or 1+2  4级=3+1 or 2+2  ——>  fibo[n-1]+fibo[n-2]
'''

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        fibo = {}
        fibo[0], fibo[1],fibo[2] = 0, 1, 2
        for i in range(3, number + 1):
            fibo[i] = fibo[i - 1] + fibo[i - 2]
        return fibo[number]