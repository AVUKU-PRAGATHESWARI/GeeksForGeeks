class Solution:
    def roundToNearest (self, N) : 
        #Complete the function
        N=int(N)
        if(N%10<=5):
            return N-(N%10)
        else:
            return N+(10-(N%10))
        
# https://practice.geeksforgeeks.org/problems/nearest-multiple-of-102437/1?page=1&difficulty[]=-1&difficulty[]=0&status[]=unsolved&category[]=Strings&sortBy=submissions