'''
对于一个int数组，请编写一个冒泡排序算法，对数组元素排序。

给定一个int数组A及数组的大小n，请返回排序后的数组。

测试样例：
[1,2,3,5,2,3],6
[1,2,2,3,3,5]
'''

# -*- coding:utf-8 -*-

class BubbleSort:
    def bubbleSort(self, A, n):
        temp = None
        for i in range(n):
            for j in range(n-1-i):
                if A[j] > A[j+1]:
                    temp = A[j]
                    A[j] = A[j+1]
                    A[j+1]= temp
        return A

a=BubbleSort()
t=a.bubbleSort([1,3,2,4],4)
print(t)