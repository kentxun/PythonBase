# -*- coding:utf-8 -*-
'''
对于一个字符串，请设计一个算法，将字符串的长度为len的前缀平移到字符串的最后。

给定一个字符串A和它的长度，同时给定len，请返回平移后的字符串。

测试样例：
"ABCDE",5,3
返回："DEABC"

使用局部倒序，再正体倒序
'''
class Translation:
    def stringTranslation(self, A, n, len):
        # write code here
        LA = list(A)
        LA[:len] = self.reverseWord(LA[:len],len)
        LA[len:] = self.reverseWord(LA[len:],n-len)
        LA= self.reverseWord(LA,n)
        return  ''.join(LA)

    def reverseWord(self, A, n):
        for i in range(int(n / 2)):
            A[i], A[n - i - 1] = A[n - i - 1], A[i]
        return A
