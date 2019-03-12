class MergeSort1:
    def merge(self,A,start,mid,end):
        i=start
        j=mid+1
        k=0
        tmp=[]

        while i<=mid & j <= end:
            if A[i]<=A[j]:
                tmp.append(A[i])
                i += 1
            else:
                tmp.append(A[j])
                j += 1
        return tmp

    def merge_sort(self,A,start,end):
        if A==None | start > end:
            return
        mid = (end+start)/2
        self.merge_sort(A,start,mid)
        self.merge_sort(A,mid+1,end)
        self.merge(A,start,mid,end)


class MergeSort:
    def mergeSort(self, A, n):
        # write code here
        if len(A) <= 1:
            return A
        num = int(len(A) / 2)
        left = self.mergeSort(A[:num], num)
        right = self.mergeSort(A[num:], num)

        i, j = 0, 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result

a = MergeSort()
out = a.mergeSort([1,6,3,4,2,5],6)


def merge_sort(lst):
    if len(lst) <= 1:
        return lst          # 从递归中返回长度为1的序列

    middle = len(lst) / 2
    left = merge_sort(lst[:middle])     # 通过不断递归，将原始序列拆分成n个小序列
    right = merge_sort(lst[middle:])
    return merge(left, right)


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):  # 比较传入的两个子序列，对两个子序列进行排序
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])         # 将排好序的子序列合并
    result.extend(right[j:])
    return result