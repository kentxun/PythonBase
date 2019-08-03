'''

如何判断一个单链表是否有环？有环的话返回进入环的第一个节点的值，无环的话返回-1。
如果链表的长度为N，请做到时间复杂度O(N)，额外空间复杂度O(1)。

给定一个单链表的头结点head（注意另一个参数adjust为加密后的数据调整参数
方便数据设置，与本题求解无关)，请返回所求值。
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ChkLoop1:
    def chkLoop(self, head, adjust):
        # write code here
        if head is  None or head.next is  None:
            return None

        fast = head
        slow = head
        index =0
        while fast and fast.next:
            # 这个方案容易第二次重返时，跳过了第一个节点，导致缺少通过一个
            if  index==0:
                fast = fast.next.next if fast.next else None
            else:
                fast = fast.next
            slow = slow.next
        # 出错原因，当fast 返回Head后，就不再是快速跳动
        #     if fast == slow:
        #         index +=1
        #         fast = head
        #         if index ==2:
        #             return slow.val
        # return -1
class ChkLoop:
    def chkLoop(self, head, adjust):
        # write code here
        if head is  None or head.next is  None:
            return None

        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next if fast.next else None
            slow = slow.next
            # 第一次判定是 确定有环，第二次是确入环位置
            if fast == slow:
                fast = head
                while fast!= slow:
                    fast = fast.next
                    slow = slow.next
                return slow.val
        return  -1
