function main()
    data = split(read(stdin, String))
    if isempty(data)
        return
    end
    n = parse(Int, data[1])
    arr = [parse(Int, x) for x in data[2:n+1]]
    
    total_sum = sum(arr)
    max_val = maximum(arr)
    
    println("$total_sum $max_val")
end

main()