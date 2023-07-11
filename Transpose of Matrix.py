
class Solution:
    def transpose(self, matrix, n):
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        return matrix

# https://practice.geeksforgeeks.org/problems/transpose-of-matrix-1587115621/1