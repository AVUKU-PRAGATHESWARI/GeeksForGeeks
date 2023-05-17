#User function Template for python3

class Solution:
    def printDiamond(self, N):
        # Code here
        for i in range(1,N+1):
            left=(N-i)*" "
            stars="* "*i
            print(left+stars)
        for j in range(N,0,-1):
            left=(N-j)*" "
            stars="* "*j
            print(left+stars)
# https://practice.geeksforgeeks.org/problems/pattern/1?page=1&category[]=pattern-printing&sortBy=submissions