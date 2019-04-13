import sys
n = int(sys.stdin.readline().strip())
stringa= sys.stdin.readline().strip()

count_0 = stringa.count('1')
count_1 = stringa.count('0')

if abs(count_0-count_1):
    print(abs(count_0-count_1))
else:
    print(0)
