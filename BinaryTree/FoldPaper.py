'''
请把纸条竖着放在桌⼦上，然后从纸条的下边向上⽅对折，压出折痕后再展 开。此时有1条折痕，突起的⽅向指向纸条的背⾯，
这条折痕叫做“下”折痕 ；突起的⽅向指向纸条正⾯的折痕叫做“上”折痕。
如果每次都从下边向上⽅ 对折，对折N次。请从上到下计算出所有折痕的⽅向。
给定折的次数n,请返回从上到下的折痕的数组，若为下折痕则对应元素为"down",若为上折痕则为"up".

1
返回：["down"]

思路2： 构建 的是 满二叉树
利用中序遍历，从右节点向左遍历，顺序是 右中左
左 为 Up 右 为 down
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FoldPaper:
    def foldPaper(self, n):
        # write code here
        ret = []
        self.fold(1,n,True,ret)
        return ret

    # 递归模拟 折叠过程
    def fold(self,i,N,down,ret):
        if i>N:
            return
        self.fold(i+1,N,True,ret)
        ret.append("down" if down else "up")
        self.fold(i+1, N,False,ret)

a = FoldPaper()
out = a.foldPaper(3)

'''
思路2： 构建 的是 满二叉树
利用中序遍历，从右节点向左遍历，顺序是 右中左
左 为 Up 右 为 down
->
就是正常中序遍历的 逆向结果
'''

class FoldPaper1:
    def foldPaper(self, n):
        root = self.buildTree(n)
        Middle_order = self.Middle(root)
        return Middle_order[::-1]

    def Middle(self, root):
        stack = []
        return_list = []
        x = root
        while (len(stack) or x):
            if x != None:
                stack.append(x)
                x = x.left
            else:
                temp = stack.pop()
                return_list.append(temp.val)
                x = temp.right

        return return_list

    def buildTree(self, n):
        sum_node = 2 ** n - 1
        i = 1
        queue = []
        root = TreeNode('down')
        queue.append(root)
        while i < sum_node:
            x = queue.pop(0)
            x.left = TreeNode('up')
            x.right = TreeNode('down')
            queue.append(x.left)
            queue.append(x.right)
            i += 2
        return root