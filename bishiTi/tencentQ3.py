import sys
m,n = [int(i) for i in sys.stdin.readline().strip().split(' ')]
s=[]
for _ in range(n):
    s.append(int(sys.stdin.readline().strip()))

s.sort()
if s[0]!=1:
    print(-1)

sum = 0
ans = 0

while True:
    if sum>=m:
       print(ans)
       break
    for i in range(n-1,-1,-1):
        if s[i]<=sum+1:
            sum+=s[i]
            ans+=1
            break
