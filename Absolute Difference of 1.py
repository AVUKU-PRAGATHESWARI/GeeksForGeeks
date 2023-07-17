class Solution:
    def getDigitDiff1AndLessK(self, arr, n, k):
        result=[]
        for i in arr:
            if i>=k:
                continue
            new=str(i)
            for j in range(len(new)-1):
                diff=abs(int(new[j])-int(new[j+1]))
                if diff!=1:
                    break
                if(j==len(new)-2):
                    result.append(i)
        return result

# https://practice.geeksforgeeks.org/problems/absolute-difference-11156/1?page=1&sprint=d605a11cf50f9ac08ed8a0c81c6a0dee&sortBy=submissions