function greedy_coin_change(coins, S)
    sorted_coins = sort(coins, rev=true)
    res = Int[]
    rem = S
    for c in sorted_coins
        cnt = div(rem, c)
        if cnt > 0
            append!(res, fill(c, cnt))
            rem %= c
        end
    end
    return res
end

function dp_coin_change(coins, S)
    dp = fill(10^9, S + 1)
    used = fill(-1, S + 1)
    dp[1] = 0 # tuong ung vơi S = 0 o chi so 1
    for i in 1:S
        for c in coins
            if i >= c && dp[i - c + 1] + 1 < dp[i + 1]
                dp[i + 1] = dp[i - c + 1] + 1
                used[i + 1] = c
            end
        end
    end
    res = Int[]
    curr = S
    while curr > 0
        c = used[curr + 1]
        push!(res, c)
        curr -= c
    end
    return res
end

sets = [
    ([1, 4, 6, 9], 12),
    ([1, 5, 10, 20, 50], 85),
    ([1, 3, 7, 12], 20),
    ([1, 2, 5, 10], 38),
    ([1, 6, 10], 12),
    ([1, 4, 5, 15, 20], 23)
]

for (idx, (coins, S)) in enumerate(sets)
    g_ans = greedy_coin_change(coins, S)
    d_ans = dp_coin_change(coins, S)
    status = length(g_ans) == length(d_ans) ? "Dung" : "Sai"
    println("Bo $idx: Tham lam = $(length(g_ans)) to | DP = $(length(d_ans)) to -> Tham lam $status")
end