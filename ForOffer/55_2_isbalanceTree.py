'''
检查二叉树是否为平衡二叉树
平衡二叉树的特点： 高度差为不大于1，
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Soulution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return self.is_BST(pRoot)

    class isBST:
        def __init__(self,isbst,depth):
            self.isbst = isbst
            self.depth = depth

    def is_BST(self,root):
        if root is None:
            return self.isBST(True,0)
        left = self.is_BST(root.left)
        right = self.is_BST(root.right)
        if not left.isbst or not right.isbst:
            return self.isBST(False,0)
        if abs(left.depth-right.depth) >1:
            return self.isBST(False,0)
        return self.isBST(True,max(left.depth,right.depth)+1)

