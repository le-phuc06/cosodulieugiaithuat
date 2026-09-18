import random, sys

# Nhan mot so tu dong lenh lam hat giong ngau nhien
seed = int(sys.argv[1])
random.seed(seed)

# Co du lieu phai NHO: loi van hien ra, ma nhin bang mat duoc
n = random.randint(1, 8)
print(n)
print(*[random.randint(-100, 100) for _ in range(n)])