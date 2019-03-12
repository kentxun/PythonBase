'''
给定一棵完全二叉树的根节点root，返回这棵树的节点个数。
如果完全二叉树的节点数为N，请实现时间复杂度低于O(N)的解法。
给定树的根结点root，请返回树的大小。

'''
# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class CountNodes:
    def count(self, root):
        if root != None:
            return 0
        return self.bs(root,1,self.mostLeftLevel(root,1))

    def bs(self,node,l,h):
        if l == h:
            return l
        if self.mostLeftLevel(node.right,l+1)==h:
            return

    def mostLeftLevel(self,node,level):
        while node!= None:
            level += 1
            node = node.left
        return level-1