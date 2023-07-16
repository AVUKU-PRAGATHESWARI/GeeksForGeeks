
class Solution:
    
    def rearrange(self,arr, n):
        positive=[]
        negative=[]
        result=[]
        
        diff=abs(len(positive)-len(negative))
        for i in arr:
            if i>=0:
                positive.append(i)
            else:
                negative.append(i)
        length=min(len(positive),len(negative))
        arr.clear()
        for i in range(length):
            arr.append(positive[i])
            arr.append(negative[i])
        if len(positive)>len(negative):
            for i in range(length,len(positive)):
                arr.append(positive[i])
        elif len(negative)>len(positive):
            for i in range(length,len(negative)):
                arr.append(negative[i])
        return arr
    
#  https://practice.geeksforgeeks.org/problems/array-of-alternate-ve-and-ve-nos1401/1?page=1&sprint=d605a11cf50f9ac08ed8a0c81c6a0dee&sortBy=submissions   
