'''
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:
输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
'''


'''
python简便方法：
1。 排序后输出 位置为 N/2的数
2。 collections存在 找众数的方法
'''
'''
一般思路：
1。 hashmap统计，边统计边比较
2。 摩尔投票法,先假设第一个数过半数并设cnt=1；遍历后面的数如果相同则cnt+1，不同则减一，当cnt为0时则更换新的数字为候选数（成立前提：有出现次数大于n/2的数存在）
3。//位运算法,统计每个数字每一位0，1出现的次数，如果某一位1出现的次数多则该位为1，0同理；
//最后按为统计出来的数就是众数
'''

class Solution:
    def majorityElement(self, nums):
        cnt = 0
        res = 0
        for i in  range(len(nums)):
            if cnt ==0:
               res =  nums[i]
               cnt = 1
            else:
               cnt = cnt+1 if res == nums[i] else cnt -1
        return  res