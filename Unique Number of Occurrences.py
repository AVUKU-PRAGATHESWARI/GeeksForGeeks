
from typing import List


class Solution:
    def isFrequencyUnique(self, n : int, arr : List[int]) -> bool:
        result=[]
        setofarr=list(set(arr))
        for i in setofarr:
            count=arr.count(i)
            if count in result:
                return False
            else:
                result.append(count)
        return True
# https://practice.geeksforgeeks.org/problems/unique-frequencies-of-not/1