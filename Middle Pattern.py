def printPattern(str):
    s=''
    length=len(str)
    for i in range(length//2,length):
        s=s+str[i]
        print(s,end="$ ")
    for j in range(0,length//2):
        s=s+str[j]
        print(s,end="$ ")
    print()

# https://practice.geeksforgeeks.org/problems/middle-pattern/0