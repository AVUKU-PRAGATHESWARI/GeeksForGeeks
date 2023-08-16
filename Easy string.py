
class Solution:

    def transform(self, S):
        result = ''
        i=0
        S=S.lower()
        while(i<len(S)):
            initial_str = S[i]
            count = 0 
            while(i<len(S) and S[i]==initial_str):
                count+=1
                i=i+1
            result+=str(count)
            result+=initial_str
        return result
# https://practice.geeksforgeeks.org/problems/easy-string2212/1?page=3&difficulty[]=0&status[]=unsolved&category[]=Strings&sortBy=submissions