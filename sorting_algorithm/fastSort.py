import  random
class QuickSort:
    def quickSort(self,A,n):
        if A==[]:
            return []
        x = A[0]
        left = self.quickSort([i for i in A[1:] if i<x],1)
        right = self.quickSort([j for j in A[1:] if j >= x ],1)
        res= left + [x] + right
        return res

a = QuickSort()
out = a.quickSort([1,3,4,5,2,6])