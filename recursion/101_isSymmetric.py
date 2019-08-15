'''
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
1。 终止条件，遍历到底
2。 向上一级返回当前root下的两个的子树是否对称
3。 判断当前root下两个子树是否镜像，（子树根值相同，子树
'''
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


# 问题出在，不是比较当前的左子树右子树是否对称，而是比较root的左右子树里的是否对称，递归的不是当前的root，
# 而是 两个子树的根
class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True
        if root.left and root.right:
           if root.left.val == root.right.val:
                return True
           else:
                return False

        left = self.isSymmetric(root.left)
        right = self.isSymmetric(root.right)
        return  left&right