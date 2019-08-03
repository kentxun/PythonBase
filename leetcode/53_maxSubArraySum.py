'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # 以num[i]结尾的最大子串和,一开始方法是对的，状态转移写错了
        dp = nums
        for i in range(1,len(nums)):
            if dp[i-1]+ nums[i] > nums[i]:
                dp[i] = dp[i-1]+nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)







'''
动态规划的是首先对数组进行遍历，当前最大连续子序列和为 sum，结果为 ans
如果 sum > 0，则说明 sum 对结果有增益效果，则 sum 保留并加上当前遍历数字
如果 sum <= 0，则说明 sum 对结果无增益效果，需要舍弃，则 sum 直接更新为当前遍历数字
每次比较 sum 和 ans的大小，将最大值置为ans，遍历结束返回结果
时间复杂度：O(n)O(n)
'''
class Solutionx1:
    def maxSubArray(self, nums: list[int]) -> int:
        # 参考之后： 考察的不是 num对最终的增益了，而是前置子串和对当前num的增益，如果前置对当前有增益
        # 则留用，如果没增益不如以当前num为首，开始新的子串。
        # 思路，动态规划？ 这个方法有问题，不是连续子串,改进一下（如果变小了，就归0）
        maxscore = nums[0]
        sum = 0
        for i in range(len(nums)) :
            if sum > 0:
                sum += nums[i]
            else:
                # 前置的置零
                sum = nums[i]
            maxscore = max(maxscore,sum)
        return maxscore



