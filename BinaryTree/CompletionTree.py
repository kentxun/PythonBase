'''
判断是否是 完全二叉树，树的节点小于等于500

'''

# class CheckCompletion:
#     def check(self,root):
#         queen = []
#         if root==None:
#             return False
#
#         queen.append(root)
#         while queen:
#             cur = queen.pop(0)
#             if cur.right and not cur.left:
#                 return False
#             elif cur.right and cur.left: # 只判断这个情况会导致 只有左支的情况被遗漏
#                 queen.append(cur.left)
#                 queen.append(cur.right)
#             else:
#                 while queen:
#                     tmp = queen.pop(0)
#                     if tmp.left or tmp.right:
#                         return False
#         return True

# 减少了内部的一个循环，修改了一个bug 处理只有左支情况，同时还是要把子节点加进去的
class CheckCompletion1:
    def check(self,root):
        queen = []
        if root==None:
            return False
        queen.append(root)
        flag =False
        while queen:
            cur = queen.pop()
            if cur.right and not cur.left:
                return False
            if cur.left :
                queen.append(cur.left)

            if cur.right :
                queen.append(cur.right)
            if flag :
                if cur.left or cur.right:
                    return False

            if not (cur.right and cur.left):
                Flag =True
        return True
