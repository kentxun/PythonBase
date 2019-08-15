'''
对于一个字符串,请设计一个高效算法，找到字符串的最长无重复字符的子串长度。

给定一个字符串A及它的长度n，请返回它的最长无重复字符子串长度。保证A中字符全部为小写英文字符，且长度小于等于500。

测试样例：
"aabcb",5
返回：3

hashmap : 记录 上一次更新时，已有字符的出现位置
pre : 记录 第i-1个 字符前，最长无重复子串的前序 位置

一般性描述，查找 第i个字符，向前的最长
如果不存在 该字符，插入，计算到 前一个有重复字符的字符的长度
如果存在了，查找前一个该字符出现的位置

如果该 位置 在 pre 之后，则长度就是 当前字符与该字符之前出现位置的 长度，需要更新pre的位置
如果在 pre之前， 则为 当前字符 到pre的位置 的 长度，不需要更新Pre的位置

'''
# -*- coding:utf-8 -*-

class DistinctSubstring:
    def longestSubstring(self, A, n):
        # write code here
        dictA={}
        pre = -1
        length =0
        maxlength =0
        for i in range(n):
            if A[i] in dictA.keys():
                if dictA[A[i]] > pre:
                    length = i - dictA[A[i]]
                    pre = dictA[A[i]]
                else:
                    length = i-pre
                    pre = dictA[A[i]]
                maxlength = max(length, maxlength)
                dictA[A[i]] = i
            else:
                dictA[A[i]] = i
                length= i-pre
                maxlength=max(length,maxlength)

        return maxlength
a = DistinctSubstring()
out = a.longestSubstring('aabadabda',9)