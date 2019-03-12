'''
假设有n对左右括号，请求出合法的排列有多少个？
合法是指每一个括号都可以找到与之配对的括号，比如n=1时，()是合法的，但是)(为不合法。
给定一个整数n，请返回所求的合法排列数。保证结果在int范围内。

1
返回：1
'''

# -*- coding:utf-8 -*-
# 1/n+1 可能导致 为0
class Parenthesis:
    def countLegalWays(self, n):
        # write code here
        X = self.factor(n)
        Y = self.factor(2*n)
        return int(Y/X/X/(n+1))

    def factor(self,n):
        if  0<=n<2:
            return 1
        else:
            return n * self.factor(n-1)

a = Parenthesis()
out = a.countLegalWays(1)
