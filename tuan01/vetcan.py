import sys

# Loi giai theo dung dinh nghia
# Bổ sung thêm max(a) để khớp với đầu ra của tong.cpp
d = sys.stdin.read().split()
if not d:
    sys.exit()
n = int(d[0])
a = list(map(int, d[1:1 + n]))
print(sum(a), max(a))