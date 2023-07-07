
class Solution:
    def extractMaximum(self,S): 
        list=[]
        i=0
        while(i<len(S)):
            start=i
            if S[i].isdigit():
                while((i<len(S)) and S[i].isdigit()):
                    i=i+1
                end=i
                num=int(S[start:end])
                list.append(num)
            else:
                i=i+1
        if len(list)==0:
            return -1
        return(max(list))

# https://practice.geeksforgeeks.org/problems/extract-maximum2943/1?page=1&difficulty[]=-1&status[]=unsolved&company[]=Amazon&category[]=Strings&sortBy=submissions