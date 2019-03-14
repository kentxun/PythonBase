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


def quick_sort(L):
    return q_sort(L, 0, len(L) - 1)

def q_sort(L, left, right):
    if left < right:
        pivot = Partition(L, left, right)

        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L

def Partition(L, left, right):
    pivotkey = L[left]

    while left < right:
        while left < right and L[right] >= pivotkey:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= pivotkey:
            left += 1
        L[right] = L[left]

    L[left] = pivotkey
    return left

L = [5, 9, 1, 11, 6, 7, 2, 4]

