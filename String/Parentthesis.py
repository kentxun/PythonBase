'''
对于一个字符串，请设计一个算法，判断其是否为一个合法的括号串。

给定一个字符串A和它的长度n，请返回一个bool值代表它是否为一个合法的括号串。

测试样例：
"(()())",6
返回：true
'''
# -*- coding:utf-8 -*-

class Parenthesis:
    def chkParenthesis(self, A, n):
        # write code here
        num = 0
        for i in range(n):
            if A[i]=='(':
                num+=1
            if A[i]==')':
                num-=1
            if num <0:
                return False
        if num ==0:
            return True
        else:
            return False
