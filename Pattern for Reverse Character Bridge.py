class Solution:
    def revCharBridge(self, N):
        l=[]# code here 
        co=0
        c='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for i in range(N,0,-1):
            start=c[:i]
            if i==N-1:
                co=1
            else:
                co+=2
            center=" "*co
            end=start[::-1]
            if i==N:
                l.append(start+end[1:])
            else:
                l.append(start+center+end)
        return l
    
# https://practice.geeksforgeeks.org/problems/pattern-for-reverse-character-bridge5738/1?page=1&category[]=pattern-printing&sortBy=submissions