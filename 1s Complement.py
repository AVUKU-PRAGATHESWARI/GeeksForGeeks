#User function Template for python3
class Solution:
            
    def onesComplement(self,S,N):
        result=''
        for i in str(S):
            if i=='1':
                result+='0'
            else:
                result+='1'
        return result
# https://practice.geeksforgeeks.org/problems/1s-complement2819/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions