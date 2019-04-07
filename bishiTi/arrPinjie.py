'''
输入：
3
2,5,6,7,9,5,7
1,7,4,3,4

输出：
2,5,6,1,7,4,7,9,5,3,4,7
'''
import  sys

string1= sys.stdin.readline().strip()
n = int(string1)
listall=[]
stringin=sys.stdin.readline().strip()
while stringin !='':
    listall.append([i for i in stringin.split(',')])
    stringin = sys.stdin.readline().strip()

list_length=len(listall)

res =[]
i=0

while any(listall):
    index =0
    if i > list_length-1 and any(listall):
        i=0
    while index <n and listall[i]!=[]:
        res.append(listall[i].pop(0))
        index+=1
    i+=1
out = ','.join(res)
print(out)