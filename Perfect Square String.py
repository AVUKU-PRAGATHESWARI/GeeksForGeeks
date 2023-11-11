#User function Template for python3

class Solution:
    def isSquare(self, S): 
        order = 0
        for i in S:
            if i.isalpha():
                order += ord(i)
        if int(order**(0.5)) * int(order**(0.5)) == order:
            return 1
        else:
            return 0





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        print(ob.isSquare(S))
# } Driver Code Ends