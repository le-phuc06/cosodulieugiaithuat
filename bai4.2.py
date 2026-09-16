activities = [
    ('H1', 1, 5), ('H2', 2, 5), ('H3', 2, 6), ('H4', 3, 4), ('H5', 4, 8),
    ('H6', 6, 9), ('H7', 8, 11), ('H8', 9, 14), ('H9', 11, 13), ('H10', 12, 15)
]

def is_compat(a, b):
    return a[2] <= b[1] or b[2] <= a[1]

# 1. Earliest Finish
ef = []
for act in sorted(activities, key=lambda x: x[2]):
    if not ef or act[1] >= ef[-1][2]:
        ef.append(act)

# 2. Earliest Start
es = []
for act in sorted(activities, key=lambda x: x[1]):
    if not es or act[1] >= es[-1][2]:
        es.append(act)

# 3. Shortest Duration
sd = []
rem = list(activities)
while rem:
    valid = [a for a in rem if all(is_compat(a, x) for x in sd)]
    if not valid: break
    valid.sort(key=lambda x: (x[2] - x[1], x[1]))
    sd.append(valid[0])

# 4. Least Overlap
lo = []
while True:
    valid = [a for a in activities if all(is_compat(a, x) for x in lo)]
    if not valid: break
    def overlap_cnt(a):
        return sum(1 for v in valid if v != a and not is_compat(a, v))
    valid.sort(key=lambda x: (overlap_cnt(x), x[2] - x[1]))
    lo.append(valid[0])

print("Ket thuc som nhat:", [x[0] for x in ef], len(ef))
print("Bat dau som nhat:", [x[0] for x in es], len(es))
print("Ngan nhat:", [x[0] for x in sd], len(sd))
print("It chong lan nhat:", [x[0] for x in lo], len(lo))