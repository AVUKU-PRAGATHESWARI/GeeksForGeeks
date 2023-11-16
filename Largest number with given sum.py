class Solution:
    # Function to return the largest possible number of n digits
    # with the sum equal to the given sum.
    def largestNum(self, n, s):
        # Check if it is possible to form the number with the given sum.
        if s > 9 * n:
            return -1

        # Initialize an array with all 9s.
        result = [0] * n

        # Iterate through the array and adjust values to get the desired sum.
        for i in range(n):
            if s >= 9:
                result[i] = 9
                s -= 9
            else:
                result[i] = s
                break

        # Convert the list to a string and then to an integer.
        result_str = ''.join(map(str, result))
        return result_str
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,s = map(int,input().strip().split())
        ob = Solution()
        print(ob.largestNum(n,s))
# } Driver Code Ends