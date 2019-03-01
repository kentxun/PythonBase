'''
是优化 的 堆排序，在堆排序的基础上修改

'''
# -*- coding:utf-8 -*-

class ScaleSort:
    def sortElement(self, A, n, k):
        # write code here
        heap=self.buildHeap(A[n-k-1:n],k)
        for i in range(n-1,k,-1):
            tmp = A[i]
            A[i]=heap[0]
            heap[0]=tmp
            heap.pop(k)
            heap.insert(0,A[i-k-1])
            A[i-k-1:i]=heap
            self.adjustHeap(heap,0,k+1)
        return A

    def buildHeap(self,A,n):
        for i in range(int(n/2)+1,-1,-1):
            self.adjustHeap(A,i,n)
        return A

    def adjustHeap(self,A,i,n):
        left = 2*i +1
        right = 2*i +2
        max_index = i
        if left < n and A[left] > A[max_index]:
            max_index = left
        if right < n and A[right] > A[max_index]:
            max_index = right
        if max_index != i:
            A[max_index],A[i]=A[i],A[max_index]
            self.adjustHeap(A,max_index,n)

a= ScaleSort()
out = a.sortElement([2,1,4,3,6,5,8,7,10,9],10,2)
print(out)