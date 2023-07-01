#User function Template for python3
class Solution:
	def setBits(self, N):
		binary = str(bin(N).replace("0b", ""))
        return binary.count('1')

# https://practice.geeksforgeeks.org/problems/set-bits0143/1