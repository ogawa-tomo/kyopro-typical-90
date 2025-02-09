N = int(input())
S = list(input())
mod = 10**9 + 7

atcoder = ["a", "t", "c", "o", "d", "e", "r"]
print(S)
string = []
for s in S:
    if s in atcoder:
        string.append(s)
print(string)


answer = 1
current_index = 0
for current_letter in atcoder:
    while True:
        if S[current_index] == current_letter:
            break
        current_index += 1
    num_letter = 0
    while True:
        if current_index >= N or S[current_index] != current_letter:
            break
        current_index += 1
        num_letter += 1
    answer *= num_letter
    answer %= mod
print(answer)
# 連続してないときがうまく使えない
