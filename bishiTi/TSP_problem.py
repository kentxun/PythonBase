
import math
n =5
inputN='200 0 200 10 200 50 200 25 200 30'
axis = inputN.split(' ')
axisNum=[0,0]
for i in axis:
    axisNum.append(int(i))
def dis(x1,y1,x2,y2):
    return math.sqrt((abs(x1-x2)**2)+(abs(y1-y2)**2))

graph = [[0 for _ in range(6)] for _ in range(6)]

for i in range(6):
    for j in range(6):
        if i==j:
            graph[i][j]=0
        else:
            graph[i][j]=dis(axisNum[2*i],axisNum[2*i+1],axisNum[2*j],axisNum[2*j+1])

i,j=1,0
sumpath =0
s =[]
s.append(0)
while True:
    k=1
    detemp = math.inf
    # 只保留
    while True:
        l=0
        flag=0
        if k in s:
            flag=1
        if flag==0 and graph[k][s[i-1]] <detemp:
            j=k
            detemp =graph[k][s[i-1]]
        k+=1
        if k>n:
            break
    s.append(j)
    i+=1
    sumpath+=detemp
    if i>n:
        break
sumpath+=graph[0][j]
print(sumpath)
