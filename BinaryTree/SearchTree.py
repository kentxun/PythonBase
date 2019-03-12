
'''
保证中序遍历情况下值递增
就是在 中序遍历的情况下，每个值都是递增的，需要记录当前与之前的
中序 是每个子树都保持 左 中 右
'''

# 二叉搜索树
# 中序遍历情况下，值递增则为二叉树
def isBSTree(head):
    minimum = -100000               # 设定一个最小值
    if head is None:
        return False
    prenum = minimum
    stack = []
    while head or len(stack) > 0:
        if head:
            stack.append(head)
            head = head.left
        else:
            head = stack.pop()
            if head.val < prenum:   # 保证中序遍历情况下值递增
                return False
            else:
                prenum = head.val
            head = head.right

    return True