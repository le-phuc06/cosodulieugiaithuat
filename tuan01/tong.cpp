#include <iostream>
using namespace std;

int main() {
    int n;
    if (!(cin >> n)) return 0;
    
    long long sum = 0;
    long long max_val = 0;
    
    for (int i = 0; i < n; ++i) {
        long long val;
        cin >> val;
        sum += val;
        if (i == 0 || val > max_val) {
            max_val = val;
        }
    }
    
    cout << sum << " " << max_val << "\n";
    return 0;
}