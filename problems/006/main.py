# 2次元DPで解こうとしたが、TLEだったりWA

N, K = map(int, input().split())
S = list(input())


def index(char: str):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    return alphabets.index(char) + 1


def dict_score(before: int, add: int):
    if before == 0:
        return add * (26**2)
    if before < 26**2 + 26:
        return before + add * 26
    return before + add


def score(string: str):
    if string == "":
        return 0
    if len(string) == 1:
        return index(string) * (26**2)
    if len(string) == 2:
        return (26**2) * index(string[0]) + 26 * index(string[1])
    return (26**2) * index(string[0]) + 26 * index(string[1]) + index(string[2])


# dp[i][j]: i文字目をj文字目に選んだとき、最小の辞書順のスコアとなる文字列
dp: list[list[str]] = []
for _ in range(N):
    row = ["z" * K] * (K + 1)
    dp.append(row)
# print(dp)
dp[0][0] = ""
dp[0][1] = S[0]
for i in range(1, N):
    for j in range(K + 1):
        if j == 0:
            dp[i][j] = ""
            continue
        unselect_str = dp[i - 1][j]
        select_str = dp[i - 1][j - 1] + S[i]
        if score(select_str) < score(unselect_str):
            dp[i][j] = select_str
        else:
            dp[i][j] = unselect_str


print(dp[N - 1][K])
