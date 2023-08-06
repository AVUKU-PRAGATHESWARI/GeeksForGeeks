class Solution:

    def check_duck(self, N):
        string = str(N)
        if '0' in string:
            if string[0] != '0':
                return 1
        return 0
    
# https://practice.geeksforgeeks.org/problems/zero-number2158/1?page=2&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions