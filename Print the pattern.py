def printPat(n):
    #Code here
    for i in range(n,0,-1):
        for j in range(n,0,-1):
            for k in range(i):
                print(j,end=' ')
        print("$",end='')
        if i==1:
            print()
# https://practice.geeksforgeeks.org/problems/print-the-pattern-set-1/1