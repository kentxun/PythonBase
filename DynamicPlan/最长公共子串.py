'''
dp矩阵第一列即dp[0~N-1][0]，对某一个位置(i,0)来说，如果str1[i] == str2[0]，令dp[i][0] = 1，否则令dp[i][0] = 0；
矩阵dp第一行，即dp[0][0~M-1]，对某个位置(0,j)来说，如果str1[0] == str2[j]，令dp[0][j] = 1，否则令dp[0][j] = 0；
一般的位置有两种情况，如果str1[i] != str2[j]，说明在必须把str1[i]和str2[j]当做公共子串最后一个字符是不可能的，
所以dp[i][j] = 0； 如果str1[i] = str2[j]，说明可以将str1[i]和str2[j]作为公共子串的最后一个字符，其长度就是dp[i-1][j-1] + 1；
'''

class Solution:
    def getdp(self,s1,s2):
        n1 ,n2 = len(s1),len(s2)
        dp =[]
        for i in range(n1):
            dp[i][0] = 1 if s1[i] ==s2[0] else 0
        for j in range(n2):
            dp[0][j] = 1 if s1[0] == s2[j] else 1
        res = 0
        for i in range(1,n1):
            for j in range(1,n2):
                if s1[i]==s2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    res = max(res , dp[i][j])
        return  res

    def getStringOut(self,s1,s2,dp):
        if s1 == None or len(s1) == 0 or len(s2) == 0 or s2 == None:
            return ''
        max = 0
        end = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if dp[i][j] > max :
                    max = dp[i][j]
                    end = i
        return s1[end-max+1 : end+1]

    