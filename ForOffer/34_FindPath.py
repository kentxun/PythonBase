'''
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

下图的二叉树有两条和为 22 的路径：10, 5, 7 和 10, 12
      10
    5    12
 4    7

'''
'''
因为路径的固定到叶子节点，不适合用bfs，应当直接检查dfs
回溯一般有个记录路径的，路径在回溯的时候，及时返回上一层
二叉树的回溯思想：
1。 当前root，符合退出条件就退出，
2。 依次递归 当前root的左子树、右子树
3。 左右子树都检查完，当前root栈退出，
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        '''
递归先序遍历树， 把结点加入路径。
若该结点是叶子结点则比较当前路径和是否等于期待和。
弹出结点，每一轮递归返回到父结点时，当前路径也应该回退一个结点
        '''

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []

        result = []
        # 回溯法
        def FindPathMain(root, path, currentSum):
            currentSum += root.val

            path.append(root)
            isLeaf = root.left == None and root.right == None

            if currentSum == expectNumber and isLeaf:
                onePath = []
                for node in path:
                    onePath.append(node.val)
                result.append(onePath)

            if currentSum < expectNumber:
                if root.left:
                    FindPathMain(root.left, path, currentSum)
                if root.right:
                    FindPathMain(root.right, path, currentSum)

            path.pop()

        FindPathMain(root, [], 0)

        return result

class Solution2:
    def FindPath(self, root, expectNumber):
        import copy
        # write code here
        ret = []
        trace = []
        def dfs(root,s,ret,trace):
            trace.append(root.val)
            if not root.left and not root.right:
                if s == root.val:
                    ret.append(copy.deepcopy(trace))
            if root.left:
                dfs(root.left,s - root.val,ret,trace)
            if root.right:
                dfs(root.right,s - root.val,ret,trace)
            trace.pop()
        if not root:
            return []
        dfs(root,expectNumber,ret,trace)
        return ret

t1 = TreeNode(10)
t2 = TreeNode(5)
t3 = TreeNode(5)
t4 = TreeNode(7)
t5 = TreeNode(12)
t1.left = t2
t1.right =t5
t2.left=t3
t2.right=t4
# 涉及 深拷贝的问题
a = Solution2()
out = a.FindPath(t1,22)
print(out)