'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
'''

'''

核心思路：回溯法
1.先将matrix字符串映射为字符矩阵；
2.从原字符串中找到第一个跟str[0]相等的字符，得到其对应的在矩阵中的位置[r,c]
1）从[r,c]开始按 上、左、右、下的顺序搜索；
2）每当搜索到一个节点，先判断path是否包括它，包括就说明已经经过此节点，不能
再经过了；如果不包括，就将其加入path容器
3）直到搜索到str[length - 1]节点，说明成功找到，标记result为true，标记
isFinished为true,尽快结束所有的递归操作
4）如果某节点起的 上、左、右、下 都搜索过但还没找到结果，说明经过此节点的路
径都不满足题意，将其从path中删除，回溯到上一层继续找。

'''

class Solution:
    result = False
    isFinished = False

    def haspath(self,matrix, rows, cols, path):
        list_mat = matrix.split(' ')
        #mat = [['' for _ in range(cols) ] for _ in range(rows)]
        mat =[]
        tmp = 0
        for i in range(rows):
            line = []
            for j in range(cols):
                line.append(list_mat[tmp])
                tmp+=1
            mat.append(line)
        first = list_mat.index(path[0])
        x,y = first/4,first%4

    def backtracing(self,r,c,matrix,index):
        if Solution.isFinished : return



a=Solution()
a.haspath('a b c e s f c s a d e e',3,4,'s')



class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix:
            return False
        if not path:
            return True
        x = [list(matrix[cols*i:cols*i+cols]) for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if self.exist_helper(x, i, j, path):
                    return True
        return False

    def exist_helper(self, matrix, i, j, p):
        if matrix[i][j] == p[0]:
            if not p[1:]:
                return True
            matrix[i][j] = ''
            if i > 0 and self.exist_helper(matrix, i-1, j, p[1:]):
                return True
            if i < len(matrix)-1 and self.exist_helper(matrix, i+1, j ,p[1:]):
                return True
            if j > 0 and self.exist_helper(matrix, i, j-1, p[1:]):
                return True
            if j < len(matrix[0])-1 and self.exist_helper(matrix, i, j+1, p[1:]):
                return True
            matrix[i][j] = p[0]
            return False
        else:
            return False