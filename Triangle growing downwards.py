#User function Template for python3

class Solution:

    def printTriangleDownwards(self, s):
        N=len(s)
        for i in range(1,N+1):
            dots="."*(N-i)
            s1=s[:i]
            print(dots+s1)


# https://practice.geeksforgeeks.org/problems/triangle-growing-downwards2344/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=pattern-printing&sortBy=submissions