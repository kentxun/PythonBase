'''
对第一个数arr[0]来说，dp[0] = 1，最长递增子序列就是自己。
当计算到dp[i]的时候，最长递增子序列要以arr[i]结尾，所以我们在arr[0....i-1]中所有比arr[i]小的数可以作为最长递增子序列的倒数第二个数，
这些数中，哪个的最长递增子序列更大，就选择哪个。
即dp[i] = max(dp[j] + 1) ，0 <= j < i，arr[j] < arr[i]；

'''

'''
外层循环用来逐个扫描输入，假设当前扫描到的元素是X
内层循环用来找出在X的左边（也就是已经扫描过的），且值比X小的元素E，使X能拼接到以E结尾的LIS的后面
'''
class Solution:
    def lengthOfLIS(self,nums):
        if len(nums) == 0:
            return 0
        dp = [-1 for _ in range(len(nums))]
        res =1
        for i in range(len(nums)):
            dp[i] =1
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i] , dp[j]+1)
                res = max(res,dp[i])
        return res

    def getlist(self,arr,dp):
        length = 0
        index =0
        for i in range(len(dp)):
            if dp[i]> length:
                length = dp[i]
                index = i
        lis = []
        length -=1
        lis[length] = arr[index]
        for i  in  range(index-1,-1,-1):
            if dp[i] == dp[index] -1 and arr[i] < arr[index]:
                length -= 1
                lis[length] = arr[index]
                index = i
        return  lis

a = Solution()
a.lengthOfLIS([1,2,5,8,3,4,6,7])