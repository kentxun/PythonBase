# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 构建二叉树
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(inorder, postorder):
    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: TreeNode
    """
    if not inorder or not postorder:
        return None
    # 找出根节点，计算在list中的位置
    ind = inorder.index(postorder.pop())
    root = TreeNode(inorder[ind])
    # 划分两边递归
    root.right = buildTree(inorder[ind + 1:], postorder)
    root.left = buildTree(inorder[:ind], postorder)
    return root

# 前序思路类似，主要是找出根节点，然后利用中序遍历两边划分的特质