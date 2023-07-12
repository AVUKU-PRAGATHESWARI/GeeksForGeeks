# https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/1

class Solution:
    def missingNumber(self,array,n):
        sumofarr = (n*(n+1))//2
        sumofactual = sum(array)
        return sumofarr-sumofactual