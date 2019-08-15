# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(left,right):
            if left is None and right is None:
                return  True
            if left is None or right is None:
                return  False
            return  left.val == right.val and isMirror(left.left,right.right) and \
                    isMirror(right.left,left.right)
        if root is None :
            return  True
        return isMirror(root,root)