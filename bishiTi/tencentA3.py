import sys
n , k = [int(i) for i in sys.stdin.readline().strip().split()]
num = [int(i) for i in sys.stdin.readline().strip().split()]
num = list(set(num))
num.sort()


if n==1 or k ==1 :
    print(num[0])
else:
    print(num[0])
    for i in range(2,k+1):
        if i > len(num):
            print(0)
        else:
            print(num[i-1]-num[i-2])

