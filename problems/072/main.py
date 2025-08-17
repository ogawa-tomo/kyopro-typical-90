import sys

sys.setrecursionlimit(120000)


H, W = map(int, input().split())


class Grid:
    def __init__(self, is_field: bool):
        self.is_field = is_field
        self.visited = False
        self.neighbors: list[Grid] = []

    def __repr__(self):
        if self.is_field:
            return "."
        else:
            return "#"


grids: list[list[Grid]] = []

for i in range(H):
    row: list[Grid] = []
    data = list(input())
    for j in range(W):
        d = data[j]
        is_field = d == "."
        row.append(Grid(is_field))
    grids.append(row)

# set neighbors
for i in range(H):
    for j in range(W):
        neighbors: list[Grid] = []
        grid = grids[i][j]
        if i > 0:
            neighbor = grids[i - 1][j]
            if neighbor.is_field:
                neighbors.append(neighbor)
        if j > 0:
            neighbor = grids[i][j - 1]
            if neighbor.is_field:
                neighbors.append(neighbor)
        if i < H - 1:
            neighbor = grids[i + 1][j]
            if neighbor.is_field:
                neighbors.append(neighbor)
        if j < W - 1:
            neighbor = grids[i][j + 1]
            if neighbor.is_field:
                neighbors.append(neighbor)
        grid.neighbors = neighbors


# start_gridからgoal_gridまで行くときの距離
def dfs(start_grid: Grid, goal_grid: Grid) -> int:
    # 戻ってきたら、0を返す
    if start_grid == goal_grid and start_grid.visited:
        return 0

    start_grid.visited = True
    ret = -10000  # ここを0にすると失敗する。十分小さな値にしておく必要がある…？
    for neighbor in start_grid.neighbors:
        if neighbor != goal_grid and neighbor.visited:
            continue
        v = dfs(neighbor, goal_grid)
        ret = max(ret, v + 1)
    start_grid.visited = False
    return ret


answer = 0
for i in range(H):
    for j in range(W):
        start_grid = grids[i][j]
        if start_grid.is_field:
            answer = max(answer, dfs(start_grid, start_grid))

if answer <= 2:  # 適切な経路が存在しないときは2が返ってきてしまう
    print(-1)
else:
    print(answer)
