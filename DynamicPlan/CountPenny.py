'''
有数组penny，penny中所有的值都为正数且不重复。每个值代表一种面值的货币，每种面值的货币可以使用任意张，
再给定一个整数aim(小于等于1000)代表要找的钱数，求换钱有多少种方法。
给定数组penny及它的大小(小于等于50)，同时给定一个整数aim，请返回有多少种方法可以凑成aim。


测试样例：
[1,2,4],3,3
返回：2

这里 四部，从 暴力-> 利用hashmap的记忆搜索法 -> 动态规划 改进的（对路径进行了优化） ->  再优化的动态规划
'''
# -*- coding:utf-8 -*-

# 暴力检索法
class Exchange1:
    def countWays(self, penny, n, aim):
        # write code here
        if n==0 or aim ==0:return 0
        return self.foo(penny,0,aim)

    def foo(self,arr,index,aim):
        if aim ==0: return 1
        if index==len(arr):
            return 0
        ret = 0
        i = 0
        while arr[index] * i <= aim:
            ret += self.foo(arr, index+1 , aim-arr[index] * i)
            i+=1
        return ret

# 记忆搜索法
class Exchange2:
    def countWays(self, penny, n, aim):
        # write code here
        if n==0 or aim ==0:return 0
        mp = {}
        return self.foo(penny,0,aim,mp)

    def foo(self,arr,index,aim, mp):
        if aim==0: return 1
        if index==len(arr):return 0
        st = str(index) + ' '+ str(aim)
        if st in mp.keys():
            return mp[st]
        else:
            ret = 0
            i = 0
            while arr[index] * i <= aim:
                ret += self.foo(arr,index+1 ,aim- arr[index]*i,mp)
                i+=1
            mp[st] = ret
            return ret


# 由记忆优化搜索出的 动态规划
class Exchange3:
    def countWays(self, penny, n, aim):
        if n==0 or aim==0: return 0
        dp = [[0 for _ in range(aim + 1)] for _ in range(n)]
        for i in range(n): dp[i][0]=1
        for i in range(1,aim+1):
            if i % penny[0] == 0:
                dp[0][i]=1
            else:
                dp[0][i]=0

        for i in range(1,n):
            for j in range(1,aim+1):
                count =0
                k =0
                while penny[i]*k <= j:
                    count += dp[i-1][j-penny[i]*k]
                    k = k+1
                dp[i][j]= count
        return dp[n-1][aim]

class Exchange4:
    def countWays(self, penny,n,aim):
        if n==0 or aim==0: return 0
        dp =[[0 for _ in range(aim+1)] for _ in range(n)]
        for i in range(n): dp[i][0]=1
        for i in range(1,aim+1):
            if i % penny[0] == 0:
                dp[0][i]=1
            else:
                dp[0][i]=0

        for i in range(1,n):
            for j in range(1,aim+1):
                if j<penny[i]:
                    dp[i][j]= dp[i-1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - penny[i]]

        return dp[n-1][aim]
1

a = Exchange4()
out = a.countWays([1,2,4],3,3)
print(out)