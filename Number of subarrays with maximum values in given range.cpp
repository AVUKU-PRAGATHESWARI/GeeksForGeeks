//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends


class Solution{
    public:
    long count(int nums[],int k,int n){
        long long  ans=0,ind=-1;
        for(int i=0;i<n;i++){
            if(nums[i]>k) ind=i;
            ans+=(ind+1);
        }
        return ans;
     }
    long countSubarrays(int arr[], int n, int le, int ri)
    {
        long ans=count(arr,le-1,n)-count(arr,ri,n);
        return ans;
    }
};

//{ Driver Code Starts.
// driver program
int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        
        int n ,l,r;
        cin >> n>>l>>r;
        int a[n];
        for(int i=0;i<n;i++)
        cin >> a[i];
        Solution ob;
    	cout << ob.countSubarrays(a, n, l, r)<<endl;
    }
	return 0;
}

// } Driver Code Ends