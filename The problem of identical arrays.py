#User function Template for python3

def check (arr,  brr, n) : 
    #Complete the function
    for i in arr:
        if i not in brr:
            return 0
        else:
            brr.remove(i)
    return 1

# https://practice.geeksforgeeks.org/problems/the-problem-of-identical-arrays3229/1?page=2&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions