#User fuNctioN Template for pythoN3

class Solution:
    def isPerfectNumber(self, N):
        s=0
        if N==1:
            return 0
        else:
            for i in range(2,int(N**0.5)+1):
                if N%i==0:
                    s+=i
                    s+=N//i
                  
            if s+1==N:
                return 1
            else:
                return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.isPerfectNumber(N))
# } Driver Code Ends