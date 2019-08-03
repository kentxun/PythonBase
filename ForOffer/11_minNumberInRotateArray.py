"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""
# -*- coding:utf-8 -*-
class Solution1:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray)==0:
            return 0
        #cur_min = rotateArray[0]
        for i in range(1,len(rotateArray)):
            if rotateArray[i]<rotateArray[i-1]:
                return rotateArray[i]
        return rotateArray[0]


''' 降低时间复杂度，使用O(logN)的方法'''
class Soulution:
    def minNumberInRotateArray(self,rotateArray):
        length = len(rotateArray)
        if length ==0:
            return length
        i= 0
        j= length-1
        while i<j:
            m = i+(j-i)/2
            if rotateArray[m]<= j:
                j= m
            else:
                i= m
        return rotateArray[i]

    '''
    nums[l] == nums[m] == nums[h]
    特殊情况，如果发生这个情况，只能进行遍历，也就是之前的
    '''

"""完整版 """
class MinValue:
    def getMin(self, arr, n):
        low = 0
        high = n - 1
        if arr[low] < arr[high]:  # 说明有序循环数组是从小到大排序的，第一个元素是最小值，特殊情况单独讨论
            return arr[low]

        # arr[low] >= arr[high]
        while low <= high:  # 和寻找元素最左出现的位置”这部分是一样的
            mid = low + (high - low) / 2
            if arr[low] > arr[mid]:  # 左一半
                high = mid
            elif arr[mid] > arr[high]:  # 右一半
                low = mid + 1
            else:  # arr[low]==arr[mid]==arr[right] 特殊情况 只能挨个遍历，之前两个if最后到了一个元素的也会到达这里进行最终的判断
                cur = arr[low]

                # 在这种情况下，此处的 从左到右遍历
                while low < high:
                    if cur > arr[low + 1]:
                        cur = arr[low + 1]
                    low = low + 1
                return cur