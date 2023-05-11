#User function Template for python3

class Solution:

    def convert(self, s):
        # code here
        upper=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        new=''
        for i in s:
            if i.isupper():
                new+=upper[(-(upper.index(i)+1))]
            else:
                new+=lower[(-(lower.index(i)+1))]
        return new
#https://practice.geeksforgeeks.org/problems/front-back-transformation1659/1?page=1&difficulty[]=-2&status[]=unsolved&category[]=Strings&sortBy=submissions