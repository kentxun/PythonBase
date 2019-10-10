import  sys
n = int(sys.stdin.readline().strip())
alist= list(map(int,sys.stdin.readline().split(' ')))
blist = list(map(int,sys.stdin.readline().split(' ')))

out = 0
for i in range(n):
    if blist[i] <= alist[i]+alist[i+1]:
        out += blist[i]
        if blist[i]> alist[i]:
            alist[i+1]= alist[i+1]-(blist[i]-alist[i])
    else:
        out += alist[i]+alist[i+1]
        alist[i+1] = 0
print(out)