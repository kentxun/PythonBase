'''
给定一个长度为N且没有重复元素的数组arr和一个整数M，实现函数等概率随机打印arr中的M个数。
'''

import random
class RandomPrint:
    def rprint(self, arr, N, M):
        # write code here
        return random.sample(arr,M)