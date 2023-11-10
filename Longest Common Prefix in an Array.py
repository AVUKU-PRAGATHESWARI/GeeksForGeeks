#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        if n==0:
            return ''
        if n==1:
            return arr[0]
        com_pre = ''
        arr.sort()
        min_len = min(len(arr[0]), len(arr[n-1]))
        index = 0
        while index<min_len and arr[0][index]==arr[n-1][index]:
            index += 1
        com_pre = arr[0][:index]
        if index == 0:
            return -1
        return com_pre

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends