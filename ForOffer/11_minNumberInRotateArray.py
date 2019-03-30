'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。

例如数组 {3, 4, 5, 1, 2} 为 {1, 2, 3, 4, 5} 的一个旋转，该数组的最小值为 1。
'''
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        left =0
        right = len(rotateArray)-1
        while left<right:
            mid = left + (right - left) / 2
            if rotateArray[mid]<=rotateArray[right]:
                right = mid
            else:
                left =mid +1

        return rotateArray[left]

'''
如果数组元素允许重复的话，那么就会出现一个特殊的情况：nums[l] == nums[m] == nums[h]，
那么此时无法确定解在哪个区间，需要切换到顺序查找。
例如对于数组 {1,1,1,0,1}，l、m 和 h 指向的数都为 1，此时无法知道最小数字 0 在哪个区间。
'''
class Solution1:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        left =0
        right = len(rotateArray)-1
        while left<right:
            mid = left + (right - left) / 2
            if  rotateArray[mid]==rotateArray[left]==rotateArray[right]:
                return self.minNumber(rotateArray,left,right)
            elif rotateArray[mid]<=rotateArray[right]:
                right = mid
            else:
                left =mid +1

        return rotateArray[left]

    def minNumber(self,num,left,right):
        for i in range(left,right):
            if num[i]>num[i+1]:
                return num[i+1]
            return num[left]



