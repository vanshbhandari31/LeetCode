class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row=[]
        col=[]
        for i in range (len(matrix)):
             for j in range(len(matrix[i])):
                 if matrix[i][j]==0:
                    row.append(i)
                    col.append(j)
        row=list(set(row))
        col=list(set(col))
        for k in range(len(row)):
            for i in range(len(matrix[row[k]])):
               matrix[row[k]][i]=0
        for k in range(len(col)):
            for i in range(len(matrix)):
               matrix[i][col[k]]=0