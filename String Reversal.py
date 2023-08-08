class Solution:
    def reverseString(self, s):
        new = ''
        s=s[::-1]
        for i in s:
            if i not in new and i!=' ':
                new+=i
        return new
    
# https://practice.geeksforgeeks.org/problems/string-reversalunpublished-for-now5324/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions