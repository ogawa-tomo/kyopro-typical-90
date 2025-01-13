N, K = map(int, input().split())
mod = 10**9 + 7
if N == 1:
    print(K % mod)
    exit()

if N == 2:
    print(K * (K - 1) % mod)
    exit()

if K <= 2:
    print(0)
    exit()

print(K * (K - 1) * pow(K - 2, N - 2, mod) % mod)
