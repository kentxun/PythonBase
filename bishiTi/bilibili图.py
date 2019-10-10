import  sys,re

line1 = re.split('[+]',sys.stdin.readline().strip())
line2 = re.split('[+]',sys.stdin.readline().strip())

a = int(line1[0])
c = int(line2[0])

if len(line1[1])==1:
    b = 1
else:
    b = int(line1[1][:-1])

if len(line2[1]) == 1:
    d = 1
else:
    d = int(line2[1][:-1])

