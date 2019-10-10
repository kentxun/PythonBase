
'''
二叉树反序列化
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ReverseSeq:

    def PredeserializeTree(self, list):
        if len(list) <= 0:
            return None
        val = list.pop(0)
        if val == '#':
            return  None
        else:
            root = TreeNode(int(val))
            root.left = self.PredeserializeTree(list)
            root.right = self.PredeserializeTree(list)
        return root


    def IndeserializeTree(self, list):
        if len(list) <= 0:
            return None
        val = list.pop(0)
        if val == '#':
            return None
        else:
            root = TreeNode(0)
            root.left = self.IndeserializeTree(list)
            root.val = int(val)
            root.right = self.IndeserializeTree(list)
        return root

    def PostdeserializeTree(self, list):
        if len(list) <= 0:
            return None
        val = list.pop(0)
        if val=='#':
            return None
        else:
            root = TreeNode(0)
            root.left = self.IndeserializeTree(list)
            root.right = self.IndeserializeTree(list)
            root.val= int(val)
        return root

    # 层次遍历 反序列化
    def layerOrder(self, root,listin):
        if len(listin) <=0:
            return  None
        queen = []
        val = listin.pop(0)
        layer = 0
        root = TreeNode(int(val))
        queen.append(root)
        while listin:
            if len(queen) == 2 ** layer:
                while queen:
                    head = queen.pop(0)
                    queen.append(head.left)
                    queen.append(head.right)



# 必须是完全二叉树
def listcreattree(root,llist,i):###用列表递归创建二叉树，
    if i<len(llist):
        if llist[i] =='#':
            return None
        else:
            root=TreeNode(k=llist[i])
            root.left=listcreattree(root.left,llist,2*i+1)
            root.right=listcreattree(root.right, llist,2*i+2)
            return root
    return root


def layerDeserialize(s):
    if len(s)==1 and s[0]=='#':
        return  None
    queen =[]
    head = TreeNode(s[0])
    queen.append(head)
    index =1
    while index< len(s):
        node = queen.pop(0)
        if node != None:
            left = TreeNode(s[index]) if s[index]!='#'else None
            index +=1
            queen.append(left)
            node.left = left
            right = TreeNode(s[index]) if s[index] != '#' else None
            index += 1
            queen.append(right)
            node.right = right
    return head