#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        i=0
        new=''
        if len(S)<2:
            return S
        while i<len(S)-1:
            char=S[i]
            new+=char
            while S[i]==char and i<len(S)-1:
                i+=1
        if new[-1]!=S[-1]:
            new+=S[-1]
        return new
#https://practice.geeksforgeeks.org/problems/consecutive-elements2306/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions  