#User function Template for python3

class Solution:
    def countElements(self, arr, n):
        count=1
        maxs=arr[0]
        for i in range(1,n):
            if maxs<arr[i]:
                maxs=arr[i]
                count+=1
        return count

# https://practice.geeksforgeeks.org/problems/elements-before-which-no-element-is-bigger0602/1?page=3&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions