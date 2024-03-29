//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution {
  public:
    int countX(int L, int R, int X) {
        
        int mod=0;
        int count=0;
        
        for(int i=L+1;i<R;i++)
        {
            int store=i;
            while(store>0)
            {
                mod=store%10;
                
                if(mod==X)
               {
                   count++;
                  
               }
               store=store/10;
            }
            
        }
        
        return count;
        
    }
};




//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int L, R, X;
        cin >> L >> R >> X;
        Solution ob;
        int ans = ob.countX(L, R, X);
        cout << ans << "\n";
    }
}

// } Driver Code Ends