class Solution:
    def countChars(self,s):
        result=[]
        s=s.split(" ")
        for i in s:
            result.append(len(i))
        return result
    
# https://practice.geeksforgeeks.org/problems/count-the-characters-in-each-word-in-a-given-sentence3451/1?page=3&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions