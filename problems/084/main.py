N = int(input())
S = list(input())

answer = 0
left = 0
right = 1
while right < N:
    if S[left] != S[right]:
        answer += (N - right) * (right - left)
        left = right
        right = left + 1
    else:
        right += 1
print(answer)
