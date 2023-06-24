class Solution:
    def alternateSort(self,arr, N):
        new=[]
        arr.sort()
        for i in range(len(arr)//2):
            new.append(arr[-(i+1)])
            new.append(arr[i])
        if len(arr)%2==1:
            new.append(arr[len(arr)//2])
        arr.clear()
        arr.extend(new)
        return arr
# https://practice.geeksforgeeks.org/problems/alternative-sorting1311/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions