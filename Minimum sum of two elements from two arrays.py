
class Solution:
    def minSum(self,  a, b, n):
        c=sorted(a)
        d=sorted(b)
        if a.index(c[0])!=b.index(d[0]):
            return c[0]+d[0]
        else:
            return min((c[0]+d[1]),(c[1]+d[0]))
        
# https://practice.geeksforgeeks.org/problems/minimum-sum-of-two-elements-from-two-arrays0253/1?page=4&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions