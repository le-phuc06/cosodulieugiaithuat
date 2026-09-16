#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> greedyCoinChange(vector<int> coins, int S) {
    sort(coins.rbegin(), coins.rend());
    vector<int> res;
    for (int c : coins) {
        while (S >= c) {
            res.push_back(c);
            S -= c;
        }
    }
    return res;
}

vector<int> dpCoinChange(const vector<int>& coins, int S) {
    vector<int> dp(S + 1, 1e9);
    vector<int> used(S + 1, -1);
    dp[0] = 0;
    for (int i = 1; i <= S; ++i) {
        for (int c : coins) {
            if (i >= c && dp[i - c] + 1 < dp[i]) {
                dp[i] = dp[i - c] + 1;
                used[i] = c;
            }
        }
    }
    vector<int> res;
    int curr = S;
    while (curr > 0) {
        res.push_back(used[curr]);
        curr -= used[curr];
    }
    return res;
}

int main() {
    struct TestCase { vector<int> coins; int S; };
    vector<TestCase> tests = {
        {{1, 4, 6, 9}, 12},
        {{1, 5, 10, 20, 50}, 85},
        {{1, 3, 7, 12}, 20},
        {{1, 2, 5, 10}, 38},
        {{1, 6, 10}, 12},
        {{1, 4, 5, 15, 20}, 23}
    };

    for (int i = 0; i < tests.size(); ++i) {
        auto g = greedyCoinChange(tests[i].coins, tests[i].S);
        auto d = dpCoinChange(tests[i].coins, tests[i].S);
        cout << "Bo " << i + 1 << ": Tham lam = " << g.size() 
             << " to | DP = " << d.size() << " to -> " 
             << (g.size() == d.size() ? "Dung" : "Sai") << endl;
    }
    return 0;
}