'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

1. 递归思路
2. 递归 + 动态规划
'''
# -*- coding:utf-8 -*-
import time


class Solution:
    def Fibonacci(self, n):
        # write code here
        fibo={}
        fibo[0],fibo[1]=0,1
        for i in range(2,n+1):
            fibo[i] = fibo[i-1]+fibo[i-2]
        return  fibo[n]

a = Solution()
out = a.Fibonacci(39)
print(out)