class Solution:
    def factorial(self, N):
        #code here
        fac=1
        for i in range(2,N+1):
            fac*=i
        return str(fac)
    
# https://practice.geeksforgeeks.org/problems/factorials-of-large-numbers2508/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions