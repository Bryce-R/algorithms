#include <algorithm>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <utility>
#include <vector>
using namespace std;

typedef vector<vector<int>> vvi;
typedef vector<int> vi;
// void vprint(vector<int> &vals) {
//   for (auto k : vals) {
//     cout << k << " ";
//   }
//   cout << " \n";
// }

// void vvprint(vvi &vs) {
//   for (auto v : vs) {
//     vprint(v);
//   }
// }
//   sort(cashier.begin(), cashier.end(),
//        [](const vector<int> &a, const vector<int> &b) {
//          if (a[3] == b[3])
//            return a[1] < b[1];
//          else
//            return a[3] < b[3];
//        });

bool process(long long t, int r, int b, vector<vector<long long>> &cashier) {
  long long max_b = 0;
  vector<long long> bits;
  for (int i = 0; i < cashier.size(); i++) {
    if (t >= cashier[i][2] + cashier[i][1]) {
      max_b = (t - cashier[i][2]) / cashier[i][1];
      max_b = (max_b > cashier[i][0]) ? cashier[i][0] : max_b;
      bits.push_back(max_b);
    }
  }
  sort(bits.begin(), bits.end());
  int total = 0;
  for (auto it = bits.rbegin(); it != bits.rend() && r > 0; it++) {
    total += (*it);
    r--;
  }
  return (total >= b);
}

long long solve() {
  int r = 0, c = 0, b = 0;
  cin >> r >> b >> c;
  vector<vector<long long>> cashier;

  for (int i = 0; i < c; i++) {
    vector<long long> temp;
    long long m = 0, s = 0, p = 0;
    cin >> m >> s >> p;
    temp = {m, s, p};
    cashier.push_back(temp);
  }

  long long lt = 0, rt = 4e18;
  while (rt - lt > 1) {
    long long m = lt + (rt - lt) / 2;
    if (process(m, r, b, cashier)) {
      rt = m;
    } else {
      lt = m;
    }
  }
  return rt;
}

int main() {
  int t = 0;
  cin >> t;
  for (int i = 0; i < t; i++) {
    long long res = solve();

    cout << "Case #" << (i + 1) << ": " << res << "\n";
  }
}
