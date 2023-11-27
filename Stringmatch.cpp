//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
	public:
		string FirstNonRepeating(string A){
		    // Code here
		    map<char,int>mp;
		    queue<char>qt;
		    string res;
		    for(int i=0;i<A.size();i++){
		        qt.push(A[i]);
		        mp[A[i]]++;
		        while(!qt.empty()){
		            if(mp[qt.front()]>1){
		                qt.pop();
		            }else{
		                res+=qt.front();
		                break;
		            }
		        }
		        if(qt.empty()){
		            res+='#';
		        }
		    }
		    return res;
		
 // 
		}

};

//{ Driver Code Starts.
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		string A;
		cin >> A;
		Solution obj;
		string ans = obj.FirstNonRepeating(A);
		cout << ans << "\n";
	}
	return 0;
}
// } Driver Code Ends
