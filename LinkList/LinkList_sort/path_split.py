'''
输入
5 /order/pnrList/pnrPriceList /order/pnrList/pnrPriceList/price /order/pnrList/pnrPriceList/price  /order/pnrList/pnrPriceList  /order/pnrList/pnrPriceList
输出
111 1111 1221 121 131
'''

import  sys
line = [i for i  in  sys.stdin.readline().strip().split()]
print(line)
dict_in ={}
n = line.pop(0)

res =[]
for i in line:
    if i not in dict_in:
        dict_in[i]=1
        length = len(i.strip('/').split('/'))
        res.append('1'*length)
    else:
        dict_in[i]+=1
        length = len(i.strip('/').split('/'))
        res.append('1'+str(dict_in[i])*(length-2)+'1')

print(' '.join(res))
