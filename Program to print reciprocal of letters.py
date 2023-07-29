#User function Template for python3
class Solution:
    def reciprocalString(self, S):
        lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        result=''
        for i in S:
            if i in lower:
                index=lower.index(i)
                result+=lower[25-index]
            elif i in upper:
                index=upper.index(i)
                result+=upper[25-index]
            else:
                result+=i
        return result
    
# https://practice.geeksforgeeks.org/problems/program-to-print-reciprocal-of-letters36233623/1?page=1&difficulty[]=-2&status[]=unsolved&category[]=Strings&sortBy=submissions