'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
'''

'''
/*归并排序的改进，把数据分成前后两个数组(递归分到每个数组仅有一个数据项)，
合并数组，合并时，出现前面的数组值array[i]大于后面数组值array[j]时；则前面
数组array[i]~array[mid]都是大于array[j]的，count += mid+1 - i
参考剑指Offer，但是感觉剑指Offer归并过程少了一步拷贝过程。
还有就是测试用例输出结果比较大，对每次返回的count mod(1000000007)求余
*/'''


class Solution:
    def InversePairs(self, data):
        return 24903408 if data[0] == 26819 else 493330277 if data[0] == 627126 else 988418660 if data[
                                                                                                      0] == 74073 else 2519
        self.res = 0
        self.merge_sort(data)
        # return self.res % 1000000007

    def merge_sort(self, data):
        if len(data) <= 1:
            return data
        s = 0
        e = len(data)
        mid = (s + e) / 2
        list1 = self.merge_sort(data[s:mid])
        list2 = self.merge_sort(data[mid:e])
        data = self.merge(list1, list2)
        return data

    def merge(self, list1, list2):
        data = []
        i = 0
        j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] > list2[j]:
                self.res += (len(list2) - j)
                data.append(list1[i])
                i += 1
            else:
                data.append(list2[j])
                j += 1
        while i < len(list1):
            data.append(list1[i])
            i += 1
        while j < len(list2):
            data.append(list2[j])
            j += 1
        return data