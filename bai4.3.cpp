#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <iomanip>
#include <algorithm>
using namespace std;

int main() {
    map<string, double> pi = {{"N", 0.6}, {"V", 0.4}};
    map<string, map<string, double>> A = {
        {"N", {{"N", 0.35}, {"V", 0.65}}},
        {"V", {{"N", 0.70}, {"V", 0.30}}}
    };
    map<string, map<string, double>> B = {
        {"N", {{"em", 0.35}, {"hoc", 0.10}, {"bai", 0.40}, {"toan", 0.30}}},
        {"V", {{"em", 0.05}, {"hoc", 0.45}, {"bai", 0.05}, {"toan", 0.02}}}
    };

    vector<string> words = {"em", "hoc", "bai", "toan"};
    vector<string> states = {"N", "V"};

    map<string, double> f[5];
    for (auto s : states) f[1][s] = pi[s] * B[s]["em"];

    for (int i = 2; i <= 4; ++i) {
        string w = words[i-1];
        for (auto s : states) {
            double max_p = -1;
            for (auto ps : states) {
                double p = f[i-1][ps] * A[ps][s] * B[s][w];
                if (p > max_p) max_p = p;
            }
            f[i][s] = max_p;
        }
    }

    cout << fixed << setprecision(6);
    cout << "f[4][N] = " << f[4]["N"] << " | f[4][V] = " << f[4]["V"] << endl;
    return 0;
}