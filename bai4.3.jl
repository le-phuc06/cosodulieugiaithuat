states = ["N", "V"]
pi_dist = Dict("N" => 0.6, "V" => 0.4)
A = Dict("N" => Dict("N" => 0.35, "V" => 0.65), "V" => Dict("N" => 0.70, "V" => 0.30))
B = Dict(
    "N" => Dict("em" => 0.35, "hoc" => 0.10, "bai" => 0.40, "toan" => 0.30),
    "V" => Dict("em" => 0.05, "hoc" => 0.45, "bai" => 0.05, "toan" => 0.02)
)

words = ["em", "hoc", "bai", "toan"]
f = [Dict{String, Float64}() for _ in 1:4]

for s in states
    f[1][s] = pi_dist[s] * B[s]["em"]
end

for i in 2:4
    w = words[i]
    for s in states
        best_p = -1.0
        for ps in states
            p = f[i-1][ps] * A[ps][s] * B[s][w]
            if p > best_p
                best_p = p
            end
        end
        f[i][s] = best_p
    end
end

println("f[4][N] = ", round(f[4]["N"], digits=6))
println("f[4][V] = ", round(f[4]["V"], digits=6))