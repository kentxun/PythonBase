'''
输出所有和为 S 的连续正数序列。

例如和为 100 的连续序列有：

[9, 10, 11, 12, 13, 14, 15, 16]
[18, 19, 20, 21, 22]。

双指针思路
//左神的思路，双指针问题
//当总和小于sum，大指针继续+
//否则小指针+
'''

class Solution1:
    def FindContinuousSequence(self, tsum):
        phigh ,plow =2,1
        allres= []
        while phigh > plow:
            cur = (phigh+plow)*(phigh-plow+1)/2
            if cur < tsum:
                phigh+=1
            if cur == tsum:
                res = []
                for i in range(plow,phigh):
                    res.append(i)
                allres.append(res)
                plow+=1
            if cur> tsum:
                plow+=1
        return allres

# -*- coding:utf-8 -*-
class Solution1:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        small = 1
        big = 2
        middle = (tsum + 1)>>1
        curSum = small + big
        output = []
        while small < middle:
            if curSum == tsum:
                output.append(range(small, big+1))
                big += 1
                curSum += big
            elif curSum > tsum:
                curSum -= small
                small += 1
            else:
                big += 1
                curSum += big
        return output


# 粗暴方法，两次遍历，第一次遍历半组数据，因为当大于其中一半的时候，两个数相加就大于和了
# 第二次遍历，就是从第一次遍历的位置，向后递增，用正序列求和公式求和，符合加入结果，大于退出循环
# -*- coding:utf-8 -*-
class Solution2:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        for i in range(1, tsum / 2 + 1):
            for j in range(i, tsum / 2 + 2):
                tmp = (j + i) * (j - i + 1) / 2 # 求和公式
                if tmp > tsum:
                    break
                elif tmp == tsum:
                    res.append(range(i, j + 1))
        return res

'''
其他思路
1）由于我们要找的是和为S的连续正数序列，因此这个序列是个公差为1的等差数列，而这个序列的中间值代表了平均值的大小。假设序列长度为n，那么这个序列的中间值可以通过（S / n）得到，知道序列的中间值和长度，也就不难求出这段序列了。
2）满足条件的n分两种情况：
n为奇数时，序列中间的数正好是序列的平均值，所以条件为：(n & 1) == 1 && sum % n == 0；
n为偶数时，序列中间两个数的平均值是序列的平均值，而这个平均值的小数部分为0.5，所以条件为：(sum % n) * 2 == n.
3）由题可知n >= 2，那么n的最大值是多少呢？我们完全可以将n从2到S全部遍历一次，但是大部分遍历是不必要的。为了让n尽可能大，我们让序列从1开始，
'''