'''
一棵二叉树原本是搜索二叉树，但是其中有两个节点调换了位置，使得这棵二叉树不再是搜索二叉树，
请找到这两个错误节点并返回他们的值。保证二叉树中结点的值各不相同。
给定一棵树的根结点，请返回两个调换了位置的值，其中小的值在前。
'''


# 寻找错误节点： 第一个错误节点为第一次降序时较大的节点
# 第二个错误节点为最后一次降序时较小的节点

# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 方案一 分两步，按照中序遍历取出值，是有序的从小到大的，再检查降序的情况
class FindErrorNode:
    def findError(self, root):
        # write code here
        if not root or (not root.left and not root.right):
            return []

        stack = []
        array = []
        cur = root
        # 中序
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                array.append(cur.val)
                cur = cur.right


        t = 0
        result = []
        cnt = len(array) - 1
        for i in range(cnt):
            if array[i + 1] < array[i]:
                if t == 0:
                    result.append(array[i])
                    result.append(array[i + 1])
                if t == 1:
                    # 发现第二次降序，弹出前一次中 较小值，换成 这次降序较小值
                    result.pop()
                    result.append(array[i + 1])
                t += 1
        result = result[::-1]
        return result

# 方案二 一边遍历一边记录
class FindErrorNode:
    def findError(self, root):
        # write code here
        if not root or (not root.left and not root.right):
            return []

        stack = []
        array = []
        cur = root
        # 中序
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                array.append(cur.val)
                cur = cur.right

