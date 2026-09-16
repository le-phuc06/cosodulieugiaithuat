#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
    int n = 5, W = 11;
    vector<string> names = {"A", "B", "C", "D", "E"};
    vector<int> w = {0, 2, 3, 4, 5, 7};
    vector<int> v = {0, 3, 7, 9, 12, 16};

    vector<vector<int>> f(n + 1, vector<int>(W + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= W; j++) {
            if (w[i] > j) {
                f[i][j] = f[i - 1][j];
            } else {
                f[i][j] = max(f[i - 1][j], f[i - 1][j - w[i]] + v[i]);
            }
        }
    }

    cout << "Bang f[i][j]:\n";
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= W; j++) {
            cout << setw(3) << f[i][j] << " ";
        }
        cout << "\n";
    }

    cout << "\nGia tri lon nhat: " << f[n][W] << "\n";

    int curr_w = W;
    vector<string> selected;
    for (int i = n; i >= 1; i--) {
        if (f[i][curr_w] != f[i - 1][curr_w]) {
            selected.push_back(names[i - 1]);
            curr_w -= w[i];
        }
    }

    reverse(selected.begin(), selected.end());
    cout << "Tap do vat duoc chon: ";
    for (size_t k = 0; k < selected.size(); k++) {
        cout << selected[k] << (k == selected.size() - 1 ? "" : ", ");
    }
    cout << "\n";

    return 0;
}