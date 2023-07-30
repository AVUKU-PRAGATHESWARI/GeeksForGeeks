class Solution:
	def removeDups(self, S):
	    result=''
	    for i in S:
	        if i not in result:
	            result+=i
	        else:
	            continue
	    return result
# https://practice.geeksforgeeks.org/problems/remove-duplicates3034/1?page=1&difficulty[]=0&status[]=unsolved&category[]=Strings&sortBy=submissions