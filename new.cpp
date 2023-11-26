#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // Recursive function to generate the pattern
    void generatePattern(vector<int> &res, int N, int current) {
        // Base case: If the current element is at or beyond N, return
        if (current >= N)
            return;

        // Add the current element to the result vector
        res.push_back(current);

        // Recursively call the function with the next element
        generatePattern(res, N, current + 5);
    }

    vector<int> pattern(int N) {
        // Initialize the result vector with the first element
        vector<int> res = {N};

        // Start generating the pattern recursively
        generatePattern(res, N, N - 4);

        return res;
    }
};

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;

        Solution ob;
        vector<int> ans = ob.pattern(N);

        // Print the generated pattern
        for (int u : ans)
            cout << u << " ";
        cout << "\n";
    }
    return 0;
}
