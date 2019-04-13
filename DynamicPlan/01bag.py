'''
一个背包有一定的承重cap，有N件物品，每件都有自己的价值，记录在数组v中，
也都有自己的重量，记录在数组w中，每件物品只能选择要装入背包还是不装入背包，
要求在不超过背包承重的前提下，选出物品的总价值最大。

给定物品的重量w价值v及物品数n和承重cap。请返回最大总价值。

[1,2,3],[1,2,3],3,6
返回：6
'''
class Backpack_Opt:
    def maxValue(self, w, v, n, cap):
        # write code here
        dp = [-1 for _ in range(cap+1) ]
        dp[0] = 0
        # 遍历每个物品
        for i in range(n):
            # 遍历每种可能的重量
            for j in range(cap,w[i]-1,-1):
                # 如果没买过
                if dp[j-w[i]]!=-1:
                    dp[j]=max(dp[j-w[i]]+v[i],dp[j])

        return max(dp)

class Backpack:
    '''
    dp[i][j]前i件物品（i不一定装进去）总重不超过j的最大价值
    两种情况：dp[i][j]=dp[i-1][j]，即第i件物品不放入
    dp[i][j]=dp[i-1][j-w[i]]+v[i]，即第i件物品放入,取两者较大值即可
    '''
    def maxValue(self,w, v, n, cap):
        # 行：物品数  列： 所剩重量
        dp = [[-1 for _ in range(cap+1)] for _ in range(n+1)]
        # 包重量 0 ，情况下可买价值
        for n in range(n+1): dp[n][0] =0
        # 不购买，包重量增加
        for m in range(cap+1): dp[0][m] = 0
        # 遍历所有物品
        for i in range(1,n+1):
            # 遍历包重量
            for j in range(1, cap+1):
                # 包重量小于当前物品重量，无法购买，当前dp存储上一个物品此重量下的价值
                if j < w[i-1] :
                    dp[i][j] = dp[i-1][j]
                else:
                    # 如果可购买，则计算购买当前物品（由去除当前物品重量时的质量+当前）与 不购买的比较
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i-1]]+v[i-1])
        return dp[n][cap]

a = Backpack()
a.maxValue([1,2,3],[1,2,3],3,6)