#User function Template for python3
class Solution:

	def segregateEvenOdd(self,arr, n):
		# code here
        even=[]
        odd=[]
        for i in arr:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        even.sort()
        odd.sort()
        arr.clear()
        for i in even:
            arr.append(i)
        for j in odd:
            arr.append(j)
        return arr
# https://practice.geeksforgeeks.org/problems/segregate-even-and-odd-numbers4629/1?page=1&difficulty[]=-2&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions