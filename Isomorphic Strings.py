class Solution:
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,a,b):
        if len(a) != len(b):
            return False
        mapp = {}
        b_seen = []
        for i in range(len(a)):
            if a[i] not in mapp:
                if b[i] not in b_seen:
                    mapp[a[i]] = b[i]
                else:
                    return False
            else:
                if mapp[a[i]] == b[i]:
                    continue
                return False
            b_seen.append(b[i])
        return True
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends