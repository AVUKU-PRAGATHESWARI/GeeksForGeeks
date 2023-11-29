#User function Template for python3

def findElement(arr, n):
    left_max = [0] * n
    right_min = [0] * n

    left_max[0] = float('-inf')
    right_min[n - 1] = float('inf')

    # Precompute maximum values in the left subarray
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], arr[i - 1])

    # Precompute minimum values in the right subarray
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], arr[i + 1])

    # Check for the element that satisfies the condition
    for i in range(1, n - 1):
        if arr[i] >= left_max[i] and arr[i] <= right_min[i]:
            return arr[i]

    return -1

        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(findElement(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends