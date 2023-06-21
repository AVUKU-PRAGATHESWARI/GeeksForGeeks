#User function Template for python3

class Solution:
    def MaxNumber(self, arr, n):
        maximum=''
        arr.sort()
        for i in arr[::-1]:
            maximum+=str(i)
        return int(maximum)
    
# https://practice.geeksforgeeks.org/problems/form-largest-number-from-digits5430/1?page=2&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions