

'''
链表的快速排序实现 ，空间复杂度是O（1）
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def quickSortList(self,head):
        if head is None or head.next is None:
            return head
        tmpHead = ListNode(0)
        tmpHead.next =head
        self.qsortList(tmpHead,head,None)
        return tmpHead.next

    def qsortList(self,headPre,head,tail):
        if head!= tail and head.next !=tail:
            mid = self.partitionList(headPre,head,tail) # 这里Head不能指向链表表头
            self.qsortList(headPre,headPre.next,mid)
            self.qsortList(mid,mid.next,tail)


    def partitionList(self,lowPre,low,hight):
        key = low.val
        node1 ,node2 = ListNode(0),ListNode(0)
        little = node1
        big = node2
        tmp = low.next
        while tmp!=hight:
            if tmp.val <key:
                little.next = tmp
                little =tmp
            else:
                big.next = tmp
                big = tmp
            tmp=tmp.next
        big.next=hight # 保证后半部分
        little.next=low
        low.next =node2.next
        lowPre.next = node1.next # 保证前半部分
        return low


