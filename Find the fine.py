class Solution:
    def totalFine(self, n, date, car, fine):
        result = 0
        is_even = (date%2==0)
        odd=0
        even=0
        for i in range(len(car)):
            if car[i]%2!=0:
                odd+=fine[i]
            else:
                even+=fine[i]
        if is_even:
            return odd
        else:
            return even
# https://practice.geeksforgeeks.org/problems/find-the-fine4353/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions