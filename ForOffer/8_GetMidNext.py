'''
题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''

'''
题解：
1. 中序遍历的顺序是 左中右，所以下一个节点是这个顺序
2. 如果当前节点的右子树不为空，则是右子树的最左孩子节点
2. 如果为空，向上找第一个左链接指向的树包含该节点的祖先节点
'''

# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode == None:
            return

        if pNode.right != None:
            node = pNode.right
            while node.left:
                node = node.left
            return node

        else:
            while pNode.next != None:
                parent = pNode.next
                if parent.left == pNode:
                    return parent
                pNode = pNode.next
        return

        collections
    '''中序遍历，下一个节点，如果是 根节点， 下一个节点就是 右子树的第一个左孩子
       如果是 左孩子，下一个就是根节点，沿着左链向上查找
       如果是 右孩子，向上找第一个左链接指向的树包含该节点的祖先节点（如果是左子树，下一个就是回到根，如果是右子树，就一直是右链，直到回到不是右链）
    '''
