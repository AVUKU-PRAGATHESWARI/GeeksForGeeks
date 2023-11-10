#User function Template for python3

class Solution:
    def clockSum(self, num1, num2):
        return (num1+num2)%12
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        num1, num2 = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.clockSum(num1, num2))

# } Driver Code Ends
# https://practice.geeksforgeeks.org/problems/12-hour-clock-addition1206/1?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions