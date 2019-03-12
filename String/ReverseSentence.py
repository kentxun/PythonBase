# -*- coding:utf-8 -*-

'''
对于一个字符串，请设计一个算法，只在字符串的单词间做逆序调整，
也就是说，字符串由一些由空格分隔的部分组成，你需要将这些部分逆序。
给定一个原字符串A和他的长度，请返回逆序后的字符串。

测试样例：
"dog loves pig",13
返回："pig loves dog"

'''

class Reverse:
    def reverseSentence(self, A, n):
        # write code here
        LA = list(A)
        LA = self.reverseWord(LA,n)
        index = 0
        for j in range(n):
            if LA[j]==' ':
                LA[index:j]=self.reverseWord(LA[index:j],j-index)
                index=j+1
        LA[index:] = self.reverseWord(LA[index:], n - index)
        return ''.join(LA)

    def reverseWord(self,A,n):
        for i in range(int(n/2)):
            A[i],A[n-i-1]=A[n-i-1], A[i]
        return A

a= Reverse()
out = a.reverseSentence("TUM MKIALI KVJUBEN VBSEWFT JAD AIZWEL CP LG PTB",47)
print(out)