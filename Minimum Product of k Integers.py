#User function Template for python3

class Solution:
    def minProduct(self, a, n, k):
        a.sort()
        product=1
        for i in range(k):
            product*=a[i]
        return product%(10**9+7)
# https://practice.geeksforgeeks.org/problems/minimum-product-of-k-integers2553/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions