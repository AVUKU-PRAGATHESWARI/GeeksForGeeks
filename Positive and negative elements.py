#User function Template for python3



class Solution:
    def arranged(self,a,n):
        pos=[]
        neg=[]
        p=[]
        for i in a:
            if i<0:
                neg.append(i)
            else:
                pos.append(i)
        while pos or neg:

            if len(pos):

                p.append(pos.pop(0))

            if len(neg):

                p.append(neg.pop(0))

        return p

# https://practice.geeksforgeeks.org/problems/positive-and-negative-elements4613/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions