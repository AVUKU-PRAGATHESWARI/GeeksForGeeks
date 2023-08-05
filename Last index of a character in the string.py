class Solution:
    def LastIndex(self, s, p):
        last=-1
        for i in range(len(s)):
            if s[i]==p:
                last=i
        return last
    

# https://practice.geeksforgeeks.org/problems/last-index-of-a-character-in-the-string4516/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions