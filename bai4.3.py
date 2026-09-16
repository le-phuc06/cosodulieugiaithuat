# Model LM
lm = {
    'em': {'học': 0.52, 'đi': 0.48},
    'học': {'bài': 0.40, 'toán': 0.35, 'vẽ': 0.25},
    'đi': {'chợ': 0.58, 'bơi': 0.22, 'ngủ': 0.20}
}

def beam_search(k):
    beam = [(["em"], 1.0)]
    for step in range(2):
        cand = []
        for path, p in beam:
            last = path[-1]
            for nxt, tp in lm[last].items():
                cand.append((path + [nxt], p * tp))
        cand.sort(key=lambda x: x[1], reverse=True)
        beam = cand[:k]
    return beam[0]

print("Beam k=1:", beam_search(1))
print("Beam k=2:", beam_search(2))

# Viterbi HMM
states = ['N', 'V']
pi = {'N': 0.6, 'V': 0.4}
A = {'N': {'N': 0.35, 'V': 0.65}, 'V': {'N': 0.70, 'V': 0.30}}
B = {
    'N': {'em': 0.35, 'học': 0.10, 'bài': 0.40, 'toán': 0.30},
    'V': {'em': 0.05, 'học': 0.45, 'bài': 0.05, 'toán': 0.02}
}
words = ['em', 'học', 'bài', 'toán']

f = [{} for _ in range(5)]
prev = [{} for _ in range(5)]

for s in states:
    f[1][s] = pi[s] * B[s]['em']

for i in range(2, 5):
    w = words[i-1]
    for s in states:
        best_p, best_prev = -1, None
        for ps in states:
            p = f[i-1][ps] * A[ps][s] * B[s][w]
            if p > best_p:
                best_p, best_prev = p, ps
        f[i][s] = best_p
        prev[i][s] = best_prev

print("Viterbi max prob:", max(f[4].values()))