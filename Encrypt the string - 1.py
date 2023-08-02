#User function Template for python3

class Solution:

    def encryptString(self, s):
        if len(s) < 2:
            return "1"+s[0]
        else:
            count=1
            S=""
            for i in range(1,len(s)):
                if s[i] == s[i-1]:
                    count+=1
                else:
                    S+=s[i-1]+str(count)
                    count=1
            S+=s[i]+str(count)
            return S[::-1]
        
# https://practice.geeksforgeeks.org/problems/encrypt-the-string-10337/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions