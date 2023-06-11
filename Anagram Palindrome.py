#User function Template for python3

class Solution:

    def isPossible(self, S):
        length=len(S)
        count=0
        if length%2==0:
            for i in list(set(S)):
                if (S.count(i)%2!=0):
                    return 0
        else:
            for i in list(set(S)):
                if S.count(i)%2==0:
                    pass
                else:
                    count+=1
                    if count>1:
                        return 0
        return 1

# https://practice.geeksforgeeks.org/problems/anagram-palindrome4720/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions