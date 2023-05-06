def game_with_number (arr,  n) : 
    new=[0]*n
    for i in range(n-1):
        new[i]=(arr[i]^arr[i+1])
    new[n-1]=arr[n-1]
    return new

