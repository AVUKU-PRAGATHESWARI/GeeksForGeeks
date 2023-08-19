
class Solution:
    def getCount(self,arr, n, num1, num2): 
        #Comlete the function
        first = arr.index(num1)
        for i in range(len(arr)-1,-1,-1):
            if arr[i]==num2:
                last = i 
                break
        if first==last:
            return 0
        return last-first-1
# https://practice.geeksforgeeks.org/problems/count-number-of-elements-between-two-given-elements-in-array4044/1?page=2&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions
