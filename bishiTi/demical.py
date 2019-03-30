'''
求a/b的小数表现形式。如果a可以整除b则不需要小数点。
如果是有限小数，则可以直接输出。如果是无限循环小数，则需要把小数循环的部分用"()"括起来。

两个整数a和b，其中

0 <= a <= 1000 000

1 <= b <= 10 000

'''
class Solution:
    def demicalString(self):
        a,b = [int(i) for i in input().split()]
        if a%b==0:
            print(a//b)
        else:
            cache=[]
            decimal = ''
            print(a//b,end='.')
            a = a%b
            while True:
                if a in cache:
                    p = cache.index(a)
                    finite =True
                    break
                cache.append(a)
                a=a*10
                decimal=decimal+'{}'.format(a//b)
                a=a%b
                if a == 0:
                    finite =False
                    break
            if finite:
                print('{0}({1})'.format(decimal[:p] , decimal[p:]))
            else:
                print(decimal)


a=Solution()
a.demicalString()