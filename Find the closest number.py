#User function Template for python3

class Solution:
    def findClosest(self, arr, n, target):
        closest=arr[0]
        diff=abs(arr[0]-target)
        for i in arr:
            if diff > abs(i-target):
                closest = i
                diff = abs(i-target)
            elif diff == abs(i-target) and closest<i:
                closest = i
        return closest
    

# https://practice.geeksforgeeks.org/problems/find-the-closest-number5513/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions