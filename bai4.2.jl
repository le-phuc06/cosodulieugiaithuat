struct Act
    id::String
    s::Int
    f::Int
end

is_compat(a::Act, b::Act) = a.f <= b.s || b.f <= a.s

acts = [
    Act("H1", 1, 5), Act("H2", 2, 5), Act("H3", 2, 6), Act("H4", 3, 4), Act("H5", 4, 8),
    Act("H6", 6, 9), Act("H7", 8, 11), Act("H8", 9, 14), Act("H9", 11, 13), Act("H10", 12, 15)
]

# Earliest Finish
ef_acts = sort(acts, by = x -> x.f)
ef = Act[]
for a in ef_acts
    if isempty(ef) || a.s >= ef[end].f
        push!(ef, a)
    end
end

println("Ket thuc som nhat: $(length(ef)) hoat dong - ", map(x -> x.id, ef))