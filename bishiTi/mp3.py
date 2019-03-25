def up(pd,up,down,le):
    if le<=4:
        if pd==1:
            pd=le
        else:
            pd-=1
    else:
        if pd==1:
            pd=le
            up=le-3
            down=le
        else:
            pd-=1
            if pd<up:
                up-=1
                down-=1
    return pd,up,down

def don(pd,up,down,le):
    if le<=4:
        if pd==le:
            pd=1
        else:
            pd+=1
    else:
        if pd==le:
            pd=1
            up=11
            down=4
        else:
            pd+=1
            if pd>down:
                up+=1
                down+=1
    return pd,up,down

try:
    while True:
        n = input()
        n = int(n)
        cmd = input()
        pd,u,d = 1,1,n
        for i in cmd:
            if i=='U':
                pd,u,d = up(pd,u,d,n)
            else:
                pd,u,d = don(pd,u,d,n)
        print(' '.join(map(str,[i for i in range(u,d+1)])))
        print(pd)
except:
    pass