'''
在一个 m*n 的棋盘的每一个格都放有一个礼物，每个礼物都有一定价值（大于 0）。从左上角开始拿礼物，每次向右或向下移动一格，直到右下角结束。给定一个棋盘，求拿到礼物的最大价值。例如，对于如下棋盘

1    10   3    8
12   2    9    6
5    7    4    11
3    7    16   5
礼物的最大价值为 1+12+5+7+7+16+5=53。
'''
'''
标准动态规划题
状态方程：
dp[i][j] = max(dp[i-1][j],dp[i][j-1])+ values[i][j]
当前最大价值，来自左边或者上边的最大值 + 当前值
'''

class Solution:
    def getMost(self,values):
        if values is None or len(values)==0 or len(values[0])==0:
            return 0
        n = len(values[0])
        m = len(values)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = values[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + values[0][i]
        for j in range(1,m):
            dp[j][0] = dp[j-1][0]+ values[j][0]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])+ values[i][j]
        return dp[ n - 1][ m - 1 ]

a= Solution()
out = a.getMost([[426,306,641,372,477,409],[223,172,327,586,363,553],[292,645,248,316,711,295],[127,192,495,208,547,175],[131,448,178,264,207,676],[655,407,309,358,246,714]])
print(out)