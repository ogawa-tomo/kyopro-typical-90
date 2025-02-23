N = int(input())

length = 1000

calc_sum_grid: list[list[int]] = []
for _ in range(length + 1):
    calc_sum_grid.append([0] * (length + 1))

for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    calc_sum_grid[lx][ly] += 1
    calc_sum_grid[lx][ry] -= 1
    calc_sum_grid[rx][ly] -= 1
    calc_sum_grid[rx][ry] += 1

for x in range(length + 1):
    for y in range(1, length + 1):
        calc_sum_grid[x][y] = calc_sum_grid[x][y - 1] + calc_sum_grid[x][y]
for y in range(length + 1):
    for x in range(1, length + 1):
        calc_sum_grid[x][y] = calc_sum_grid[x - 1][y] + calc_sum_grid[x][y]

# answers[k]: 紙がk枚重なっている部分の面積
answers = [0] * (N + 1)
for x in range(length):
    for y in range(length):
        answers[calc_sum_grid[x][y]] += 1

for answer in answers[1:]:
    print(answer)
