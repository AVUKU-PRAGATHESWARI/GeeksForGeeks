class Solution:
    def PartyType(self, a, n):
        b=list(set(a))
        if len(a)==len(b):
            return "GIRLS"
        else:
            return "BOYS"
# https://practice.geeksforgeeks.org/problems/professor-and-parties2000/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions