
class Solution:
    def minValueToBalance(self,a,n):
        sum1=sum(a[:n//2])
        sum2=sum(a[n//2:])
        return max(sum1,sum2)-min(sum1,sum2)
# https://practice.geeksforgeeks.org/problems/balanced-array07200720/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions