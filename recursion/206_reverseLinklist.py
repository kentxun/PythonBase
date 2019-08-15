'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 1. 终止条件是，head到末尾了
# 2. 返回的是 一个已经倒序好的 列表
# 3. 递归操作： 每轮返回的是倒序好的链表
# 套路不完全适用，要改
'''
1。 递归
相当于将原链表中的节点从后向前一个一个拆下来并按顺序放入新链表，
原链表从后往前每拆一个节点，新链表p的尾部就加上这个被拆下的节点。

中间态：
5->4  3, 2 ,1 

利用栈保存着，当前层重的cur& pre ，每层指向都不一样
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(head,last,current):
            if not head or not head.next:
                return head
            last.next = current.next
            temp = current.next
            current.next = head
            return reverse(current,last,temp)
        last = head
        current = head.next
        return reverse(head,last,current)

# 尾递归
class Solution3:
    def reverseList(self, head: ListNode, tail=None) -> ListNode:
        if head: head.next, tail, head = tail, head, head.next
        return self.reverseList(head, tail) if head else tail
'''
func reverse(pre,cur *ListNode) *ListNode {
    if cur == nil {
        return pre
    }
    head := reverse(cur, cur.Next)
    cur.Next = pre
    return head
}

'''
class Solution4:
    def reverseList(self,head):
        def reverse(pre,cur):
            if not cur:
                return pre
            head = reverse(cur,cur.next)
            print(cur.val)
            cur.next = pre
            return head
        return reverse(None,head)

'''
2# 迭代
1. next保留head.next的位置
2. head断链，head.next 指向 pre
3. pre变为当前链表头位置
4. head向下滑动

中间态：
pre <------ head
|            |
2->1->None , 3-->| 4->5 
                   |
                  next 
'''
class Solution2:
    def reverseList(self,head):
        pre = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre



t1 = ListNode(1)
t2 = ListNode(2)
t3 = ListNode(3)
t4 = ListNode(4)
t1.next = t2
t2.next = t3
t3.next = t4
a =Solution4()
res = a.reverseList(t1)