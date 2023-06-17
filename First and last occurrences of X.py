#User function Template for python3
class Solution: 
    def firstAndLast(self, arr, n, x): 
        # Code here
        result=[]
        if x not in arr:
            return [-1]
        for i in range(n):
            if arr[i]==x:
                result.append(i)
                break
        for j in range(n-1,-1,-1):
            if arr[j]==x:
                result.append(j)
                break
        return result

# https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x2041/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions