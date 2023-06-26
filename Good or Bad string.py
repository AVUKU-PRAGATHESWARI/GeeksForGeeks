#User function Template for python3

class Solution:
    def isGoodorBad(self, S):
        vowels = 'aeiou'
        vowel_count = 0
        consonant_count = 0

        for char in S:

            if char == '?':
                vowel_count += 1
                consonant_count += 1

            elif char in vowels:
                vowel_count += 1
                consonant_count = 0

            else:
                consonant_count += 1
                vowel_count = 0

            if consonant_count == 4 or vowel_count == 6:
                return 0

        return 1

# https://practice.geeksforgeeks.org/problems/good-or-bad-string1417/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions