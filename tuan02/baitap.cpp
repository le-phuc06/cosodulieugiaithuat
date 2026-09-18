#include <iostream>
#include <vector>
#include <chrono>

using namespace std;

int board_seq[9][9], board_mrv[9][9];
long long calls_seq = 0, calls_mrv = 0;

bool is_valid(int b[9][9], int r, int c, int val) {
    for (int i = 0; i < 9; ++i)
        if (b[r][i] == val || b[i][c] == val) return false;
    int br = 3*(r/3), bc = 3*(c/3);
    for (int i = br; i < br+3; ++i)
        for (int j = bc; j < bc+3; ++j)
            if (b[i][j] == val) return false;
    return true;
}

bool backtrack_seq() {
    calls_seq++;
    for (int r = 0; r < 9; ++r) {
        for (int c = 0; c < 9; ++c) {
            if (board_seq[r][c] == 0) {
                for (int val = 1; val <= 9; ++val) {
                    if (is_valid(board_seq, r, c, val)) {
                        board_seq[r][c] = val;
                        if (backtrack_seq()) return true;
                        board_seq[r][c] = 0;
                    }
                }
                return false;
            }
        }
    }
    return true;
}

vector<int> get_candidates(int b[9][9], int r, int c) {
    bool used[10] = {false};
    for (int i = 0; i < 9; ++i) { used[b[r][i]] = true; used[b[i][c]] = true; }
    int br = 3*(r/3), bc = 3*(c/3);
    for (int i = br; i < br+3; ++i)
        for (int j = bc; j < bc+3; ++j) used[b[i][j]] = true;
    vector<int> cands;
    for (int v = 1; v <= 9; ++v) if (!used[v]) cands.push_back(v);
    return cands;
}

bool backtrack_mrv() {
    calls_mrv++;
    int min_cands = 10, best_r = -1, best_c = -1;
    vector<int> best_cands;

    for (int r = 0; r < 9; ++r) {
        for (int c = 0; c < 9; ++c) {
            if (board_mrv[r][c] == 0) {
                vector<int> cands = get_candidates(board_mrv, r, c);
                if (cands.size() < min_cands) {
                    min_cands = cands.size();
                    best_r = r; best_c = c;
                    best_cands = cands;
                    if (min_cands == 0) break;
                }
            }
        }
    }

    if (best_r == -1) return true;
    if (min_cands == 0) return false;

    for (int val : best_cands) {
        board_mrv[best_r][best_c] = val;
        if (backtrack_mrv()) return true;
        board_mrv[best_r][best_c] = 0;
    }
    return false;
}

int main() {
    int init[9][9] = {
        {5, 3, 0, 0, 7, 0, 0, 0, 0}, {6, 0, 0, 1, 9, 5, 0, 0, 0}, {0, 9, 8, 0, 0, 0, 0, 6, 0},
        {8, 0, 0, 0, 6, 0, 0, 0, 3}, {4, 0, 0, 8, 0, 3, 0, 0, 1}, {7, 0, 0, 0, 2, 0, 0, 0, 6},
        {0, 6, 0, 0, 0, 0, 2, 8, 0}, {0, 0, 0, 4, 1, 9, 0, 0, 5}, {0, 0, 0, 0, 8, 0, 0, 7, 9}
    };
    for(int i=0;i<9;++i) for(int j=0;j<9;++j) board_seq[i][j] = board_mrv[i][j] = init[i][j];

    backtrack_seq();
    backtrack_mrv();

    cout << "Quet tuan tu: So loi goi = " << calls_seq << endl;
    cout << "MRV          : So loi goi = " << calls_mrv << endl;
    return 0;
}