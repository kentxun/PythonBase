'''
首先我们介绍二叉树先序序列化的方式，假设序列化的结果字符串为str，初始时str等于空字符串。

先序遍历二叉树，如果遇到空节点，就在str的末尾加上“#!”，“#”表示这个节点为空，节点值不存在，
当然你也可以用其他的特殊字符，“!”表示一个值的结束。如果遇到不为空的节点，假设节点值为3，
就在str的末尾加上“3!”。现在请你实现树的先序序列化。

给定树的根结点root，请返回二叉树序列化后的字符串。
'''

# -*- coding:utf-8 -*-
'''实现两个函数，分别用来序列化和反序列化二叉树。
二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，
从而使得内存中建立起来的二叉树可以持久保存。序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，
序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreeToString:
    flag = -1
    def toString(self, root):
        # write code here
        res = []
        stack = []
        if root == None:
            return ''
        cur = root
        stack.append(cur)
        while len(stack):
            cur = stack.pop()
            if cur:
                res.append(str(cur.val)+'!')
                stack.append(cur.right)
                stack.append(cur.left)
            else:
                res.append('#!')
        return ''.join(res)

    def reverse_string(self,s):
        self.flag += 1
        l = s.split(',')
        if (self.flag >= len(s)):
            return None
        root = None
        if (l[self.flag] != '$'):
            root = TreeNode(int(l[self.flag]))
            root.left = self.reverse_string(s)
            root.right = self.reverse_string(s)
        return root