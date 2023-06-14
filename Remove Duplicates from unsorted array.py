#User function Template for python3

class Solution:
    def removeDuplicate(self, A, N):
        dup,ans = set(),[]
        for i in A:
            if i not in dup:
                dup.add(i)
                ans+=[i]
        return ans
# https://practice.geeksforgeeks.org/problems/remove-duplicates-from-unsorted-array4141/1?page=2&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions