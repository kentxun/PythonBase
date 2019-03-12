'''
对于一个给定的字符串数组，请找到一种拼接顺序，
使所有小字符串拼接成的大字符串是所有可能的拼接中字典序最小的。
给定一个字符串数组strs，同时给定它的大小，请返回拼接成的串。

测试样例：
["abc","de"],2
"abcde"
'''

# -*- coding:utf-8 -*-

class Prior:
    def findSmallest(self, strs, n):
        # write code here
        for i in range(n-1):
            for j in range(i,n):
                if strs[i]+strs[j]<=strs[j]+strs[i]:
                    strs[i] = strs[i]
                    strs[j] = strs[j]
                else:
                    strs[i],strs[j] = strs[j],strs[i]
        strs = ''.join(strs)
        return strs


# -*- coding:utf-8 -*-

class Prior1:
    def findSmallest(self, strs, n):
        strs.sort(cmp=lambda x, y: cmp(x + y, y + x))
        return ''.join(strs)


class Prior2:
    def findSmallest(self, strs, n):
        from functools import cmp_to_key
        def func(x, y):
            if x + y < y + x:
                return -1
            elif x + y == y + x:
                return 0
            else:
                return 1
        strs.sort(key=cmp_to_key(func))
        return ''.join(strs)