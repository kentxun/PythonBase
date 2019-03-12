import sys

n = int(sys.stdin.readline().strip())
q=[]

for i in range(1,n+1):
    q.append(i)
out =[]
while q:
    out.append(q.pop(0))
    if q:
        q.append(q.pop(0))

out = map(str,out)
print(' '.join(out))