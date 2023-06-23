#User function Template for python3

class Solution:
    def RedOrGreen(self,N,S):
        red=S.count('R')
        green=S.count('G')
        return min(red,green)

# https://practice.geeksforgeeks.org/problems/red-or-green5711/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions