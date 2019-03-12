'''
有一棵二叉树，请设计一个算法判断这棵二叉树是否为平衡二叉树。

给定二叉树的根结点root，请返回一个bool值，代表这棵树是否为平衡二叉树。
'''

# -*- coding:utf-8 -*-

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class CheckBalance:
    def check(self, root):
        # write code here
        if self.che_recur(root)>0:
            return True
        return False

    def che_recur(self,root):
        if root == None:
            return  True
        left = self.che_recur(root.left)
        right = self.che_recur(root.right)
        if left<0 or right<0: return -1
        if abs(left-right) >1 : return -1
        return right+1 if right>left else left+1