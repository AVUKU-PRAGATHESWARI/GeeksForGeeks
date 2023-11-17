class Solution:
    def ExtractNumber(self, S):
        words = S.split()
        res = -1
        for i in words:
            if i[0].isdigit() and '9' not in i:
                res = max(res, int(i))
        return res


#{ 
 # Driver Code Starts

t=int(input())
for _ in range(t):
    S=input()
    ob=Solution()
    ans=ob.ExtractNumber(S)
    print(ans)   
# } Driver Code Ends