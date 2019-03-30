class Solution:
    """
    Get all distinct N-Queen solutions
    @param n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        #每一行和每一列只能有一个皇后 而且必定有一个皇后
        n = int(n)
        result = []
        col = [-1]*n
        k = 0
        #row
        while k>=0:
            #查看下一列
            col[k] = col[k]+1
            while col[k]<n and not self.judgePlace(k,col):
                #col
                col[k] += 1
            if col[k]<n:
                #获得一次解
                if k == n-1:
                    empty = ['.'*n for i in range(0,n)]
                    for i in range(0,n):
                        temp = list(empty[i])
                        temp[col[i]] = 'Q'
                        empty[i] = ''.join(temp)
                    result.append(empty)
                #判断下一行
                else:
                    k +=1
                    #清除残留数据
                    col[k] = -1
            #没有找到结果回溯
            else:
                k -= 1


        return result

    def judgePlace(self,k,col):
        for i in range(0,k):
            if col[i] == col[k] or (abs(col[k]-col[i]) == abs(k - i)):
                return False
        return True



class Nqueen:
    def judge(self,k,col):
        for i in range(0,k):
            if col[i] == col[k] or (abs(col[k] - col[i]) == abs(k - i)):
                return False
        return True

    def slove(self,N):
        col = [-1] * N
        k = 0
        self.findT(col,k,N)


    def find(self,col,row,N):
        for i in range(N):
            col[row]=i
            if self.judge(row,col):
                if row==N-1:
                    print(col)
                    return
                else:
                    self.find(col,row+1,N)
            col[row]=-1

    def findT(self,col,row,N):
        while row<N:
            while col[row]<N:
                col[row] +=1
                if self.judge(row,col):
                    if row == N-1:
                        print(col)
                        break
                    else:
                        row+=1
            col[row] = -1
            row-=1

a = Nqueen()
a.slove(4)




