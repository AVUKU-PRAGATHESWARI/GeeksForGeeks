#User function Template for python3

def isSubset( a1, a2, n, m):
    for i in a2:
        if i not in a1:
            return "No"
        else:
            a1.remove(i)
    return "Yes"
# https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1?page=1&status[]=unsolved&curated[]=2&sortBy=submissions