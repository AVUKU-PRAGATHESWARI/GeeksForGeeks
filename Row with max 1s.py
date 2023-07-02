#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
	    maxi=-1
	    count=0
		for i in range(len(arr)):
		    index = arr[i]
		    if count < index.count(1):
		        count = index.count(1)
		        maxi=i
		return maxi

# https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1?page=1&status[]=unsolved&category[]=Arrays&sortBy=submissions