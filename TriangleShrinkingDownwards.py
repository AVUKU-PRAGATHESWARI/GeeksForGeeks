#User function Template for python3

class Solution:
    def triDownwards(self, S):
        res=[]
        for i in range(len(S)-1):
            dot="."*i
            res.append(dot+S[i:]+"\n")
        dot="."*(len(S)-1)
        res.append(dot+S[-1])
        return res
"""
https://practice.geeksforgeeks.org/problems/triangle-shrinking-downwards0459/1?page=1&difficulty[]=-2&status[]=unsolved&category[]=Strings&sortBy=submissions
"""