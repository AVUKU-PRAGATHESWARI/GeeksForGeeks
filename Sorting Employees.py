class Solution:
    def sortRecords(self, a, n):
        # Your code goes here
        a.sort(key=lambda a:a[0])
        a.sort(key=lambda a:a[1])
# https://practice.geeksforgeeks.org/problems/sorting-employees5907/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions