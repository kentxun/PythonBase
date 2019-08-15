# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root :
            return []
        queen =[]
        res = []
        last = nlast = root
        queen.append(root)
        while queen:
            cur = queen.pop(0)
            res.append(cur.val)
            if cur.left:
                queen.append( cur.left)
                nlast = cur.left
            if cur.right:
                queen.append( cur.right)
                nlast = cur.right
            if last == cur:
                last = nlast
        return res
