'''
dp[i][j]代表的是 : 必须以str1[i]、str2[j]结尾的最长公共子序列，dp[i][j]来源:

可能是dp[i-1][j]，代表str1[0~i-1]与str2[0~j]的最长公共子序列。
可能是dp[i][j-1]，代表str1[0~i]与str2[0~j-1]的最长公共子序列。
如果str1[i] == str2[j]，还可能是dp[i-1][j-1] + 1。
这三种情况中取最大值。
'''


class Solution:
    def getDp(self, str1, str2):
        n1, n2 = len(str1), len(str2)
        dp = []
        dp[0][0] = 1 if str1[0] == str2[0] else 0
        for i in range(1, n1):
            dp[i][0] = max(dp[i - 1][0], 1 if str1[i] == str2[0] else 0)
        for j in range(1, n2):
            dp[0][j] = max(dp[0][j - 1], 1 if str1[0] == str2[j] else 0)

        for i in range(1, n1):
            for j in range(1, n2):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if str1[i] == str2[j]:
                    dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j])
        return dp

    def getStringOut(self, str1, str2, dp):
        if str1 == None or len(str1) == 0 or len(str2) == 0 or str2 == None:
            return ''
        n = len(str1) - 1
        m = len(str2) - 1
        index = dp[n][m] - 1
        res = ['' for _ in range(index)]
        while index >= 0:
            if n > 0 and dp[n][m] == dp[m - 1][m]:
                n -= 1
            elif m > 0 and dp[n][m] == dp[n][m - 1]:
                m -= 1
            else:
                index -= 1
                res[index] = str1[n]
                n -= 1
                m -= 1
        return ''.join(res)








