'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

# dfs加剪支

class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return []
        res= []
        def dfs(start , tmp, index):
            if start >(n-1)*2:
                if index==0 :
                   res.append(tmp)
                   return
                else:
                   return
            if index <= 0:
                dfs(start+1, tmp+'(',index+1)
            else:
                dfs(start+1, tmp+'(',index+1)
                dfs(start+1, tmp+')',index-1)
        dfs(0,'(',1)
        return res
a = Solution()
out = a.generateParenthesis(2)
print(out)