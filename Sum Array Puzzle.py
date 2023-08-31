#User function Template for python3

# arr is the array
# n is the number of element in array
def SumArray(arr,n):
    result = []
    sum_of_arr=0
    for i in arr:
        sum_of_arr += int(i)
    for i in range(n):
         arr[i]=(sum_of_arr-int(arr[i]))
    return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():
    t = int(input())
    
    while(t >= 1):
        n = int(input())
        arr = input().split();
        SumArray(arr,n)
        print(*arr)
        t -= 1
        
if __name__ == '__main__':
    main()
# } Driver Code Ends

# https://practice.geeksforgeeks.org/problems/sum-array-puzzle/1?page=1&difficulty[]=-1&status[]=unsolved&category[]=Arrays&sortBy=submissions
