class Solution:
    def merge(self, S1, S2):
        S3=''
        length=min(len(S1),len(S2))
        for i in range(length):
            S3+=S1[i]+S2[i]
        if len(S1)>length:
            S3+=S1[length:]
        else:
            S3+=S2[length:]
        return S3
# https://practice.geeksforgeeks.org/problems/merge-two-strings2736/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions