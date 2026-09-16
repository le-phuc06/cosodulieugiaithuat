def greedy_coin_change(coins, S):
    coins = sorted(coins, reverse=True)
    res = []
    rem = S
    for c in coins:
        cnt = rem // c
        if cnt > 0:
            res.extend([c] * cnt)
            rem %= c
    return res if rem == 0 else []

def dp_coin_change(coins, S):
    dp = [float('inf')] * (S + 1)
    used = [-1] * (S + 1)
    dp[0] = 0
    for i in range(1, S + 1):
        for c in coins:
            if i >= c and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
                used[i] = c
    if dp[S] == float('inf'):
        return []
    curr = S
    res = []
    while curr > 0:
        c = used[curr]
        res.append(c)
        curr -= c
    return res

sets = [
    ([1, 4, 6, 9], 12),
    ([1, 5, 10, 20, 50], 85),
    ([1, 3, 7, 12], 20),
    ([1, 2, 5, 10], 38),
    ([1, 6, 10], 12),
    ([1, 4, 5, 15, 20], 23)
]

for idx, (coins, S) in enumerate(sets, 1):
    g_ans = greedy_coin_change(coins, S)
    d_ans = dp_coin_change(coins, S)
    is_correct = "Đúng" if len(g_ans) == len(d_ans) else "Sai"
    print(f"Bộ {idx}: Tham lam = {len(g_ans)} tờ {g_ans} | DP = {len(d_ans)} tờ {d_ans} -> Tham lam {is_correct}")