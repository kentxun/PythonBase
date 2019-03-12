'''
假设函数f()等概率随机返回一个在[0,1)范围上的浮点数，那么我们知道，在[0,x)区间上的数出现的概率为x(0<x≤1)。
给定一个大于0的整数k，并且可以使用f()函数，请实现一个函数依然返回在[0,1)范围上的数，
但是在[0,x)区间上的数出现的概率为x的k次方。
'''
# -*- coding:utf-8 -*-
import random


class RandomSeg:
    def f(self):
        return random.random()

    # 请通过调用f()实现
    def random(self, k, x):
        res = 0
        for i in range(k):
            res = max(res, self.f())
        return res