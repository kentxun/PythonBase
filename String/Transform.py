'''
对于两个字符串A和B，如果A和B中出现的字符种类相同且每种字符出现的次数相同，
则A和B互为变形词，请设计一个高效算法，检查两给定串是否互为变形词。
给定两个字符串A和B及他们的长度，请返回一个bool值，代表他们是否互为变形词。

测试样例：
"abc",3,"bca",3
返回：true
'''

class Transform:
    def chkTransform(self, A, lena, B, lenb):
        # write code here
        if lena != lenb:
            return False
        if set(A)!=set(B):
            return False
        dictA={}
        dictB={}
        for key in set(A):
            dictA[key]=dictB[key]=0
        for item in A:
            dictA[item]+=1
        for item in B:
            dictB[item]+=1
        if dictA!= dictB:
            return False
        return True


# -*- coding:utf-8 -*-
"别人的思路，不使用python自带的字典和元组，是用ord获取ascii字符串"

class Transform1:
    def chkTransform(self, A, lena, B, lenb):
        if lena != lenb:
            return False
        hashTable = [0 for i in range(0, 256)]
        for x in A:
            hashTable[ord(x)] += 1
        for x in B:
            hashTable[ord(x)] -= 1
        if not max(hashTable):
            return True
        else:
            return False
        # write code here