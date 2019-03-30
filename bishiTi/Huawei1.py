'''
回溯法解决 旅行商问题

输入： 5个坐标 200 0 200 10 200 50 200 25 200 30
输出： 最短距离
'''

import  math
import sys
n =6

inputN='200 0 200 10 200 50 200 25 200 30'
#inputN = sys.stdin.readline()
axis = inputN.split(' ')
axisNum=[0,0]
for i in axis:
    axisNum.append(int(i))

def dis(x1, y1, x2, y2): return math.sqrt((abs(x1-x2)**2)+(abs(y1-y2)**2))

graph = [[0 for _ in range(6)] for _ in range(6)]

for i in range(6):
    for j in range(6):
        if i==j:
            graph[i][j]=0
        else:
            graph[i][j]=dis(axisNum[2*i],axisNum[2*i+1],axisNum[2*j],axisNum[2*j+1])
bestway = ''
bestcost = math.inf
nowcost = 0
x = [0, 1, 2, 3, 4, 5]


def TSP(graph, n, s):
    global nowcost, bestcost
    # boundary
    if s == n:
        if graph[x[n - 1]][x[0]] != 0 and (nowcost + graph[x[n - 1]][x[0]] < bestcost):
            bestcost = nowcost + graph[x[n - 1]][x[0]]
    else:
        # search
        for i in range(s, n):
            # 如果下一节点不是自身 而且 求得的值小于目前的最佳值
            # 不符合要求及时剪枝
            if graph[x[i - 1]][x[i]] != 0 and nowcost + graph[x[i - 1]][i] < bestcost:
                x[i], x[s] = x[s], x[i]  # 交换一下
                nowcost += graph[x[s - 1]][x[s]]  # 将花费加入
                # 向下搜索
                TSP(graph, n, s + 1)
                nowcost -= graph[x[s - 1]][x[s]]  # 回溯上去还需要减去
                x[i], x[s] = x[s], x[i]


TSP(graph,n,1)
print(int(bestcost))