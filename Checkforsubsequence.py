#User function Template for python3

class Solution:
    def isSubSequence(self, A, B):
        ind,count=0,0
        for i in range(len(B)):
            if A[ind]==B[i]:
                count+=1
                ind+=1
            if count>len(A)-1:
                break
        if count==len(A):
            return 1
        else:
            return 0
# https://practice.geeksforgeeks.org/problems/check-for-subsequence4930/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions