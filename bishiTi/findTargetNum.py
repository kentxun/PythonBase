'''
给出一个不重复大于0数字的数组和一个目标，
求数组中数的组合的和得到该目标（数字不同组合顺序当做一个解）。
'''

class Solution:
    def find(self,num,target,tmp):
        if self.isFinished(tmp,target):
            print(tmp)
            return
        for i in range(len(num)):
            if num[i]!=-1 and sum(tmp)<=target:
                k = num[i]
                num[i] = -1
                tmp.append(k)
                self.find(num,target,tmp)
                num[i] = k
                tmp.remove(k)


    def isFinished(self, tmp, target):
        if tmp is None:
            return False
        if sum(tmp) == target:
            return True
        else:
            return False

a = Solution()
tmp =[]
res = a.find([2,3,6,7],9,tmp)
