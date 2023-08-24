class Solution:
	def Addition(self, matrixA, matrixB):
		matrix3=[]
		rowlen = len(matrixA)
		collen = len(matrixA[0])
		for i in range(rowlen):
		    for j in range(collen):
		        temp = matrixA[i][j]
		        matrixA[i][j] = 0
		        temp += matrixB[i][j]
		        matrixA[i][j] = temp
		return matrixA