#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// long long factorial(int k){
//     if (k<0) cout << "Error\n";
//     if (k == 0) return 1;
//     long long ans = 1;
//     for(int i = 2; i<= k; i++){
//         ans *= i;
//     }
//     return ans;
// }

long long combinHelper(int n, int k, vector<vector<long long> > & memo){
    
    if (memo[n][k] != -1) return memo[n][k];
    if (n==k || k==0) {
        memo[n][k] = 1;
        return 1;
    }
    memo[n-1][k-1]  = combinHelper(n-1,k-1,memo);
    memo[n-1][k]  = combinHelper(n-1, k,memo);
    return memo[n-1][k-1]+memo[n-1][k];
} 

long long combination(int n, int k){
    // from n select k
    if(n == k || n == 0 || k == 0 ) return 1;
    if( k == 1 || k == n-1) return n;
    vector<vector<long long> > memo( n+1, vector<long long> (k+1, -1));
    return combinHelper(n,k, memo);
}


int main(){
    int T = 0, N = 0;
    cin >> T;
    for(int t_idx =0; t_idx<T; t_idx++){
        cin >> N;

        vector<int> nums(N,0);
        for(int i =0; i<nums.size(); i++){
            cin >> nums[i];
        }
        vector<vector<long long> > memo( N+1, vector<long long> (N+1, -1));
        long long ans = 0;
        for(int tochoose = 2; tochoose <= nums.size(); tochoose++){
            for(int s_idx = 0; s_idx+tochoose-1 < nums.size(); s_idx++){
                for(int e_idx = s_idx + tochoose-1; e_idx <nums.size(); e_idx++){
                    // cout << "comb " <<(nums[e_idx] - nums[s_idx])*combination( e_idx-s_idx-1, tochoose-2) << endl;
                    // ans += (nums[e_idx] - nums[s_idx])*combination( e_idx-s_idx-1, tochoose-2);
                    ans += (nums[e_idx] - nums[s_idx])*combinHelper( e_idx-s_idx-1, tochoose-2, memo);
                }
            }
            ans = ans %( int(pow(10,9)) + 7);
            cout << "tochoose increase " << tochoose << endl;

        }
        ans = ans %( int(pow(10,9)) + 7);
        cout << "Case #" << (t_idx+1) << ": " << ans << "\n";
    }

}