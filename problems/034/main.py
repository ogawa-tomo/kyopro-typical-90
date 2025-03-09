N, K = map(int, input().split())
A = list(map(int, input().split()))

# emerged[i]: iが現れた回数
# emerged = [0] * (10**9 + 1)  # こうするとメモリエラーになる
emerged: dict[int, int] = {}  # 単に空のディクショナリとして用意してやればよさそう

answer = 1
end_index = 0
start = A[0]
emerged[start] = 1
current_type_num = 1
for start_index in range(N - 1):
    start = A[start_index]

    # タイプ数がKより多かったら次へ
    if current_type_num > K:
        emerged[start] -= 1
        if emerged[start] == 0:
            current_type_num -= 1
        continue

    # end_indexを増やせるだけ増やしていく
    while end_index < N - 1:
        end_index += 1
        end = A[end_index]
        if not end in emerged:
            emerged[end] = 0
        emerged[end] += 1
        if emerged[end] == 1:
            current_type_num += 1
            if current_type_num > K:
                break
        # end_indexを増やせたので、更新
        answer = max(answer, end_index - start_index + 1)

    # end_indexを増やし過ぎたら、start_indexを増やす準備
    emerged[start] -= 1
    if emerged[start] == 0:
        current_type_num -= 1

print(answer)
