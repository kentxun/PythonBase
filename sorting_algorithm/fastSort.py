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
#out = a.quickSort([1,3,4,5,2,6])


def quick_sort(L):
    return q_sort(L, 0, len(L) - 1)

def q_sort(L, left, right):
    if left < right:
        pivot = Partition(L, left, right)
        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L

'''
取 a[l] 作为切分元素，然后从数组的右端向左扫描找到第一个小于它的元素，交换这两个元素。
再从数组的左端向右扫描直到找到第一个大于等于它的元素。
不断进行这个过程，就可以保证左指针 i 的左侧元素都不大于切分元素，右指针 j 的右侧元素都不小于切分元素。
当两个指针相遇时，将切分元素 a[l] 和 a[j] 交换位置。
'''

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
out = quick_sort(L)
