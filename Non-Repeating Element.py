
class Solution:
    def firstNonRepeating(self, arr, n): 
        d = {}
        for i in arr:
            d[i] = d.get(i,0)+1
        for i in arr:
            if d[i] == 1:
                return i
