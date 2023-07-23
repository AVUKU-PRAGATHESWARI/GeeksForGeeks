class Solution:
	def isSame(self, s):
	    boundpoint=0
	    for i in s[::-1]:
	        if i.isdigit():
	            boundpoint+=1
	        else:
	            break
	    length=len(s)-boundpoint
	    number=int(s[(len(s)-boundpoint):len(s)])
	    if(length==number):
	        return 1
	    else:
	        return 0
# https://practice.geeksforgeeks.org/problems/string-with-numbers-at-its-end5749/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions

