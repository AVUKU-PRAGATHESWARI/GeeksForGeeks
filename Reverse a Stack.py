from typing import List

class Solution:
    def reverse(self,St): 
        i=0
        j=len(St)-1
        while(i<j):
            St[i],St[j]=St[j],St[i]
            i+=1
            j-=1
        return St

# https://practice.geeksforgeeks.org/problems/reverse-a-stack/1