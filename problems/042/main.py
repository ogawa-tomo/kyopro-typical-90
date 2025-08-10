mod = 10**9 + 7
K = int(input())

# Xが9の倍数であることと、Xを10進法で表したときの各桁の数字の和が9の倍数であることが同値
if K % 9 != 0:
    print(0)
    exit()

# 各桁の数字の和がKとなる整数の数を求める

# dp[i]:各桁の数字の和がiとなる整数の数
dp: list[int] = [0] * (K + 1)
dp[0] = 1
for k in range(1, K + 1):
    for i in range(1, 10):
        if k - i < 0:
            continue
        dp[k] += dp[k - i]
    dp[k] %= mod

print(dp[K])
