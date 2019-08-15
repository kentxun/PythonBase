'''
翻转一棵二叉树。
示例：
输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def  invert(root):
            if root is None:
                return
            left = invert(root.left)
            right = invert(root.right)
            root.left,root.right = right, left
            return  root
        newroot = invert(root)
        return newroot