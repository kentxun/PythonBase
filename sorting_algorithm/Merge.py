'''
有两个从小到大排序以后的数组A和B，其中A的末端有足够的缓冲空容纳B。请编写一个方法，将B合并入A并排序。

给定两个有序int数组A和B，A中的缓冲空用0填充，同时给定A和B的真实大小int n和int m，请返回合并后的数组
'''
# -*- coding:utf-8 -*-
class Merge:
    def mergeAB(self, A, B, n, m):
        # write code here
        len_a=len([i for i in A if i !=0])
        len_all= len_a+m
        index_a = len_a-1
        index_b = m-1
        n=1
        while index_b >= 0 and index_a>=0:
            if A[index_a]>B[index_b]:
                A[len_all-n]=A[index_a]
                index_a-=1
                n+=1
            else:
                A[len_all - n] =B[index_b]
                index_b-=1
                n+=1
        # 处理 未处理的B
        if index_b>=0:
            A[:index_b+1]=B[:index_b+1]
        return A
a = Merge()
out = a.mergeAB([1,3,5,0,0,0],[0,2,4],6,3)
print(out)
