class Solution:

	def nextGreatest(self,arr, n):
	    g=arr[n-1]
        for i in range(n-2,-1,-1):
            temp=arr[i]
            arr[i]=max(g,arr[i+1])
            g=temp
        arr[n-1]=-1
        return arr

# https://practice.geeksforgeeks.org/problems/greater-on-right-side4305/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions