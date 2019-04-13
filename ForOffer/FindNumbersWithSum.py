'''
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
'''

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        res = []
        for i in range(len(array)):
            if (tsum-array[i]) in array:
                res.append([array[i],tsum-array[i]])

        if res:
            out = sorted(res,key=lambda x:x[0]*x[1])
            return  out[0]
        else:
            return []
a =Solution()
print(a.FindNumbersWithSum([1,2,4,7,11,16],10))