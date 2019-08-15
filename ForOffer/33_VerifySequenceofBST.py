'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
'''


'''
思路

BST的后序序列的合法序列是，对于一个序列S，最后一个元素是x （也就是根），如果去掉最后一个元素的序列为T，
那么T满足：T可以分成两段，前一段（左子树）小于x，后一段（右子树）大于x，且这两段（子树）都是合法的后序序列。
'''


'''
二叉搜索树的特点：  root的左半边比root小， 右边比root大
递归检查，二分查找，两侧检查
'''
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        def verify(sequence):
            length = len(sequence)
            if length == 1 or length == 0:
                return True
            root = sequence[-1]
            left = 0
            while sequence[left] < root:
                    left += 1
            for j in range(left, length-1):
                if sequence[j] < root:
                    return False
            return verify(sequence[:left]) and verify(sequence[left:length-1])
        if not sequence:
            return False
        return verify(sequence)


class Solution1:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False

        length = len(sequence)
        root = sequence[-1]

        for i in range(length):
            if sequence[i] > root:
                break
        while i < length - 1:
            if sequence[i] < root:
                return False
            i += 1

        left = sequence[:i]
        right = sequence[i:length - 1]

        leftIs = True
        rightIs = True

        if len(left) > 0:
            leftIs = self.VerifySquenceOfBST(sequence=left)
        if len(right) > 0:
            rightIs = self.VerifySquenceOfBST(sequence=right)
        return leftIs and rightIs

a = Solution()
a.VerifySquenceOfBST([4,6,7,5])