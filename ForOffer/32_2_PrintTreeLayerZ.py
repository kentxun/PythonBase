'''
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def Print(self, root):
        # write code here
        if not root :
            return []
        queen =[]
        line =[]
        res = []
        flag = 0
        last = nlast = root
        queen.append(root)
        while queen:
            cur = queen.pop(0)
            line.append(cur.val)
            if cur.left:
                queen.append( cur.left)
                nlast = cur.left
            if cur.right:
                queen.append( cur.right)
                nlast = cur.right
            if last == cur:
                last = nlast
                if flag ==1:
                    line =line[::-1]
                res.append(line)
                flag = not flag
                line =[]
        return res