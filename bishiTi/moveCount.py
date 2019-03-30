
class Solution1:
    def movingCount(self,threshod,rows,cols):
        markmatrix = [False] *(rows*cols)
        count = self.Getnum(threshod,rows,cols,0,0,markmatrix)
        return count

    def Getnum(self,threshold,rows,cols,row,col,marktrix):
        count =0
        if self.GetSum(threshold,rows,cols,row,col,marktrix):
            marktrix[row*col +col] = True
            count = 1 + self.Getnum(threshold,rows,cols,row-1,col,marktrix)+\
                self.Getnum(threshold,rows,cols,row,col-1,marktrix) +\
                self.Getnum(threshold,rows,cols,row+1,col,marktrix) + \
                self.Getnum(threshold,rows,cols,row,col+1,marktrix)
        return count

    def GetSum(self,threshold,rows,cols,row, col, marktrix):
        if row >=0 and row <= rows and col>=0 and col< cols \
                and self.getDig(row)+self.getDig(col) <= threshold \
                and not marktrix[row*col +col]:
            return True
        return False

    def getDig(self, num):
        sumNum = 0
        while num > 0:
            sumNum += num % 10
            num = num//10
        return sumNum


class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold < 0 or rows <= 0 or cols <= 0:
            return 0
        visitmatrix = [0] * (rows * cols)  # 标记矩阵
        count = self.movingCountCore(threshold, rows, cols, 0, 0, visitmatrix)
        return count

    def movingCountCore(self, threshold, rows, cols, row, col, visitmatrix):
        count = 0
        if self.check(threshold, rows, cols, row, col, visitmatrix):
            visitmatrix[row * cols + col] = True
            count = (1 + self.movingCountCore(threshold, rows, cols, row - 1, col, visitmatrix)
                     + self.movingCountCore(threshold, rows, cols, row, col + 1, visitmatrix)
                     + self.movingCountCore(threshold, rows, cols, row + 1, col, visitmatrix)
                     + self.movingCountCore(threshold, rows, cols, row, col - 1, visitmatrix))
        return count

    def check(self, threshold, rows, cols, row, col, visitmatrix):
        if (row >= 0 and row < rows and col >= 0 and col < cols and
                self.getDigitSum(row) + self.getDigitSum(col) <= threshold and
                not visitmatrix[row * cols + col]):
            return True
        return False

    def getDigitSum(self, number):
        sum = 0
        while number > 0:
            sum += number % 10  # 先个位，然后十位。。。
            number /= 10  # 从个位不断往前走，个位，十位。。。
        return sum

class Solution1:
    def movingCount(self, threshold, rows, cols):
        self.row, self.col = rows, cols
        self.dict = set()
        self.search(threshold, 0, 0)
        return len(self.dict)

    def judge(self, threshold, i, j):
        return sum(map(int, list(str(i)))) + sum(map(int, list(str(j)))) <= threshold

    def search(self, threshold, i, j):
        if not self.judge(threshold, i, j) or (i, j) in self.dict:
            return
        self.dict.add((i, j))
        if i != self.row - 1:
            self.search(threshold, i + 1, j)
        if j != self.col - 1:
            self.search(threshold, i, j + 1)

if __name__ == '__main__':
    a = Solution()
    import sys
    x,y,k = [int(i) for i in sys.stdin.readline().split()]
    out = a.movingCount(k,x,y)
    print(out)