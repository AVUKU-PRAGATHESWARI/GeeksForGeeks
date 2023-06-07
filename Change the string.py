#User function Template for python3


class Solution:
    def modify(self, s):
        # code here
        upper=s[0].isupper()
        lower=s[0].islower()
        if upper:
            s=s.upper()
        else:
            s=s.lower()
        return s
# https://practice.geeksforgeeks.org/problems/change-the-string3541/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions