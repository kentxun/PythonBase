'''
有一个单链表，请设计一个算法，使得每K个节点之间逆序，
如果最后不够K个节点一组，则不调整最后几个节点。
例如链表1->2->3->4->5->6->7->8->null，K=3这个例子。
调整后为，3->2->1->6->5->4->7->8->null。因为K==3，所以每三个节点之间逆序，
但其中的7，8不调整，因为只有两个节点不够一组。
给定一个单链表的头指针head,同时给定K值，返回逆序后的链表的头指针。
'''

# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class KInverse:
    def inverse(self, head, k):
        # write code here
        if not head:
            return None
        pre_head = ListNode(0)
        pre_head.next = head

        pre = pre_head
        current = head
        tag =0

        while True:
            tmp = current
            for i in range(k):
                if tmp is None:
                    tag =1
                    break
                tmp = tmp.next
            if tag:
                break
            for i in range(k-1):
                tmp = current.next
                current.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            pre =current
            current=current.next

        return pre_head.next

if __name__ == '__main__':
    import sys
    line1 = sys.stdin.readline().split(' ')
    k = int(sys.stdin.readline().strip())
    tmp=head= ListNode(int(line1[0]))
    for i in range(1, len(line1)-1):
        tmp.next =  ListNode(int(line1[i]))
        tmp=tmp.next
    ob= KInverse()
    out = ob.inverse(head,k)
    res= []
    while out.next:
        res.append(str(out.val)+'->')
        out=out.next
    res.append(str(out.val))
    print(''.join(res))
