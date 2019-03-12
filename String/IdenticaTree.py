# -*- coding:utf-8 -*-
'''
1. 二叉树遍历，前序遍历，

'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class IdenticalTree:
    def chkIdentical(self, A, B):
        # write code here
        stringA =self.tranList(A)
        stringB =self.transList(B)
        if stringA in stringB:
            return True
        else:
            return False

    def transList(self,Node):
        if Node==None:
            return '#'
        String = str(Node.val)
        String += self.transList(Node.left)
        String += self.transList(Node.right)
        return String
