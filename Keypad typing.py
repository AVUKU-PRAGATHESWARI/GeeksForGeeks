#User function Template for python3


#Function to find matching decimal representation of a string as on the keypad.
def printNumber(s,n):
    result=''
    keypad = { 
        'a':2,
        'b':2,
        'c':2,
        'd':3,
        'e':3,
        'f':3,
        'g':4,
        'h':4,
        'i':4,
        'j':5,
        'k':5,
        'l':5,
        'm':6,
        'n':6,
        'o':6,
        'p':7,
        'q':7,
        'r':7,
        's':7,
        't':8,
        'u':8,
        'v':8,
        'w':9,
        'x':9,
        'y':9,
        'z':9,
    }
    for i in s:
        result+=str(keypad[i])
    return result
                
    #CODE HERE
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        
        s=input()
        n=len(s)
        print(printNumber(s,n))
# } Driver Code Ends