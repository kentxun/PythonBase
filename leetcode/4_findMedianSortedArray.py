'''
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]
则中位数是 (2 + 3)/2 = 2.5
'''


class Solution:
    def findMedianSortedArrays(self, nums1,nums2) -> float:
        # 题解1，归并后，长度定中位数
        res= []
        i,j= 0,0
        while i < len(nums1) and j < len(nums2) :
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        if i< len(nums1):
            res.extend(nums1[i:])
        if j < len(nums2):
            res.extend(nums2[j:])
        # 到目前位置，确实是 O(m+n)的复杂度,奇偶分情况输出
        return  res[int((len(nums1)+len(nums2))/2)] if (len(nums2)+len(nums1)) %2 !=0 \
            else float((res[int((len(nums1)+len(nums2))/2)-1]+res[int((len(nums1)+len(nums2))/2)]))/2

    '''
    如果不合并，节省空间呢？
    合并是为了找中间，现在用合并的方法，找中间数
    '''
class Solution1:
    def findMedianSortedArrays(self, nums1,nums2) -> float:
        # 题解1，归并后，长度定中位数
        i,j= 0,0
        n,m = len(nums1),len(nums2)
        mid_1 = int((n+m)/2)-1  if (n+m)%2 == 0 else int((n+m)/2)
        mid_2 = mid_1+1 if (n+m)%2 == 0 else mid_1
        index =-1
        while i < len(nums1) and j < len(nums2) :
            if nums1[i] < nums2[j]:
                i+=1
                index+=1
                if index == mid_1:
                    start = nums1[i-1]
                if index == mid_2:
                    end = nums1[i-1]
                    return (start+end)/2
            else:
                j+=1
                index+=1
                if index == mid_1:
                    start = nums2[j - 1]
                if index == mid_2:
                    end = nums2[j - 1]
                    return (start + end) / 2
        if i< len(nums1):
            return (nums1[i+(mid_1-index)]+nums1[i+mid_2-index])/2
        if j < len(nums2):
            return (nums2[j+(mid_1-index)]+nums2[j+mid_2-index])/2

a=Solution1()
out = a.findMedianSortedArrays([1,3],[2])
print(out)