'''
[[1,2,3,4,5],
[11,12,13,14,15],
[21,22,23,24,25],
[31,32,33,34,35],
[41,42,43,44,45]]
'''


import sys
tmp = []
rect = sys.stdin.readline().strip()
while rect!='\n':
    tmp.append(rect.split(' '))
    rect = sys.stdin.readline().strip()

def deal_line(t):
    for i in range(len(t)-2):
        if abs(t[i+1] - t[i] ) !=1 and abs(t[i+1] - t[i]) !=10:
            return False
    if abs(t[len(t)-1]- t[len(t)-2]!=1) and abs(t[len(t)-1]- t[len(t)-2]!=10) and abs(t[len(t)-1]- t[0]!=10) and abs(t[len(t)-1]- t[0]!=1):
        return False
    else:
        return True

for line in tmp:
    print(deal_line(line))