class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self,A, n, X):
        A.sort()
        for i in range(0,n-1):
            left=i+1
            right=n-1
            while left<right:
                total=A[i]+A[left]+A[right]
                if total==X:
                    return True
                elif total<X:
                    left=left+1
                else:
                    right=right-1
        return False
    
# https://practice.geeksforgeeks.org/problems/triplet-sum-in-array-1587115621/1?page=1&status[]=unsolved&category[]=Arrays&sortBy=submissions