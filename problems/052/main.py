N = int(input())
S = 1
mod = 10**9 + 7
for _ in range(N):
    A = list(map(int, input().split()))
    S *= sum(A)
    S %= mod
print(S)
