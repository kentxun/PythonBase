'''
统计一个数字在排序数组中出现的次数。
'''

'''
一般方法，顺序遍历后，统计

优化方法：二分查找，确定index
'''

class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        res = 0
        flag = 0
        for i in data:
            if i == k:
                res +=1
                flag = 1
            else:
                if flag ==1:
                    return res
        return res

