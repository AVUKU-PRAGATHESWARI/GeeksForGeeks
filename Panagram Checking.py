class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        s=s.lower()
        list1 = list(set(s))
        if len(list1)<26:
            return 0
        new = ''
        for i in s:
            if i.isalpha() and i not in new:
                new+=i
        if len(new)!=26:
            return 0
        return 1

# https://practice.geeksforgeeks.org/problems/pangram-checking-1587115620/1?page=1&difficulty[]=0&status[]=unsolved&category[]=Strings&sortBy=submissions