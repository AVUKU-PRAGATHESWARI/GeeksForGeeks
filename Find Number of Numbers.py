# Your task is to complete this function
# Function should return an integer
def num(arr, n, k):
    # Code here
    k=str(k)
    count=0
    for i in arr:
        s=str(i)
        count+=s.count(k)
    return  count


# https://practice.geeksforgeeks.org/problems/find-number-of-numbers/1?page=1&difficulty[]=-2&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions