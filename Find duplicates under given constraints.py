#User function Template for python3

def findDuplicate(A):
    # Your code goes here
    for i in list(set(A)):
        if A.count(i)>1:
            return i
# https://practice.geeksforgeeks.org/problems/find-duplicates-under-given-constraints0856/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions