class Solution:
    def missingNumber(self,arr,n):
        a=[]
        m=1
        for i in arr:
            if i>0:
                a.append(i)
        a=sorted(set(a))
        for i in range(1,len(a)+1):
            if i not in a:
                return i
            else:
                m+=1
        if m==len(a)+1:
                return m
        
# https://practice.geeksforgeeks.org/problems/smallest-positive-missing-number-1587115621/1