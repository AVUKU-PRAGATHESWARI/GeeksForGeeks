class Solution:
    def removeSpecialCharacter (self, S):
		#code here
		result=''
		for i in S:
		    if i.isalpha():
		        result+=i
		if result=='':
		    return -1
		return result
# https://practice.geeksforgeeks.org/problems/remove-all-characters-other-than-alphabets4923/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions