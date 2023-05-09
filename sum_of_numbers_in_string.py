class Solution:
    
    #Function to calculate sum of all numbers present in a string.
    def findSum(self,s):
        #code here
        sum=0
        i=0
        
        while (i<=len(s)-1):
            count=0
            if (s[i].isnumeric()==True):
                j=i
                while(j!=len(s)-1 and s[j+1].isnumeric()==True):
                    j+=1
                    count+=1
                num=s[i:j+1]
                sum+=int(num)
            i+=count+1
        return sum
                
#https://practice.geeksforgeeks.org/problems/sum-of-numbers-in-string-1587115621/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions