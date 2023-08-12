class Solution:
    def nthFibonacci(self, n : int) -> int:
        mod = 1000000007
        if n<2:
            return n
        first = 0
        second = 1
        for i in range(n-1):
            next_one = (first%mod)+(second%mod)
            first = second
            second = next_one
        return next_one % mod 
    
# https://practice.geeksforgeeks.org/problems/nth-fibonacci-number1335/1