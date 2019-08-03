'''
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    class BST:
        def __init__(self,isB,Depth):
            self.isB = isB
            self.depth = Depth

    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBST(root)

    # 1. 确定退出条件，本题：就是向下搜索到为空时返回
    # 2. 确定返回的内容，本题：root的left和right子树，包含（是否是平衡二叉树，高度）
    # 3. 确定每次递归解决的问题， 本题：确定当前root是否为平衡二叉树并返回，包含：检查子树是否平衡二叉树、高度差，返回需要返回的内容

    def isBST(self,root):
        if root is None:
            return self.BST(True,0)
        left = self.isBST(root.left)
        right = self.isBST(root.right)
        if left.isB == False or right.isB == False:
            return self.BST(False,0)
        if abs(left.depth - right.depth)>1:
            return self.BST(False,0)
        return self.BST(True,max(left.depth,right.depth)+1)