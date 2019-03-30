

'''
你需要爬上一个N层的楼梯，在爬楼梯过程中， 每阶楼梯需花费非负代价，第i阶楼梯花费代价表示为cost[i]，
一旦你付出了代价，你可以在该阶基础上往上爬一阶或两阶。
你可以从第 0 阶或者 第 1 阶开始，请找到到达顶层的最小的代价是多少。
N和cost[i]皆为整数，且N∈[2,1000]，cost[i]∈ [0, 999]。
'''
class Solution:
    def minCostClimbingStairs(self,N,cost):
        dp = [0 for _ in range(N+1)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        if N==2:
            return min(cost[0],cost[1])
        else:
            for t in range(2,N+1):
                dp[t]=min(dp[t-2],dp[t-1])+cost[t]
        return dp[N]