

class Solution:

    # Program for zig-zag conversion of array

    def zigZag(self, arr, n):

        for i in (1,n,2):

            if arr[i] < arr[i-1]:

                arr[i],arr[i-1] = arr[i-1],arr[i]

            if i != n-1 and  arr[i] < arr[i+1] :

                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        return

