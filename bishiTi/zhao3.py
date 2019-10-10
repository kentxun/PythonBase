import  sys
n = int(sys.stdin.readline().strip())
lines= []
for _ in range(n-1):
    lines.append(list(map(int,sys.stdin.readline().split(' '))))

tmp_dit ={}
value_dict ={}
for ele in lines:
    if tmp_dit.__contains__(ele[0]):
        tmp_dit[ele[0]].append((ele[1],ele[2]))
    else:
        tmp_dit[ele[0]] = [(ele[1],ele[2])]
    if  not  tmp_dit.__contains__(ele[1]):
        tmp_dit[ele[1]] = []
print(tmp_dit)
for i in range(n,0,-1):
    if len(tmp_dit[i]) ==0:
        value_dict[i]=0
    else:
        tmp_value = []
        for t in tmp_dit[i]:
            tmp_value.append(value_dict[t[0]]+t[1])
        if max(tmp_value)<0:
            value_dict[i]=0
        else:
            value_dict[i]=max(tmp_value)
res= []
for i in range(1,n+1):
    res.append(str(value_dict[i]))

print(" ".join(res))