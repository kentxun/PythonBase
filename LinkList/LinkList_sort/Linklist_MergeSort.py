
'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
输入: 4->2->1->3
输出: 1->2->3->4
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self,head):
        if head is None or head.next is None:
            return  head

        mid =self.get_mid(head)
        left = head
        right = mid.next
        mid.next = None

        self.sortList(left)
        self.sortList(right)
        return self.merge(left,right)

    def merge(self,p,q):
        tmp = ListNode(0)
        h = tmp
        # 保留头结点
        while p and q:
            if p.val <q.val:
                h.next = p
                p = p.next
            else:
                h.next = q
                q= q.next
        # 处理剩余情况
        if p:
            h.next = p
        if q:
            h.next = q
        return tmp.next

    def get_mid(self,node):
        if node is None:
            return node
        fast = slow = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next if fast.next else None
        return slow
