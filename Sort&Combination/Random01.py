# -*- coding:utf-8 -*-
import random;

p = random.random()


class RandomP:
    @staticmethod
    def f():
        return 0 if random.random() < p else 1


class Random01:
    def random01(self):
        zero = RandomP.f()
        one = RandomP.f()
        while (zero + one != 1):
            zero = RandomP.f()
            one = RandomP.f()
        # 通过randomP.f()来实现01等概率
        return zero