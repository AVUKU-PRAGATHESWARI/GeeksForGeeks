#User function Template for python3



class Solution:
    def rearrangeArray(self, arr, n):
        arr.sort()
        new=[]
        length=len(arr)
        for i in range(length//2):
            new.append(arr[i])
            new.append(arr[-(i+1)])
        if len(arr)%2==0:
            pass
        else:
            new.append(arr[length//2])
        arr.clear()
        arr.extend(new)
        return arr
    
# https://practice.geeksforgeeks.org/problems/rearrange-the-array5802/1?page=2&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions