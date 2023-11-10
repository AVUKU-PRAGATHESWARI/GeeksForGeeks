#User function Template for python3

class Solution:
    def sortSecond(self,val):
        return val[1] 
    def secFrequent(self, arr, n):
        # code here
        d={}
        for x in arr:
            if x not in d:
                d[x]=0
            d[x]+=1
        dic=list(d.items())
        dic.sort(key=self.sortSecond,reverse=True)
        return(dic[1][0])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr,n)
        print(ans)
# } Driver Code Ends

# https://practice.geeksforgeeks.org/problems/second-most-repeated-string-in-a-sequence0534/1?page=1&difficulty[]=0&status[]=unsolved&category[]=Strings&sortBy=submissions