class Solution:
	def pushZerosToEnd(self,arr, n):
	    # Initialize two pointers
        left = 0
        right = 0

    # Move non-zero elements to the left side of the array
        while right < len(arr):
            if arr[right] != 0:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
            right += 1

        return arr

# https://practice.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1?page=1&difficulty[]=-2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&category[]=Arrays&sortBy=submissions