'''
如何判断两个有环单链表是否相交？
相交的话返回第一个相交的节点，不想交的话返回空。如果两个链表长度分别为N和M，
请做到时间复杂度O(N+M)，额外空间复杂度O(1)。

给定两个链表的头结点head1和head2(注意，另外两个参数adjust0和adjust1用于调整数据,与本题求解无关)。
请返回一个bool值代表它们是否相交。

方案：
对 相交点进行区分，有两种可能，环内相交以及环外相交
环外相交 等同于 无环链表的相交问题
环内相交  运用之前的单链寻找入环点的方法找到入环点，从入环点开始检查环内情况，停止条件是回到入环点

'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ChkIntersection:
    def chkInter(self, head1, head2, adjust0, adjust1):
        # write code here
        p1,p2=head1,head2
        Loop1 = self.chkinCir(p1)
        Loop2 = self.chkinCir(p2)
        if Loop1 == Loop2:
            return True

        cur =Loop1.next
        while cur != Loop1:
            if cur == Loop2:
                return True
            else:
                cur = cur.next

        return self.getCirInsec(head1, head2, Loop1, Loop2)
        # lenA =  self.getlength(head1,Loop1)
        # lenB =  self.getlength(head2,Loop2)
        #
        # if lenA>lenB:
        #     for _ in range(lenA-lenB):
        #         head1 = head1.next
        # else:
        #     for _ in range(lenB-lenA):
        #         head2 = head2.next
        #
        # for _ in range(min(lenA,lenB)):
        #     if head1==head2:
        #         return True
        #     else:
        #         head1 = head1.next
        #         head2 = head2.next
        #
        # return False

    def getCirInsec(self,head1,head2,loop1,loop2):
        lenA = self.getlength(head1, loop1)
        lenB = self.getlength(head2, loop2)

        if lenA > lenB:
            for _ in range(lenA - lenB):
                head1 = head1.next
        else:
            for _ in range(lenB - lenA):
                head2 = head2.next

        for _ in range(min(lenA, lenB)):
            if head1 == head2:
                return True
            else:
                head1 = head1.next
                head2 = head2.next
        return False

    def chkinCir(self,head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next if fast.next else None
            slow = slow.next
            # 第一次判定是 确定有环
            if fast == slow:
                return slow

    def getlength(self,head,end):
        length = 0
        while head!=end:
            length+=1
            head = head.next

        return length

