import  re

list_all =[]
legal=[]
ilegal =[]

while True:
    try:
        s= input().split()
        if re.match('[0-9|a-z|A-z]+$',s):
            if s not in legal:
                legal.append(s)
            else:
                ilegal.append(s)
    except EOFError:
        break
res1= []
for s in legal:
    left = 10 % len(s)
    out = s[left:]+s[:left]
    res1.append(out)

print(' '.join(legal))
print(' '.join(ilegal))
print(' '.join(res1))
print(' '.join(sorted(res1)))