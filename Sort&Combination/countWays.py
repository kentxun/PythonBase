'''
在XxY的方格中，以左上角格子为起点，右下角格子为终点，每次只能向下走或者向右走，请问一共有多少种不同的走法

给定两个正整数int x,int y，请返回走法数目。保证x＋y小于等于12。
2,2
返回：2


排列组合公式：
Am^n = n!/(n-m)!
Cm^n = n!/(n-m)!m!  = An^m / m!
'''

class Robot:
    def countWays(self, x, y):
        # write code here
        # 长度不能直接使用，转换为走的步数
        n = self.factor(x+y-2)
        m = self.factor(y-1)
        z = self.factor(x-1)
        return n/(m*z)

    def factor(self,n):
        if 0<= n< 2 :
            return 1
        else:
            return self.factor(n-1)*n