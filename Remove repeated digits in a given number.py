#User function Template for python3

class Solution:
    def modify(self, N):
        N = str(N)
        res = [N[0]]
        for i in N:
            if i != res[-1]:
                res += i
        return ''.join(res)
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        num = int(input())

        solObj = Solution()

        print(solObj.modify(num))
# } Driver Code Ends