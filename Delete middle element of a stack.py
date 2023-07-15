class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        if sizeOfStack%2==1:
            del s[sizeOfStack//2]
        else:
            del s[sizeOfStack//2-1]
        return s

# https://practice.geeksforgeeks.org/problems/delete-middle-element-of-a-stack/1