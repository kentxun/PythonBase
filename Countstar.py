'''
给定矩形区域，检查四个角落都为0、1 即可
现在要从 这个矩阵中的矩阵 包含K个星星的矩形数


'''



class CountStars:
    def count(self,arr,m,n):
        dict_star ={}
        for i in range(1,m-1):
            for j in range(1,n-1):
                if arr[i][j] ==1 and arr[i-1][j]==1\
                    and arr[i+1][j]==1 and arr[i][j-1]==1  and arr[i][j+1]==1:
                        dict_star[i]=1

        for i in range(1,m-1):
            for j in range(1,n-1):

