
class Solution:
    def TreeDepth(self,root):
        return 0  if root is None else 1+max(self.TreeDepth(root.left),self.TreeDepth(root.right))
