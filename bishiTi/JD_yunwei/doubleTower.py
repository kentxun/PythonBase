'''
现在有红，绿两种颜色的石头，现在我们需要用这两种石头搭建一个塔，塔需要满足如下三个条件：

1． 第1层应该包含1块石头，第2层应该包含两块，第 i 层需要包含 i 块石头。

2． 同一层的石头应该是同一个颜色（红或绿）。

3． 塔的层数尽可能多。

问在满足上面三个条件的前提下，有多少种不同的建造塔的方案，当塔中任意一个对应位置的石头颜色不同，我们就认为这两个方案不相同。石头可以不用完。
'''

'''
样例输入
4 6
样例输出
2
'''
import  sys
stick =[int(i) for i in sys.stdin.readline().strip().split()]

def depth(num):
    return int((1+4*num )**0.5/2+1)


def solve(stick):
    dict_tmp ={i+1 :-1 for i in range(depth(sum(stick)))}
    dept = depth(sum(stick))
    k = 1
    res= []
    flag =0
    while k >= 1:
        # 查看下一列
        if k == dept :
           res.append(dict_tmp)
           dict_tmp ={i:-1 for i in range(sum(stick))}
        if  stick[0] > k:
            if dict_tmp[k] and flag:
                stick[0] -= k
                dict_tmp[k] = 0
                k+=1
            else:
                stick[0] -= k
                dict_tmp[k] = 0
                flag =0
                k += 1
        elif stick[1] > k:
            if (1-dict_tmp[k]) and  flag:
                stick[1] -=k
                dict_tmp[k] = 1
                k += 1
            else:
                stick[1] -= k
                dict_tmp[k] = 1
                flag = 0
                k += 1
        else:
            k -=1
            flag = 1
        if k == dept :
           res.append(dict_tmp)
           dict_tmp ={i:-1 for i in range(sum(stick))}
    return res


out= solve(stick)
tmp =[]
count =0
for i in out:
    if i  not in tmp:
        tmp.append(i)
        count+=1
print(out)