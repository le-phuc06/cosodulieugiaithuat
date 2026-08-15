import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    arr = [int(x) for x in data[1:n+1]]
    
    total_sum = sum(arr)
    max_val = max(arr)
    
    print(f"{total_sum} {max_val}")

if __name__ == '__main__':
    main()