def getFloorAndCeil(arr, n, x):
    arr = list(set(arr))
    arr.sort()
    floor = -1
    ceil = -1
    if_found = 1
    for i in arr:
        if if_found:
            if i<=x:
                floor = i
            if i>=x:
                ceil=i
                if_found = 0
    return floor,ceil

# https://practice.geeksforgeeks.org/problems/ceil-the-floor2802/1?page=1&difficulty[]=-2&status[]=unsolved&category[]=Arrays&sortBy=submissions