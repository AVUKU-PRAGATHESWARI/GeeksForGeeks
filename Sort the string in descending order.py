#User function Template for python3
class Solution:
    def ReverseSort(self, str): 
        rev = list(str)
        rev.sort(reverse=True)
        str = "".join(rev)
        return str


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        print(ob.ReverseSort(s))
# } Driver Code Ends