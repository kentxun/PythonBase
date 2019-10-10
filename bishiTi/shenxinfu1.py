class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preOrder(root,res):
    if root is None:
        res.append('#')
    else:
        res.append(root.val)
        preOrder(root.left,res)
        preOrder(root.right,res)

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


import  sys
n = int(sys.stdin.readline().strip())
listin= []
for _ in range(n):
    listin.append(sys.stdin.readline().strip())


root = layerDeserialize(listin)

res= []
preOrder(root,res)
for i in res:
    print(i)
