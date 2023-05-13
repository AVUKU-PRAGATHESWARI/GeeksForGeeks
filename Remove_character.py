
class Solution:
    def removeChars (ob, string1, string2):
        new=''
        for i in string1:
            if i not in string2:
                new+=i
        return new
    
# https://practice.geeksforgeeks.org/problems/remove-character3815/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions