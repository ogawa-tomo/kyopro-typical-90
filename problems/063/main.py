H, W = map(int, input().split())
grids: list[list[int]] = []
for _ in range(H):
    row = list(map(int, input().split()))
    grids.append(row)

# print(grids)
answer = 0
# ビット全探索で、選ぶ行の組み合わせを列挙する
for i in range(1 << H):
    selected_row_indexes: list[int] = []
    for r in range(H):
        if i & 1 << r:
            selected_row_indexes.append(r)
    # print(selected_row_indexes)
    if len(selected_row_indexes) == 0:
        continue

    # 選ばれた行について、同じ数字である列を調べる
    column_indexes: list[int] = []
    for column_index in range(W):
        num = 0
        same = True
        for i, row_index in enumerate(selected_row_indexes):
            if i == 0:
                num = grids[row_index][column_index]
                continue
            if num != grids[row_index][column_index]:
                same = False
                break
        if same:
            column_indexes.append(column_index)
    # 対象の1行について、同じ数字である列を抽出
    num_list: list[int] = []
    target_row = grids[selected_row_indexes[0]]
    for column_index in column_indexes:
        num_list.append(target_row[column_index])
    # count[i]: 数字iが出た回数
    count: list[int] = [0] * (10000 * 8 + 1)
    max_count = 0
    for num in num_list:
        count[num] += 1
        max_count = max(max_count, count[num])

    answer = max(answer, max_count * len(selected_row_indexes))

print(answer)
