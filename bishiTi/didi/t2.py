'''
有一个魔法阵的形状是由n个阵基组成的正n边形。

“真正强大的魔法都是返璞归真的！”一位大魔导师这样说。

魔法学院的同学们开始改进魔法阵，他们从书上了解到，所有魔法阵的形状都是正K边形，K为大于等于三的正整数。一个魔法阵的威力等于构成魔法阵的阵基威力之和。

因此他们可以通过去掉一些阵基，改变魔法阵使得法阵的威力更大，但是因为他们只是学生，并不能移动阵基。如现在的魔法阵是正六边形，阵基威力值分别为：1，5，2，-3，3，-3。显然，我们选择第1，3，5号阵基构成正三角形法阵的威力变为6是最好的；我们不能选择1，2，5号阵基，因为这并不是一个正k边形。

现在给出你原来阵基的威力大小，请你求出魔法阵的最大的威力，如果去掉一部分阵基并不能增强法阵威力，也可以保持原样。

6
1 5 2 -3 3 -3
out
6
'''
import sys
n = int(sys.stdin.readline().strip())
Kline =list(map(int,sys.stdin.readline().split(' ')))

step = 2
res = 0
while n /step >=3 :
    if n % step ==0:
        if max(sum(Kline[::step]),sum(Kline[1::step]))<sum(Kline):
            out = sum(Kline)
        else:
            out= max(sum(Kline[::step]),sum(Kline[1::step]))
    else:
        out = sum(Kline)

    if res < out:
        res += out
    step+=1

print(res)