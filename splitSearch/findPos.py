'''
有一个有序数组arr，其中不含有重复元素，请找到满足arr[i]==i条件的最左的位置。
如果所有位置上的数都不满足条件，返回-1。
给定有序数组arr及它的大小n，请返回所求值。

测试样例：
[-1,0,2,3],4
返回：2
'''

# -*- coding:utf-8 -*-

class Find:
    def findPos(self, arr, n):
        # write code here
        # 如果 头 小于 尾，则是逆序，
        if arr[0] > n-1 or arr[n-1] < 0:
            return -1
        left = 0
        right = n-1
        res = -1
        while left <= right:
            mid = left + int((right-left)/2)
            # 0-mid从左到右 严格递增1 ，数值最小是1
            if arr[mid] > mid:
                right = mid -1
            elif arr[mid] < mid:
                left = mid + 1
            else:
                res = mid
                right = mid -1
        return res
