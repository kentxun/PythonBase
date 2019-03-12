'''
有n个信封，包含n封信，现在把信拿出来，再装回去，要求每封信不能装回它原来的信封，问有多少种装法?

给定一个整数n，请返回装发个数，为了防止溢出，请返回结果Mod 1000000007的值。保证n的大小小于等于300。

测试样例：
2
返回：1
'''
class CombineByMistake:
    def countWays(self, n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        pre, last = 0, 1
        for i in range(3, n+1):
            t = (i - 1) * (pre + last) % 1000000007
            pre, last = last, t
        return last