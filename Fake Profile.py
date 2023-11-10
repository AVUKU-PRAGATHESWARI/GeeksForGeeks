#User function Template for python3

class Solution:

    def solve(self, a):
        record = []
        vowels = 'aeiou'
        for i in a:
            if i not in record and i not in vowels:
                record.append(i)
        return "HE!" if len(record)%2==1 else "SHE!"

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        a = input()

        solObj = Solution()

        print(solObj.solve(a))
# } Driver Code Ends