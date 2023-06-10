#User function Template for python3
class Solution:

	def kLargest(self,arr, n, k):
		arr = sorted(arr, reverse=True)
		return arr[:k]

# https://practice.geeksforgeeks.org/problems/k-largest-elements4206/1?page=2&status[]=unsolved&category[]=Arrays&sortBy=submissions