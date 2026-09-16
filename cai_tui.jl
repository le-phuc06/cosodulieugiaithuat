# QUY ƯỚC CHỈ SỐ JULIA:
# Do Julia đánh chỉ số mảng bắt đầu từ 1, bảng f được khởi tạo kích thước (n+1) x (W+1).
# Tọa độ f[i+1, j+1] trong Julia tương ứng chính xác với trạng thái f[i][j] trong thuật toán 
# (với i chạy từ 0 đến n, j chạy từ 0 đến W).

function cai_tui()
    n = 5
    W = 11
    names = ["A", "B", "C", "D", "E"]
    w = [2, 3, 4, 5, 7]
    v = [3, 7, 9, 12, 16]

    f = zeros(Int, n + 1, W + 1)

    for i in 1:n
        for j in 1:W
            if w[i] > j
                f[i + 1, j + 1] = f[i, j + 1]
            else
                f[i + 1, j + 1] = max(f[i, j + 1], f[i, j + 1 - w[i]] + v[i])
            end
        end
    end

    println("Bảng f[i][j]:")
    for i in 0:n
        println(f[i + 1, :])
    end

    println("\nGiá trị lớn nhất: ", f[n + 1, W + 1])

    curr_w = W
    selected = String[]
    for i in n:-1:1
        if f[i + 1, curr_w + 1] != f[i, curr_w + 1]
            push!(selected, names[i])
            curr_w -= w[i]
        end
    end

    reverse!(selected)
    println("Tập đồ vật được chọn: ", join(selected, ", "))
end

cai_tui()