'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。

思路1.： 可能性增加 fibo[n-1] = fibo[n-2]+fibo[n-3]+...+fibo[0]
                  fibo[n] = fibo[n-1]+fibo[n-2]+...+fibo[0]
        等比数列   fibo[n] = 2 * fibo[n-1]
思路2： 动态规划，干算

'''

class Solution:
    def jumpFloorII(self, number):
        # write code here
        fibo = {i:1 for i in range(number+1)}
        fibo[0], fibo[1],fibo[2] = 0, 1, 2
        for i  in range(3,number+1):
            for j in range(i):
                fibo[i] += fibo[j]
        return fibo[number]

a = Solution()
out = a.jumpFloorII(3)
print(out)