
import copy
def findAllSeq(seq):
    res =[""]
    for i in seq:
        if i=='?':
            tmp =[]
            for index, item in enumerate(res):
                tmp.append(item+'0')
                tmp.append(item+'1')
            res = copy.deepcopy(tmp)
        else:
            for index, item in enumerate(res):
                res[index] += i
    return res

def getF(num,packets):
    origin = sorted(packets)
    first = origin[0]
    return packets.index(first)

out = getF(4,[8,9,1,5])



class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def winTeamId(ceo):
    if ceo.left is None and ceo.right is None:
        return ceo.value
    elif ceo.left is None and ceo.right is not None:
        return winTeamId(ceo.right) + ceo.value
    elif ceo.left is not None and ceo.right is None:
        return winTeamId(ceo.left) + ceo.value
    else:
        left = winTeamId(ceo.left)
        right = winTeamId(ceo.right)
        return min(left,right)+ceo.value

root = TreeNode(7)
left1 = TreeNode(3)
right1 = TreeNode(10)
left2 = TreeNode(1)
left3= TreeNode(0)
right_l=TreeNode(8)
right_r = TreeNode(12)

root.left=left1
root.right=right1
left1.left= left2
left2.left= left3
right1.left=right_l
right1.right= right_r
out = winTeamId(root)
print(out)