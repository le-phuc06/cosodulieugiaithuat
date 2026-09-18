import time

def solve_sudoku():
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    # --- 1. Sequential Scan ---
    board_seq = [row[:] for row in grid]
    calls_seq = 0

    def is_valid(b, r, c, val):
        for i in range(9):
            if b[r][i] == val or b[i][c] == val: return False
        br, bc = 3*(r//3), 3*(c//3)
        for i in range(br, br+3):
            for j in range(bc, bc+3):
                if b[i][j] == val: return False
        return True

    def backtrack_seq():
        nonlocal calls_seq
        calls_seq += 1
        for r in range(9):
            for c in range(9):
                if board_seq[r][c] == 0:
                    for val in range(1, 10):
                        if is_valid(board_seq, r, c, val):
                            board_seq[r][c] = val
                            if backtrack_seq(): return True
                            board_seq[r][c] = 0
                    return False
        return True

    # --- 2. MRV Scan ---
    board_mrv = [row[:] for row in grid]
    calls_mrv = 0

    def get_candidates(b, r, c):
        used = set(b[r]) | {b[i][c] for i in range(9)}
        br, bc = 3*(r//3), 3*(c//3)
        for i in range(br, br+3):
            for j in range(bc, bc+3):
                used.add(b[i][j])
        return [v for v in range(1, 10) if v not in used]

    def backtrack_mrv():
        nonlocal calls_mrv
        calls_mrv += 1
        min_cands, best_cell, best_cands = 10, None, []
        for r in range(9):
            for c in range(9):
                if board_mrv[r][c] == 0:
                    cands = get_candidates(board_mrv, r, c)
                    if len(cands) < min_cands:
                        min_cands = len(cands)
                        best_cell = (r, c)
                        best_cands = cands
                        if min_cands == 0: break
        if best_cell is None: return True
        if min_cands == 0: return False

        r, c = best_cell
        for val in best_cands:
            board_mrv[r][c] = val
            if backtrack_mrv(): return True
            board_mrv[r][c] = 0
        return False

    t0 = time.time(); backtrack_seq(); t1 = time.time()
    t2 = time.time(); backtrack_mrv(); t3 = time.time()

    print(f"Quet tuan tu: So loi goi = {calls_seq}, Thoi gian = {(t1-t0)*1000:.2f}ms")
    print(f"MRV          : So loi goi = {calls_mrv}, Thoi gian = {(t3-t2)*1000:.2f}ms")
    print(f"Loi giai giong nhau? {board_seq == board_mrv}")

solve_sudoku()