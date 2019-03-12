'''
有一棵二叉树，其中所有节点的值都不一样,找到含有节点最多 的搜索二叉子树,并返回这棵子树的头节点.

给定二叉树的头结点root，请返回所求的头结点,若出现多个节点最多的子树，返回头结点权值最大的。
'''

'''
基本情况分析：
1. 以Node节点为头，整棵树是最大搜索二叉树：
   左子树：以Node左孩子为头，最大搜索二叉树的最大值小于Node的节点值
   右子树：以Node右孩子为头，最大搜索二叉树的最小值大于Node的节点值
2. 不满足上述： 以Node为头整体不能连成搜索二叉树，此时最大搜索二叉树 = 两侧子树的最大搜索二叉树里 节点数较多的
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class MaxSubtree:
    def getMax(self, root):
        # write code here
        node, count, max, min = self.printout(root)
        return node

    def printout(self, root):
        if root == None:
            return None, 0, None, None
        else:
            Rnode, Rcount, Rmax, Rmin = self.printout(root.right)
            Lnode, Lcount, Lmax, Lmin = self.printout(root.left)
            if Lnode == None and Rnode == None:
                return root, 1, root.val, root.val
            elif Lnode == None and Rnode != None:
                if root.val < Rmin and Rnode == root.right:
                    return root, Rcount + 1, Rmax, root.val
                else:
                    return Rnode, Rcount, Rmax, Rmin
            elif Lnode != None and Rnode == None:
                if root.val > Lmax and Lnode == root.left:
                    return root, Lcount + 1, root.val, Lmin
                else:
                    return Lnode, Lcount, Lmax, Lmin
            else:
                if Lmax < root.val and root.val < Rmin and Lnode == root.left and Rnode == root.right:
                    return root, Lcount + Rcount + 1, Rmax, Lmin
                elif Lcount > Rcount:
                    return Lnode, Lcount, Lmax, Lmin
                elif Lcount < Rcount:
                    return Rnode, Rcount, Rmax, Rmin
                else:
                    if Lnode.val >= Rnode.val:
                        return Lnode, Lcount, Lmax, Lmin
                    else:
                        return Rnode, Rcount, Rmax, Rmin