'''
有一个X*Y的网格，小团要在此网格上从左上角到右下角，只能走格点且只能向右或向下走。
请设计一个算法，计算小团有多少种走法。给定两个正整数int x,int y，请返回小团的走法数目。

输入包括一行，空格隔开的两个正整数x和y，取值范围[1,10]。


输出描述:
输出一行，表示走法的数目
'''

class Solution:
    def moveInGrid(self):
        x,y=[int(a) for a in input().split()]
        dp = [[0 for _ in range(y+1)] for _ in range(x+1)]
        for t in range(y+1):
            dp[0][t]=1
        for i in range(1,x+1):
            for j in range(y+1):
                if i != 0:
                    if j!=0 :
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    else:
                        dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[x][y]


import sys
try:
    while True:
        x, y = [int(a) for a in input().split()]
        dp = [[0 for _ in range(y + 1)] for _ in range(x + 1)]
        for t in range(y + 1):
            dp[0][t] = 1
        for i in range(1, x + 1):
            for j in range(y + 1):
                if i != 0:
                    if j != 0:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]
        print(dp[x][y])
except:
    pass