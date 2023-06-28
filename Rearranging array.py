#User function Template for python3

class Solution:    
    def Rearrange(self, a, n, answer):
        a.sort()
        start=0
        end=n-1
        for i in range(n):
            if i%2==0:
                answer[i]=a[start]
                start+=1
            else:
                answer[i]=a[end]
                end-=1
        return answer
    
# https://practice.geeksforgeeks.org/problems/rearranging-array1648/1?page=2&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions