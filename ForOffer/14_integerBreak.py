"""
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
把一根绳子剪成多段，并且使得每段的长度乘积最大。
n = 2
return 1 (2 = 1 + 1)
n = 10
return 36 (10 = 3 + 3 + 4)
"""

"""
贪心算法,解析
https://leetcode-cn.com/problems/integer-break/solution/tan-xin-xuan-ze-xing-zhi-de-jian-dan-zheng-ming-py/
"""

class Solution:
    def interBreak(self,n):
        # write code here
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        res *= n
        return res

    def interBreak2(self,n):
        if n ==2:
            return  1
        if n == 3:
            return 2
        if n == 4:
            return 4
        timeOf3 = n/3
        if (n - 3*timeOf3==1):
            timeOf3 -=1
        timeOf2 = (n-3*timeOf3)/2
        return  (3**timeOf3)*(2**timeOf2)

'''
不考虑推理出2和3的乘积最大的方法，使用动态规划法
每一轮： 长度i 和 长度（n-i）的积 或者 在长度j时的的积与（n-j）的积 （动态规划的思想）
'''
class Solution2:
    def interBreak(self,n):
        dp = [0 for _ in range(n+1)]
        dp[1]= 1
        for i in range(2,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i], max(j * (i - j), dp[j] * (i - j)))
        return  dp[n]

ob = Solution2()
out = ob.interBreak(10)
print(out)