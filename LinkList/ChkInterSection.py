'''
给定两个单链表的头节点head1和head2，如何判断两个链表是否相交？相交的话返回true，不相交交的话返回false。

给定两个链表的头结点head1和head2(注意，另外两个参数adjust0和adjust1用于调整数据,与本题求解无关)。
请返回一个bool值代表它们是否相交。

思路：
1. 查找入环节点
2. 如果一个有环一个无，则不相交
3. 如果都为空，按照无环检查
4. 如果不为空，都有环，按照有环处理

'''

#-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ChkIntersection:
    def chkInter(self, head1, head2, adjust0, adjust1):
        # write code here
        loop1 = self.chkinCir(head1)
        loop2 = self.chkinCir(head2)
        if loop2 and loop1:
            if loop1==loop2:
                return True
            cur = loop1.next
            while cur != loop1:
                if cur == loop2:
                    return True
                else:
                    cur = cur.next

            return self.getCirInsec(head1,head2,loop1,loop2)
        elif not loop1 and not loop2:
            return self.getCirInsec(head1,head2,None,None)
        else:
            return False

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
        return False

    def getlength(self, head, end):
        length = 0
        while head != end:
            length += 1
            head = head.next

        return length
