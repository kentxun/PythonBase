'''
从二叉树的节点A出发，可以向上或者向下走，但沿途的节点只能经过一次，当到达节点B时，
路径上的节点数叫作A到B的距离。对于给定的一棵二叉树，求整棵树上节点间的最大距离。
给定一个二叉树的头结点root，请返回最大距离。保证点数大于等于2小于等于500.

'''
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class LongestDistance:
    ##得到最大距离只有三种情况，在根的左子树上获得最大距离，在右子树上获得最大距离，跨越根节点获得最大距离
    # 递归思想，逐步从左右子树上找最大距离，而跨越根节点的最大距离是，左右子树到根节点最远距离，也就是高度
    def findLongest(self, root):
        if root == None:
            return 0
        lmax = self.findLongest(root.left)
        rmax = self.findLongest(root.right)
        hmax = self.getHeight(root.left) + self.getHeight(root.right) + 1
        return max(lmax, rmax, hmax)

    # 递归获得获取最长的子树
    def getHeight(self, root):
        if root == None:
            return 0
        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)
        return max(lh, rh) + 1