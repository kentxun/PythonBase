
import math

class Soulution:
    def __init__(self,StrPut):
        self.axisNum = [0, 0]
        self.graph = [[0 for _ in range(6)] for _ in range(6)]

    def dis(self,x1, y1, x2, y2):
        return math.sqrt((abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2))

    def StrInput(self,StrPut):
        axis = StrPut.split(' ')
        for i in axis:
            self.axisNum.append(int(i))

        self.N = int(len(self.axisNum) / 2)

        self.graph = [[0 for _ in range(self.N)] for _ in range(self.N)]

        for i in range(self.N):
            for j in range(self.N):
                if i == j:
                    self.graph[i][j] = 0
                else:
                    self.graph[i][j] = self.dis(self.axisNum[2 * i], self.axisNum[2 * i + 1], self.axisNum[2 * j], self.axisNum[2 * j + 1])

    def dp_tsp(self):
        dp=self.graph


import numpy as np

N = 6
path = np.ones((2**(N+1),N))
dp = np.ones((2**(N+1),N))* -1


def TSP(s,init,num):
    if dp[s][init] !=-1 :
        return dp[s][init]
    if s==(1<<(N)):
        return graph[0][init]
    sumpath=1000000000
    for i in range(N):
        if s&(1<<i):
            m=TSP(s&(~(1<<i)),i,num+1)+dist[i][init]
            if m<sumpath:
                sumpath=m
                path[s][init]=i
    dp[s][init]=sumpath
    return dp[s][init]

