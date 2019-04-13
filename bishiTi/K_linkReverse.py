class LinkList:
    def __init__(self,x):
        self.val = x
        self.next =None

class Kreverse:
    def reverseKgroup(self,head,k):
        t = head
        tot = 0
        p =t
        if k ==1:
            return head
        while p != None:
            p = p.next
            tot +=1
        cnt =0
        while t!= None:
            if cnt+k <= tot:
                if cnt == 0:
                    head = self.reverse(t,k)
                    cnt += k
                else:
                    i = t.next
                    newhead = self.reverse(i,k)
                    cnt += k
                    t.next = newhead
                    t = i
            else:
                break
        return  head


    def reverse(self,t,k):
        count = 1
        oldhead = t
        while count <k:
            nowhead = t.next
            t.next= nowhead.next
            nowhead.next = oldhead
            oldhead = nowhead
            count +=1
        return nowhead

if __name__ == '__main__':
    import  sys
    linkin = [int(i) for i in sys.stdin.readline().strip()[1:-1].split(',')]
    k = int(sys.stdin.readline().strip())
    head = LinkList(None)
    cnt = LinkList(None)
    for i in linkin:
        if  not cnt.val:
            cnt.val = i
            head = cnt
        else:
            cnt.next= LinkList(i)
            cnt = cnt.next
    a = Kreverse()
    out = a.reverseKgroup(head,k)
    res =[]
    while out:
        res.append(str(out.val))
        out = out.next
    print('['+','.join(res)+']')