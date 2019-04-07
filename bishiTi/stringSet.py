import sys

# listall=[]
# stringin=sys.stdin.readline().strip()
# while stringin !='':
#     listall.append([i for i in stringin.split(',')])
#     stringin = sys.stdin.readline().strip()

def legal(stringA):
    legallist = []
    illegallist = []
    for i in stringA:
        if not ((ord(i)>=65 and ord(i)<=122) or (ord(i)<=57 and ord(i)>=48)):
            return [],stringA
    return stringA,[]


def loopleft(listin):
    if listin==[]:
        return []
    tmp = listin
    for t in range(10):
        tmp.append(tmp.pop(0))
    return tmp

def removedup(listin):
    listdict=[]
    for i in listin:
        if i not in listdict:
            listdict.append(i)
    return listdict

if __name__ == '__main__':
    listall=[]
    stringin=sys.stdin.readline().strip()
    while stringin !='':
        listall.append([i for i in stringin])
        stringin = sys.stdin.readline().strip()
    res1=[]
    res2=[]
    res3=[]
    res4=[]
    for t in listall:
        a,b = legal(t)
        if a!=[]:
            res1.append(''.join(a))
            res3.append(''.join(loopleft(a)))
        if b!=[]:
            res2.append(''.join(b))

    res1 = removedup(res1)
    res3 = removedup(res3)
    res4 = sorted(res3)

    print(' '.join(res1))
    print(' '.join(res2))
    print(' '.join(res3))
    print(' '.join(res4))



'''
abc
def  
==                
acd123             
44234tjg
aga'-=
ad--s
abd
123
abcdef
123456789012345678901234567890123456789012345678901234567890123
EDFG
SDFG
ABC
DEF	
cccc
a*b=1
abc
cccc
dd
def
87&&^
abc
asdfas
234abc35
765rgfh4sd
1231
123
==
EDFG
'''