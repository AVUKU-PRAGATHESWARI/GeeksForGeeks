#User function Template for python3

class Solution:
    
    #Function to sort the binary array.
    def binSort(self, A, N): 
        lenof0=A.count(0)
        lenof1=A.count(1)
        A.clear()
        for i in range(lenof0):
            A.append(0)
        for j in range(lenof1):
            A.append(1)
        return A
    
# https://practice.geeksforgeeks.org/problems/binary-array-sorting-1587115620/1?page=1&difficulty[]=-2&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions