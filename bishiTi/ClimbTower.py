
'''
我们定义f[i]表示到达第i层的时候爬上去的最大值（也就是说，第i层到第i+1层必须爬）

因此我们很容易地找到它的子问题：

1.爬上第i层，（f[i]=f[i-1]+a[i]）

2.飞跃上第i层，（f[i]=min(f[i-2]+a[i],f[i-3]+a[i])）

'''
import sys
if __name__ == '__main__':

    n = int(sys.stdin.readline().strip())
    tower = [0]
    for i in range(n):
        tower.append(int(sys.stdin.readline()))
    df = [0,tower[1]]
    dp = [0,0]

    for i in range(2,n+1):
        dp.append(min(df[i-1],df[i-2]))
        df.append(min(dp[i-1]+tower[i] , df[i-1]+tower[i]))

    print(min(df[n],dp[n]))

