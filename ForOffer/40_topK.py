'''
快速选择
复杂度：O(N) + O(1)  只有当允许修改数组元素时才可以使用
快速排序的 partition() 方法，会返回一个整数 j 使得 a[l..j-1] 小于等于 a[j]，
且 a[j+1..h] 大于等于 a[j]，此时 a[j] 就是数组的第 j 大元素。
可以利用这个特性找出数组的第 K 个元素，这种找第 K 个元素的算法称为快速选择算法。

'''





'''
大小为 K 的最小堆
复杂度：O(NlogK) + O(K)
特别适合处理海量数据
应该使用大顶堆来维护最小堆，而不能直接创建一个小顶堆并设置一个大小，企图让小顶堆中的元素都是最小元素。

维护一个大小为 K 的最小堆过程如下：在添加一个元素之后，如果大顶堆的大小大于 K，那么需要将大顶堆的堆顶元素去除。
'''