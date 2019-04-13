'''
请用非递归方式实现二叉树的先序、中序和后序的遍历打印。

给定一个二叉树的根结点root，请依次返回二叉树的先序，中序和后续遍历(二维数组的形式)。

'''
# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreeToSequence:
    def convert(self, root):
        # write code here
        out = []
        out.append(self.preOrder(root,[]))
        out.append(self.inOrder(root,[]))
        out.append(self.postOrder(root,[]))

        return out

    def preOrder(self,root,res):
        #res =[]
        stack = []
        if root == None:
            return []
        stack.append(root)
        while len(stack):
            cur  = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res

    def inOrder(self,root,res):
        #res = []
        stack = []
        if root == None:
            return  res
        cur = root
        while (len(stack) or cur):
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return  res


    def postOrder(self,root,res):
        stack1 = []
        stack2 = []
        #res =[]
        if root == None:
            return res
        stack1.append(root)
        while len(stack1):
            cur = stack1.pop()
            stack2.append(cur)
            if cur.left :
                stack1.append(cur.left)
            if cur.right:
                stack1.append(cur.right)

        while len(stack2):
            res.append(stack2.pop().val)

        return res

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
    nodes = [root]
    values = []
    while nodes:
        temp = []
        temp_nodes = []
        for i in nodes:
            temp.append(i.val)
            left = i.left
            right = i.right
            if left:
                temp_nodes.append(left)
            if right:
                temp_nodes.append(right)
        nodes = temp_nodes
        values.append(temp)
    return values

dict_a = {'code':1,'dept':2,'name':3,'a':1}
print(dict_a)