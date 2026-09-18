function solve_sudoku()
    init_grid = [
        5 3 0 0 7 0 0 0 0;
        6 0 0 1 9 5 0 0 0;
        0 9 8 0 0 0 0 6 0;
        8 0 0 0 6 0 0 0 3;
        4 0 0 8 0 3 0 0 1;
        7 0 0 0 2 0 0 0 6;
        0 6 0 0 0 0 2 8 0;
        0 0 0 4 1 9 0 0 5;
        0 0 0 0 8 0 0 7 9
    ]

    # 1. Sequential
    board_seq = copy(init_grid)
    calls_seq = 0

    function is_valid(b, r, c, val)
        for i in 1:9
            (b[r, i] == val || b[i, c] == val) && return false
        end
        br, bc = 3*div(r-1, 3)+1, 3*div(c-1, 3)+1
        for i in br:br+2, j in bc:bc+2
            b[i, j] == val && return false
        end
        return true
    end

    function backtrack_seq()
        calls_seq += 1
        for r in 1:9, c in 1:9
            if board_seq[r, c] == 0
                for val in 1:9
                    if is_valid(board_seq, r, c, val)
                        board_seq[r, c] = val
                        backtrack_seq() && return true
                        board_seq[r, c] = 0
                    end
                end
                return false
            end
        end
        return true
    end

    # 2. MRV
    board_mrv = copy(init_grid)
    calls_mrv = 0

    function get_candidates(b, r, c)
        used = Set{Int}()
        for i in 1:9
            push!(used, b[r, i]); push!(used, b[i, c])
        end
        br, bc = 3*div(r-1, 3)+1, 3*div(c-1, 3)+1
        for i in br:br+2, j in bc:bc+2
            push!(used, b[i, j])
        end
        return [v for v in 1:9 if !(v in used)]
    end

    function backtrack_mrv()
        calls_mrv += 1
        min_cands, best_r, best_c = 10, 0, 0
        best_cands = Int[]
        for r in 1:9, c in 1:9
            if board_mrv[r, c] == 0
                cands = get_candidates(board_mrv, r, c)
                if length(cands) < min_cands
                    min_cands = length(cands)
                    best_r, best_c = r, c
                    best_cands = cands
                    min_cands == 0 && break
                end
            end
        end
        best_r == 0 && return true
        min_cands == 0 && return false

        for val in best_cands
            board_mrv[best_r, best_c] = val
            backtrack_mrv() && return true
            board_mrv[best_r, best_c] = 0
        end
        return false
    end

    backtrack_seq()
    backtrack_mrv()

    println("Quet tuan tu: So loi goi = $calls_seq")
    println("MRV          : So loi goi = $calls_mrv")
    println("Loi giai giong nhau? $(board_seq == board_mrv)")
end

solve_sudoku()