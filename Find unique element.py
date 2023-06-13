class Solution:
    def findUnique(self, a, n, k): 
        d1={}
        for i in a:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for i,j in d1.items():
            if j%k!=0:
                return i
# https://practice.geeksforgeeks.org/problems/find-unique-element2632/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions