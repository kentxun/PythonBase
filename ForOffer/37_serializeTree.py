class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreeToString:
    flag =-1
    res =[]
    def toString(self, root):
        # write code here
        res = []
        stack = []
        if root == None:
            return ''
        cur = root
        stack.append(cur)
        while len(stack):
            cur = stack.pop()
            if cur:
                res.append(str(cur.val)+'!')
                stack.append(cur.right)
                stack.append(cur.left)
            else:
                res.append('#')
        return ''.join(res)

    def Serialize(self,root):
        if not root: return ''
        self.res.append(root.val)
        self.Serialize(root.left)
        self.Serialize(root.right)


    def reverse_string(self, s):
        self.flag += 1
        l = s.split('!')
        if (self.flag >= len(s)):
            return None
        root = None
        if (l[self.flag] != '#'):
            root = TreeNode(int(l[self.flag]))
            root.left = self.reverse_string(s)
            root.right = self.reverse_string(s)
        return root

# 另外还有对应的各种遍历方式的反序列化
