#User function Template for python3

class Solution:
    def MaximumIntegerValue(self,S):
        result = int(S[0])
        for i in range(1,len(S)):
            result = max(result*int(S[i]) , result+int(S[i]))
        return result
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        
        ob=Solution()
        print(ob.MaximumIntegerValue(S))
# } Driver Code Ends