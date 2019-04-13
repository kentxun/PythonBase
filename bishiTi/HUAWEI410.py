import sys
List = [i for i in sys.stdin.readline().strip().split()]
res = []
for i in range(1, int(List[0])+1):
    for j in range(0,len(List[i]),8):
        res.append(List[i][j:j+8])

for t in range(len(res)):
    res[t] = res[t]+'0'*(8-len(res[t]))
res.sort()
print(' '.join(res))
