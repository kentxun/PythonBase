'''
请用递归方式实现二叉树的先序、中序和后序的遍历打印。
给定一个二叉树的根结点root，请依次返回二叉树的先序，中序和后续遍历(二维数组的形式)。


除了 二叉树的遍历顺序，主要考察的是 对于遍历的理解，遍历需要传入能够用于递归的对象
'''

class TreeToSequence:
    def convert(self, root):
        # write code here
        res1,res2,res3 = [],[],[]
        self.preOrder(root,res1)
        self.inOrder(root,res2)
        self.postOrder(root,res3)

        return [res1,res2,res3]

    def preOrder(self,root,res):
        if root is None:
            return root
        else:
            res.append(root.val)
            self.preOrder(root.left,res)
            self.preOrder(root.right,res)
        return res

    def inOrder(self,root,res):
        if root is None:
            return root
        else:
            self.inOrder(root.left,res)
            res.append(root.val)
            self.inOrder(root.right,res)
        return res

    def postOrder(self,root,res):
        if root is None:
            return root
        else:
            self.postOrder(root.left,res)
            self.postOrder(root.right,res)
            res.append(root.val)
        return res
    


