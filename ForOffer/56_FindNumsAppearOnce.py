'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次，找出这两个数。
'''

'''
两个不相等的元素在位级表示上必定会有一位存在不同，将数组的所有元素异或得到的结果为不存在重复的两个元素异或的结果。

diff &= -diff 得到出 diff 最右侧不为 0 的位，也就是不存在重复的两个元素在位级表示上最右侧不同的那一位，利用这一位就可以将两个元素区分开来。


此题考察的是异或运算的特点：即两个相同的数异或结果为0。
此题用了两次异或运算特点：
（1）第一次使用异或运算，得到了两个只出现一次的数相异或的结果。
（2）因为两个只出现一次的数肯定不同，即他们的异或结果一定不为0，一定有一个位上有1。另外一个此位上没有1，
我们可以根据此位上是否有1，将整个数组重新划分成两部分，一部分此位上一定有1，另一部分此位上一定没有1，
然后分别对每部分求异或，因为划分后的两部分有这样的特点：其他数都出现两次，只有一个数只出现一次。
因此，我们又可以运用异或运算，分别得到两部分只出现一次的数。
'''
# -*- coding:utf-8 -*-

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        tmp = []
        for i in array:
            if i not in tmp:
                tmp.append(i)
            else:
                tmp.remove(i)
        return tmp

a = Solution()
print(a.FindNumsAppearOnce([2,4,3,6,3,2,5,5]))


# 异或法
class Solution2:
    def FindNumsAppearOnce(self, array):
        if not array:
            return []
        # 对array中的数字进行异或运算
        tmp = 0
        for i in array:
            tmp ^= i
        # 获取tmp中最低位1的位置
        idx = 0
        while (tmp & 1) == 0:
            tmp >>= 1
            idx += 1
        a = b = 0
        for i in array:
            if self.isBit(i, idx):
                a ^= i
            else:
                b ^= i
        return [a, b]

    def isBit(self, num, idx):
        """
        判断num的二进制从低到高idx位是不是1
        :param num: 数字
        :param idx: 二进制从低到高位置
        :return: num的idx位是否为1
        """
        num = num >> idx
        return num & 1