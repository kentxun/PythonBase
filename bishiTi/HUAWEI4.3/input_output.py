'''
4
1 2 3 4

'''
import  sys
n = int(sys.stdin.readline() )

'1 2 3 4'
n_list = sys.stdin.readline().split(' ')
n_list = ['1','2','3','4']
n_list = list(map(int, n_list))
print(n_list)


import sys
n = int(sys.stdin.readline().strip() )
res =[]
for _ in range(n):
    res.append(sys.stdin.readline().strip())

'''
out : 1 2 4 5
expect : [1,2,4,5]

true
'''
n_list = [1,2,4,5]
print(' '.join(map(str,n_list)))