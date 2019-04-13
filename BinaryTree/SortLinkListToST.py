# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''

链表转二叉树
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedListToBST(head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    if not head:
        return
    if not head.next:
        return TreeNode(head.val)
    slow, fast = head, head.next.next
    # 找到中间位置，断开分两部分，划分两个子树，数组同思路。
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    midtree = TreeNode(mid.val)
    midtree.left = sortedListToBST(head)
    midtree.right = sortedListToBST(mid.next)
    return midtree
