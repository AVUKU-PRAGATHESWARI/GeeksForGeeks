class Solution:
    def leftRotate(self, arr, k, n):
        r=k%n
        new=arr[r:]+arr[:r]
        arr.clear()
        for i in new:
            arr.append(i)
        return arr
    
    
# https://practice.geeksforgeeks.org/problems/quick-left-rotation3806/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions