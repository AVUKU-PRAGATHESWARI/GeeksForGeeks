class Solution:
    def totalCount(self, arr, n, k):
        count=0
        for i in arr:
            if(i%k==0):
                count+=(i//k)
            else:
                count+=(i//k+1)
        return count
# https://practice.geeksforgeeks.org/problems/total-count2415/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions