'''
小M要制作一种黑暗饮料，这种饮料的原料有n种，编号为1-n，已知小M的容器最多容纳V升材料，
黑暗料理的各种原料配比为 a1 : a2 : a3 : ... : an  , 每种原料分别有b1，b2，... bn升。

问小M最多可以制作多少升这种饮料。小M使用的各种原料体积和不能超过V。

输入第一行，两个正整数n 和 V，表示原料种类数和容器容积。(1<=n<=1000，1<=V<=1000000)

输入第二行包含n个数a1,a2,a3,...an，表示n种原料的配比。

输入第三行包含n个数b1,b2,b3...bn，表示小M拥有的各种原料数。

输入
1 100
1
40
样例输出
40.0000
'''
import  sys
import decimal
from decimal import Decimal
decimal.getcontext().prec =4
n,v=[int(v) for v in sys.stdin.readline().strip().split()]
level = [Decimal(v) for v in sys.stdin.readline().strip().split()]
origin = [Decimal(v) for v in sys.stdin.readline().strip().split()]
origin_dict = [[index,origin[index]]for index in range(n)]
sor = sorted(origin_dict,key=lambda x:x[1])

sumlevel = Decimal(sum(level))
flag = 0
max_v = Decimal(0)
now_v = Decimal(0)
for i in range(n):
    if sor[i][1] < Decimal((level[sor[i][0]]*v)/sumlevel):
        now_v = Decimal(sor[i][1]*sumlevel/level[sor[i][0]])
        flag = 1
        break

if not flag:
    print('%.4f'%v)
else:
    print('%.4f'%now_v)




