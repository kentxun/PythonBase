# -*- coding:utf-8 -*-
'''[1,2,3,5,2,3],6
1、 是升级版的插入排序，设置合理步长，逐步递减到步长1，为最后一步做预处理，减轻每次移动位置的问题
2、 按照步长，从左向右，选取位置，向前比较，如果前方更大对换位置，碰到边界就进行
3、

'''


class ShellSort:
    def shellSort(self, A, n):
        # write code here
        step = int(n/2)
        while step >0:
            for i in range(step,n):
                index = i
                pre = i - step
                while pre >= 0 :
                    if A[pre] > A[index]:
                        A[pre],A[index] = A[index],A[pre]
                    index = pre
                    pre = pre -step
            step -= 1

        return A

a= ShellSort()
out = a.shellSort([1,2,3,5,2,3],6)
print(out)



