import sys
import math
n =6

#inputN = sys.stdin.readline()
inputN='200 0 200 10 200 50 200 25 200 30'
axis = inputN.split(' ')
axisNum=[0,0]
for i in axis:
    axisNum.append(int(i))
def dis(x1,y1,x2,y2):
    return int(math.sqrt((abs(x1-x2)**2)+(abs(y1-y2)**2)))

graph = [[0 for _ in range(6)] for _ in range(6)]

for i in range(6):
    for j in range(6):
        if i==j:
            graph[i][j]=0
        else:
            graph[i][j]=dis(axisNum[2*i],axisNum[2*i+1],axisNum[2*j],axisNum[2*j+1])

