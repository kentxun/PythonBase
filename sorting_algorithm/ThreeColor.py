# -*- coding:utf-8 -*-

class ThreeColor:
    def sortThreeColor(self, A, n):
        index_pre = 0
        index_post = n-1
        index = 0
        while index <=index_post:
            if A[index]==2:
                A[index_post],A[index]=A[index],A[index_post]
                index_post-=1
            elif A[index]==0:
                A[index_pre],A[index]=A[index],A[index_pre]
                index_pre += 1
                index+=1
            elif A[index]==1:
                index+=1
        return A

a = ThreeColor()
out = a.sortThreeColor([1,2,0,2],4)
print(out)