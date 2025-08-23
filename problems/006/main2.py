# こちらの解法を参考
# https://drken1215.hatenablog.com/entry/2021/10/10/195200
# なぜか2問だけWA…

N, K = map(int, input().split())
S = list(input())


alphabets = list("abcdfeghijklmnopqrstuvwxyz")


def make_alphabet_dict() -> dict[str, int]:
    alphabet_dict: dict[str, int] = {}
    for alphabet in alphabets:
        alphabet_dict[alphabet] = N
    return alphabet_dict


# nex[i][c]: Sのi文字目以降で、文字cが登場する最小のインデックス（ただし、登場しない場合はN）
nex: list[dict[str, int]] = [make_alphabet_dict() for _ in range(N)]

for i in range(N):
    index = N - 1 - i  # 後ろから調べる

    # index + 1文字目で初期化
    if index < N - 1:
        for alphabet in alphabets:
            nex[index][alphabet] = nex[index + 1][alphabet]

    # index番目に登場した文字を反映
    nex[index][S[index]] = index

answer: list[str] = []

j = -1  # 文字列Sの中で、最後にとった文字の添字
# 答えの文字列のうち、0文字目からK-1文字目まで順番に調べていく
for k in range(K):
    # aから順にアルファベットを調べていく
    for alphabet in alphabets:
        # 文字列Sの中で、最後にとった文字のインデックスより大きいインデックスで、alphabetが最初に出るインデックス
        index = nex[j + 1][alphabet]
        # この文字を採用するとしたとき、残りの文字数が足りるか
        remaining = K - 1 - k  # 残り取る必要のある文字
        # 足りていればこの文字を採用してbreak
        if N - 1 - index >= remaining:
            j = index
            answer.append(alphabet)
            break

print("".join(answer))
