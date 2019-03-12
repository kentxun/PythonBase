'''
对于一个有序循环数组arr，返回arr中的最小值。
有序循环数组是指，有序数组左边任意长度的部分放到右边去，右边的部分拿到左边来。
比如数组[1,2,3,3,4]，是有序循环数组，[4,1,2,3,3]也是。
给定数组arr及它的大小n，请返回最小值。

[4,1,2,3,3],5
返回：1
'''
# -*- coding:utf-8 -*-

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