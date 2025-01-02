N = int(input())
A, B, C = map(int, input().split())


max_num = 10000
answer = max_num
for a_num in range(max_num):
    if A * a_num > N:
        break
    for b_num in range(max_num):
        value = A * a_num + B * b_num
        if value > N:
            break
        if (N - value) % C == 0:
            answer = min(answer, a_num + b_num + (N - value) // C)

print(answer)
