'''
题目描述：计算让一组区间不重叠所需要移除的区间个数。
先计算最多能组成的不重叠区间个数，然后用区间总个数减去不重叠区间的个数。
在每次选择中，区间的结尾最为重要，选择的区间结尾越小，留给后面的区间的空间越大，那么后面能够选择的区间个数也就越大。

Input: [ [1,2], [1,2], [1,2] ]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Input: [ [1,2], [2,3] ]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
'''

class Solution:
    def eraseOverlapingIntervals(self,intervals):
        if len(intervals) == 0: return 0
        # 按照区间 尾数排序，小的考前，尽可能给后面留下更多的
        b= sorted(intervals,key=lambda x:x[-1])
        # 遍历去除不重复的区间
        cnt = 1
        end = b[0][-1]
        for i in  b[1:]:
            if i[0] < end:
                continue
            else:
                end = i[-1]
                cnt += 1
        return len(intervals)-cnt

a = Solution()
out = a.eraseOverlapingIntervals( [ [1,2], [1,2], [1,2] ])
print(out)
