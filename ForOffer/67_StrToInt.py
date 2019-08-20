# -*- coding:utf-8 -*-
'''
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
'''
class Solution:
    def StrToInt(self, s):
        # write code here
        # 先排除异常特殊情况
        if s in ['','-','+','+-','-+']:
            return 0
        count = 0
        # 只要有非法字符就不过
        for i in s:
            # 检查字母
            if i not in '0123456789+-':
                count += 1
        # 只要-+号不在第一位就不过
        for i in s[1:]:
            if i not in '0123456789':
                count += 1
        if count:
            return 0
        return int(s)