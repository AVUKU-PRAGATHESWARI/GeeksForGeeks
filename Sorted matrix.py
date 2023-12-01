#User function Template for python3

class Solution:
    def sortedMatrix(self,N,Mat):
        new = []
        k = 0
        for i in Mat:
            new.extend(i)
        new.sort()
        for i in range(len(Mat)):
            for j in range(len(Mat[i])):
                Mat[i][j] = new[k]
                k += 1
        return Mat


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        v=[]
        for i in range(N):
            a=list(map(int,input().strip().split()))
            v.append(a)
        ob=Solution()
        ans=ob.sortedMatrix(N,v)
        for i in range(N):
            for j in range(N):
                print(ans[i][j],end=" ")
            print()
# } Driver Code Ends