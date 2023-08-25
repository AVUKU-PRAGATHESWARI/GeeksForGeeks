def game_with_number (arr,  n) : 
    #Complete the function
    result = []
    for i in range(len(arr)-1):
        result.append(arr[i] | arr[i+1])
    result.append(arr[-1])
    return result
# https://practice.geeksforgeeks.org/problems/play-with-or5515/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions