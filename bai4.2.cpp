#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

struct Act { string id; int s, f; };

bool isCompat(const Act& a, const Act& b) {
    return a.f <= b.s || b.f <= a.s;
}

int main() {
    vector<Act> acts = {
        {"H1", 1, 5}, {"H2", 2, 5}, {"H3", 2, 6}, {"H4", 3, 4}, {"H5", 4, 8},
        {"H6", 6, 9}, {"H7", 8, 11}, {"H8", 9, 14}, {"H9", 11, 13}, {"H10", 12, 15}
    };

    // Earliest Finish
    auto ef_acts = acts;
    sort(ef_acts.begin(), ef_acts.end(), [](const Act& a, const Act& b){ return a.f < b.f; });
    vector<Act> ef;
    for (auto& a : ef_acts) {
        if (ef.empty() || a.s >= ef.back().f) ef.push_back(a);
    }

    cout << "Ket thuc som nhat: " << ef.size() << " hoat dong (" ;
    for (auto& a : ef) cout << a.id << " ";
    cout << ")" << endl;

    return 0;
}