'''

某公司雇有N名员工，每名员工可以负责多个项目，但一个项目只能交由一名员工负责。
现在该公司接到M个项目，令Ai,j表示第i名员工负责第j个项目所带来的收益，那么如果项目分配得当，总收益最大是多少？

第一行包含两个整数N和M，1≤N，M≤1000。

接下来N行，每行包含M个整数，第i行的第j个整数表示Ai,j，1≤Ai,j≤1000。
样例输入
3 3
1 3 3
2 2 2
3 2 1
样例输出
9
'''
import  sys
M,N = sys.stdin.readline().split(' ')
input = []
for i in range(int(N)):
    input.append(list(map(int,sys.stdin.readline().split(' '))))

out = 0
for i in range(int(M)):
    tmp = 0
    for j in  range(int(M)):
        if input[j][i] >= tmp:
            tmp = input[j][i]
    out += tmp
print(out)

