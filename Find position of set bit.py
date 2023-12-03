#User function Template for python3

class Solution:
    def findPosition(self, N):
        if N==0:
            return -1
        if  N==1:
            return 1
        count = 1
        while(N!=1):
            if N%2!=0:
                return -1
            N = N//2
            count += 1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.findPosition(N))
# } Driver Code Ends