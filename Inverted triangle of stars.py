class Solution:
    def invIsoTriangle(self, N):
        # code here 
        start=2*N-1 
        result=[]
        for i in range(N):
            space=" "*i
            stars="*"*start
            result.append(space+stars)
            start-=2
        return result
    
# https://practice.geeksforgeeks.org/problems/inverted-triangle-of-stars0110/1?page=1&status[]=unsolved&category[]=pattern-printing&sortBy=submissions