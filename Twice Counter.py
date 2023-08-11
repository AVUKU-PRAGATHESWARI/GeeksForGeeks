class Solution:
    def countWords(self,List, n):
        result = 0
        list1 = list(set(List))
        for i in list1:
            if List.count(i)==2:
                result += 1
        return  result

# https://practice.geeksforgeeks.org/problems/twice-counter4236/1?page=1&difficulty[]=0&status[]=unsolved&category[]=Strings&sortBy=submissions