#User function Template for python3

class Solution:
    def firstIndex(self, arr, n):
    # Your code goes here
        count=arr.count(0)
        if count==len(arr):
            return -1
        return count
    
# https://practice.geeksforgeeks.org/problems/index-of-first-1-in-a-sorted-array-of-0s-and-1s4048/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions