#User function Template for python3
class Solution:
	def maxProduct(self,arr, n):
		# code here
        arr.sort()
        product=arr[-1]*arr[-2]
        return product
# https://practice.geeksforgeeks.org/problems/maximum-product-of-two-numbers2730/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions