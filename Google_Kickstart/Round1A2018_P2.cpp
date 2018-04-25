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
  long long total = 0;
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


/* reference:
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define mp make_pair
#define pb push_back
#define rep(i, n) for (int i = 0; i < (n); i++)
#define re return
#define fi first
#define se second
#define sz(x) ((int)(x).size())
#define all(x) (x).begin(), (x).end()
#define sqr(x) ((x) * (x))
#define sqrt(x) sqrt(abs(x))
#define y0 y3487465
#define y1 y8687969
#define fill(x, y) memset(x, y, sizeof(x))
#define prev PREV

typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef double D;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<string> vs;
typedef vector<vi> vvi;

template <class T> T abs(T x) { re x > 0 ? x : -x; }

int n;
int m;
int r, b, c;
ll cm[1010];
ll cs[1010];
ll cp[1010];

ll can(ll h) {
  vector<ll> now;
  for (int i = 0; i < c; i++)
    if (cp[i] + cs[i] <= h)
      now.pb(min((h - cp[i]) / cs[i], cm[i]));
  sort(all(now));
  ll cur = 0;
  int tr = r;
  for (int i = 0; tr > 0 && i < sz(now); i++) {
    cur += now[sz(now) - i - 1];
    tr--;
  }
  re cur;
}

int main() {
  int tt;
  cin >> tt;
  for (int it = 1; it <= tt; it++) {
    cin >> r >> b >> c;
    for (int i = 0; i < c; i++)
      cin >> cm[i] >> cs[i] >> cp[i];
    ll l = 0, rt = 4e18;
    while (rt > l) {
      ll s = (l + rt) / 2;
      if (can(s) >= b)
        rt = s;
      else
        l = s + 1;
    }
    cout.precision(20);
    cout << "Case #" << it << ": " << rt;
    cout << endl;
    fprintf(stderr, "%d / %d = %.2f | %.2f\n", it, tt,
            (double)clock() / CLOCKS_PER_SEC,
            ((double)clock() / it * tt) / CLOCKS_PER_SEC);
  }
  return 0;
}
*/
