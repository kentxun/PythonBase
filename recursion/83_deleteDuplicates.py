'''
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
套路：
1。 head到底
2。 返回一个已经去重的链表，存放已有元素的dict
3。 递归操作： 检查当前所在位置元素，与后部分是否重复，重复的话去除，返回

链表套路：
递归的程序里，一定放着head.next,而当前head的状态存在当前的栈内，也就是说不会造成，利用递归栈向后遍历，利用返回进行反向
递归的程序栈的每一层都放着的是当前的head的状态，没有带入下一层
'''
# di = {'1':1,'2':2}
# di.__contains__()


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        def delete(head, dic):
            if not head:
                return head
            cur = delete(head.next, dic)
            if  dic.__contains__(head.val):
                return cur
            else:
                dic[head.val] = 0
                head.next= cur
                return head
        dic = {}
        return delete(head,dic)

t1 = ListNode(1)
t2 = ListNode(2)
t3 = ListNode(3)
t4 = ListNode(2)
t1.next = t2
t2.next = t3
t3.next = t4
a =Solution()
res = a.deleteDuplicates(t1)
print(res.val,res.next.val,res.next.next.val)