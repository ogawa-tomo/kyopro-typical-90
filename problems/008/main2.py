N = int(input())
S = list(input())
mod = 10**9 + 7

atcoder = ["a", "t", "c", "o", "d", "e", "r"]
M = len(atcoder)

# dp[i][j]: 文字列Sの最初のi文字から何文字か抜き出して繋げる方法のうち、それが"atcoder"の最初のj文字まで一致するような方法の個数
dp = [[0] * (M + 1)] * (N + 1)

for i in range(N + 1):
    dp[i][0] = 1
for i in range(1, N + 1):
    i_index = i - 1
    for j in range(1, M + 1):
        j_index = j - 1
        dp[i][j] = dp[i - 1][j]
        if S[i_index] == atcoder[j_index]:
            dp[i][j] += dp[i - 1][j - 1]
        dp[i][j] %= mod
print(dp[N][M])
