def getprim(start, end):
    p=start
    x=0
    res =[]
    while(p< end):
        result=True
        for i in range(2,p-1):
            if(p%i==0):
                result=False#如果P能被任意一个小于n的数整除，则非质数
        if result==True:
            res.append(p)#如果是质数，则打印
            x=x+1#计数+1
        p+=1#P+1
    return res

import  sys
start ,end = sys.stdin.readline().split(' ')
out = getprim(int(start),int(end))
out = map(str,out)
ten_digit = 0
one_digit = 0
for i in out:
    ten_digit += int(i[-2])
    one_digit += int(i[-1])
print(min(ten_digit,one_digit))

# 考虑情况不周， 比如边界情况，还有 最后计算十位数时候没考虑 个位数的情况