'''
堆排序
1. 建立最大堆过程： 从下向上，选取父节点，与子节点进行比较，
如果出现 父<子，就交换位置，同时将子节点作为父节点向下递归查询
ps: 二叉树特性，子 left_index = f_index *2 right_index=f_index*2+1

2. 堆排序，就是不断将 index=0 的位置，与最后交换，在末端形成有序序列
再将交换后的 堆 进行最大堆调整
'''


class HeapSort:
    def heapSort(self, A, n):
        # write code here
        self.buildHeap(A,n)

        for i in range(n - 1, -1, -1):
            A[0], A[i] = A[i], A[0]
            self.heap_adjust(A, 0, i)
        return A

    def buildHeap(self,A,n):
        for i in range(int(n/2)+1,-1,-1):
            self.heap_adjust(A,i,n)

    def heap_adjust(self,A,i,n):
        left = 2*i +1
        right = 2*i +2
        max_index = i
        if (left < n and A[max_index]<A[left]):
            max_index = left
        if (right < n and A[max_index]<A[right]):
            max_index = right
        if (max_index!= i ):
            A[max_index],A[i]= A[i],A[max_index]
            self.heap_adjust(A,max_index,n)

a = HeapSort()
out = a.heapSort([1,2,3,5,2,3],6)