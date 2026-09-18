def cai_tui():
    n = 5
    W = 11
    names = ["A", "B", "C", "D", "E"]
    w = [0, 2, 3, 4, 5, 7]
    v = [0, 3, 7, 9, 12, 16]

    f = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if w[i] > j:
                f[i][j] = f[i - 1][j]
            else:
                f[i][j] = max(f[i - 1][j], f[i - 1][j - w[i]] + v[i])

    print("Bảng f[i][j]:")
    for row in f:
        print(" ".join(f"{x:3d}" for x in row))

    print(f"\nGiá trị lớn nhất: {f[n][W]}")

    curr_w = W
    selected = []
    for i in range(n, 0, -1):
        if f[i][curr_w] != f[i - 1][curr_w]:
            selected.append(names[i - 1])
            curr_w -= w[i]

    selected.reverse()
    print("Tập đồ vật được chọn:", ", ".join(selected))

if __name__ == "__main__":
    cai_tui()