#Your task is to complete this function
#Function should return complete string
def encode(arr):
    re = ''
    l = len(arr)
    i = 0
    while(i<l):
        char = arr[i]
        count = 1
        i += 1
        while i<l and arr[i]==char:
            count += 1
            i += 1
        re += (char + str(count))
    return re


#{ 
 # Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends