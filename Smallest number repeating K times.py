#User function Template for python3


class Solution:
    def findDuplicate(self, arr, N, K):
        result=0
        arr.sort()
        for i in arr:
            if arr.count(i)==K:
                return i

# https://practice.geeksforgeeks.org/problems/smallest-number-repeating-k-times3239/1?page=3&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions