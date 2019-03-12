'''
如果更快的求一个整数k的n次方。如果两个整数相乘并得到结果的时间复杂度为O(1)，
得到整数k的N次方的过程请实现时间复杂度为O(logN)的方法。
给定k和n，请返回k的n次方，为了防止溢出，请返回结果Mod 1000000007的值。

测试样例：
2,3
返回：8
'''
# -*- coding:utf-8 -*-

class QuickPower:
    def getPower(self, k, N):
        # write code here
        bin_n = list(str(bin(N)))
        tmp = k
        res = 1
        for i in range(len(bin_n)-1,-1,-1):
            if bin_n[i]=='1':
                res = res * tmp
            tmp = (tmp* tmp)%1000000007
            res = res % 1000000007
        return res

a = QuickPower()
out = a.getPower(2,13)
print(out)