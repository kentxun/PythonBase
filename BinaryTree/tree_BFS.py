'''

有一棵二叉树，请设计一个算法，按照层次打印这棵二叉树。

给定二叉树的根结点root，请返回打印结果，结果按照每一层一个数组进行储存，

所有数组的顺序按照层数从上往下，且每一层的数组内元素按照从左往右排列。保证结点数小于等于500。

'''

class TreePrinter:
    def printTree(self, root):
        queue=[]
        line=[]
        res=[]
        if root == None:
            return res
        queue.append(root)
        nlast=last=root

        while len(queue):
            node = queue.pop(0)
            line.append(node.val)

            if node.left!=None:
                nlast=node.left
                queue.append(node.left)

            if node.right!=None:
                queue.append(node.right)
                nlast=node.right

            if node ==last:
                res.append(line)
                last=nlast
                line=[]
        return res