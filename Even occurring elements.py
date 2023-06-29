#User function Template for python3

class Solution:
    def repeatingEven(self, arr, n):
        result=[]
        new=list(set(arr))
        for i in new:
            if arr.count(i)%2==0:
                result.append(i)
        if len(result)==0:
            return [-1]
        result.sort()
        return result

# https://practice.geeksforgeeks.org/problems/even-occurring-elements4332/1?page=4&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions