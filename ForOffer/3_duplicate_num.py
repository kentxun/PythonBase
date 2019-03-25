'''
在一个长度为 n 的数组里的所有数字都在 0 到 n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的，也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。

Input:
{2, 3, 1, 0, 2, 5}

Output:
2
要求 ：  时间O(N) 空间O(1)
'''
'''
思路，只遍历一次，利用索引坐标存放，如果当前索引上已有当前索引值的数字
'''


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if len(numbers) == 0:
            return False

        for i in range(len(numbers)):
            if numbers[i] != i:
                if numbers[numbers[i]] == numbers[i]:
                    duplication.append(numbers[i])
                    print(duplication)
                    return True
                else:
                    # 不能直接交换，number[i]的值会动态变化
                    num = numbers[i]
                    numbers[i], numbers[num] = numbers[num], numbers[i]
        return False


a= Solution()
out = a.duplicate([2,1,3,1,4],[])
print(out)