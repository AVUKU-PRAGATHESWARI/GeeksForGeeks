class Solution:
    def largestPrimeFactor (self, N):
        num = 2
        while ((num*num) <= N):
            if N%num == 0:
                N=N//num
            else:
                num+=1
        return int(N)
    
# https://practice.geeksforgeeks.org/problems/largest-prime-factor2601/1