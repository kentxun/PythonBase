'''
对于一个int数组，请编写一个选择排序算法，对数组元素排序。

给定一个int数组A及数组的大小n，请返回排序后的数组。

测试样例：
[1,2,3,5,2,3],6
[1,2,2,3,3,5]
'''
# -*- coding:utf-8 -*-

class SelectionSort:
    def selectionSort(self, A, n):
        res=[]
        for j in range(n):
            last= n-j
            res.append(self.FindMin(A[:last],last))
            A.pop(A.index(self.FindMin(A[:last],last)))
            # 这步用到了python的内置库，不太好
            print(last)
        return res

    def FindMin(self,list_A,m):
        tmp=list_A[0]
        for i in range(m):
            if list_A[i] < tmp:
                tmp=list_A[i]
        return tmp

class SelectionSort1:
    def selectionSort(self, A, n):
        min_index=0
        for i in range(n):
            min_index = i
            for j in range(i+1,n):
                if A[min_index] > A[j]:
                    min_index = j
            if min_index != i:
                A[min_index],A[i]=A[i],A[min_index]
        return A

'''
选择排序，不断缩小候选列表，选取列表中最小的元素，放在前序列表中
'''