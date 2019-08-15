# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明: 叶子节点是指没有子节点的节点。

示例:
给定二叉树 [3,9,20,null,null,15,7]
'''

'''
分析
'''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        # 很关键，处理其中一个叶子结点为空的情况
        if root.left is None or root.right is None:
            return left + right +1
        return min(left,right)+1


