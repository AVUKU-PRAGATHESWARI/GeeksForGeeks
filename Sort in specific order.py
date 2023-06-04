class Solution:
    def sortIt(self, arr, n):
        odd = []
        even = []
        for i in arr: 
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        even.sort()
        odd = sorted(odd,reverse=True)
        arr.clear()
        arr.extend(odd)
        arr.extend(even)
        return arr

class Solution:
    def sortIt(self, arr, n):
        odd = []
        even = []
        for i in arr: 
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        even.sort()
        odd = sorted(odd,reverse=True)
        arr.clear()
        arr.extend(odd)
        arr.extend(even)
        return arr
# https://practice.geeksforgeeks.org/problems/sort-in-specific-order2422/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions