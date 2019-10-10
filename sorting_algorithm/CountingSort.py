# -*- coding:utf-8 -*-
class CountingSort:
    def countingSort(self, A, n):
        # write code here
        count = [0] * (max(A)+1)
        for i in A:
            count[i] += 1
        n = 0
        for k in range( len (count)):
            for j in range(count[k]):
                A[n] = k
                n+=1
        return A

eval()