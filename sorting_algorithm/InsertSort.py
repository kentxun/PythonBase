'''
从第二个数开始比较，依次与前序排列好的数进行比较，小于就交换位置
因为前序是排列好的，所以可以直接比较，一定是最后一个数最大，交换完之后，前面的数字一定是更小的

'''

class InsertionSort:
    def insertionSort(self, A, n):
        for i in range(1,n):
            for j in range(i):
                if A[i] < A[j]:
                    A[i],A[j]=A[j],A[i]
        return A

a = InsertionSort()
print(a.insertionSort([1,3,2,5,4],5))