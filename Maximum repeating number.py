#User function Template for python3
class Solution:

	def maxRepeating(self,arr, n, k):
        mx=0
        for i in arr:
            if i>mx:
                mx = i
        tab=[0 for i in range(0,mx+1)]
        for i in arr:
            tab[i]+=1
        mx=max(tab)
        return tab.index(mx)
# https://practice.geeksforgeeks.org/problems/maximum-repeating-number4858/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions