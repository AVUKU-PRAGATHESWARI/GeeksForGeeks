#User function Template for python3

def maxlength(s):
    s = s.split("0")
    ans = 0
    for i in s:
        ans = max(ans, len(i))
    return ans
    
    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        s=input()
        print(maxlength(s))
# } Driver Code Ends