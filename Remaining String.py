#User function Template for python3
class Solution:
	def printString(self, S, ch, count):
	    my_count = 0
	    r = "Empty string"
	    for i in range(len(S)):
	        if my_count == count:
	            r= S[i:]
	            break
	        if S[i]==ch:
	            my_count += 1
	        
        return r

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ch = input()[0]
		count = int(input())
		ob = Solution()	
		answer = ob.printString(s,ch,count)
		
		print(answer)


# } Driver Code Ends