

class ArrDelNum:
    def delNum(self,arr,N):
        flag =0
        index =0
        LAST =len(arr)
        while LAST >1:
            if flag ==2 and arr[index]!=-1:
                arr[index] = -1
                flag=0
                LAST -=1
            elif arr[index]!=-1:
                flag+=1
            index += 1
            if index>= N:
                index=0
        for i in range(N):
            if arr[i]!= -1:
                return i

class Solution:
    def delnum(self,arr,N):
        flag =0
        index =0
        while len(arr)>1:
            if flag==2:
                arr.pop(index)
                flag =0
                index -=1
            else:
                flag +=1
            index += 1
            if index >= len(arr):
                index = 0
        return arr[0]


a = ArrDelNum()
out = a.delNum([0,1,2,3,4,5,6,7],8)
print(out)

b = Solution()
out1 =b.delnum([0,1,2,3,4,5,6,7],8)
print(out1)