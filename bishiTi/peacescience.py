'''

aqwww

a1 q1 w3
'''
#
# import  sys
# string = sys.stdin.readline().strip()
# fast = 0
# slow = 0
# res = []
#
# while fast!=len(string):
#     if string[fast]!= string[slow]:
#         res.append(string[slow]+str(fast-slow))
#         slow=fast
#     fast+=1
# res.append(string[slow]+str(fast-slow))
# print(" ".join(res))
#
#
# s =0
# res2 = []
# for f in range(len(string)):
#     if string[f] != string[s]:
#         res2.append(string[s]+str(f-s))
#         s=f
# res2.append(string[s]+str(len(string)-s))
# print(res2)
#

# -*- coding:utf-8 -*-
str_in = input().strip().split(' ')
dict_str={}
for i in str_in:
    tmp = i.split(':')
    dict_str[tmp[0]]= tmp[1]
out= sorted(dict_str.items(),key=lambda x:x[1],reverse=True)

res= []
for i in out:
    res.append(i[0]+':'+i[1])
print(' '.join(res))
