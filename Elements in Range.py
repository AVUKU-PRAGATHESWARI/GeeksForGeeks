class Solution:
    def check_elements(self, arr, n, A, B):
        # Your code goes here
        for i in range(A,B+1):
            if i not in arr:
                return False
        return True
# https://practice.geeksforgeeks.org/problems/elements-in-the-range2834/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions