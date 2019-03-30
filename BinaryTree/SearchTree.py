
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

class node():
    def __init__(self, k=None, l=None, r=None):
        self.val = k
        self.left = l
        self.right = r

def listcreattree(root,llist,i):###用列表递归创建二叉树，
    if i<len(llist):
        if llist[i] =='#':
            return None
        else:
            root=node(k=llist[i])
            root.left=listcreattree(root.left,llist,2*i+1)
            root.right=listcreattree(root.right, llist,2*i+2)
            return root
    return root




if __name__ == '__main__':
    root=node()
    import sys
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    llist = list(map(int, line.split()))
   # llist=[10,5,15,3,7,13,18]
    root=listcreattree(root,llist,0)
    print(isBSTree(root))
