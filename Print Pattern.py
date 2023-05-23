#User function Template for python3

class Solution:
    def pattern(self, N):
        # code here
        test=N
        result=[N]
        while(test>0):
            test-=5 
            result.append(test)
        while(test!=N):
            test+=5 
            result.append(test)
        return result
# https://practice.geeksforgeeks.org/problems/print-pattern3549/1?page=1&category[]=pattern-printing&sortBy=submissions    
