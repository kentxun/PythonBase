'''
连续子数组的最大和
{6, -3, -2, 7, -15, 1, 2, 2}，连续子数组的最大和为 8（从第 0 个开始，到第 3 个为止）。
'''
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        max_sum, cur_sum = -0xffffff, 0
        for i in array:
            # 负反馈
            if cur_sum <= 0:
                cur_sum = i
            else:
            # 正反馈
                cur_sum += i
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum

'''
动态规划
F（i） 以array[i]为末尾元素的子数组的和的最大值，子数组的元素的相对位置不变
F（i）= max（F（i-1）+array[i] ， array[i]）
'''