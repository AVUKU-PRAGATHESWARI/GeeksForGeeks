class Solution:
    def removeConsonants(self, s):
        #complete the function here
        vowel=['a','e','i','o','u','A','E','I','O','U']
        new=''
        for i in s:
            if i in vowel:
                new+=i
        if new=='':
            return 'No Vowel'
        return new
    
# https://practice.geeksforgeeks.org/problems/c-program-to-remove-consonants-from-a-string1945/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions