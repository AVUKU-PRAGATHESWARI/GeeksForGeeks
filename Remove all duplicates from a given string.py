#User function Template for python3
class Solution:

	
	def removeDuplicates(self,str):
	    result = ''
	    for i in str:
	        if i not in result:
	            result+=i
	    return result

# https://practice.geeksforgeeks.org/problems/remove-all-duplicates-from-a-given-string4321/1?page=1&difficulty[]=0&status[]=unsolved&category[]=Strings&sortBy=submissions