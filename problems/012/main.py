from collections import deque

H, W = map(int, input().split())
Q = int(input())


class Grid:
    def __init__(self, i: int, j: int):
        self.red = False
        self.i = i
        self.j = j
        self.neighbors: list[Grid] = []

    def __repr__(self):
        return f"({self.i}, {self.j})"


# grids[i][j]: (i, j)が白いならFalse、赤いならTrue
grids: list[list[Grid]] = []
for i in range(H):
    row = []
    for j in range(W):
        row.append(Grid(i, j))
    grids.append(row)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        r = q[1] - 1
        c = q[2] - 1
        grid = grids[r][c]
        grid.red = True
        # 上
        if grid.i > 0 and grids[grid.i - 1][grid.j].red:
            neighbor = grids[grid.i - 1][grid.j]
            grid.neighbors.append(neighbor)
            neighbor.neighbors.append(grid)
        # 左
        if grid.j > 0 and grids[grid.i][grid.j - 1].red:
            neighbor = grids[grid.i][grid.j - 1]
            grid.neighbors.append(neighbor)
            neighbor.neighbors.append(grid)
        # 右
        if grid.j < W - 1 and grids[grid.i][grid.j + 1].red:
            neighbor = grids[grid.i][grid.j + 1]
            grid.neighbors.append(neighbor)
            neighbor.neighbors.append(grid)
        # 下
        if grid.i < H - 1 and grids[grid.i + 1][grid.j].red:
            neighbor = grids[grid.i + 1][grid.j]
            grid.neighbors.append(neighbor)
            neighbor.neighbors.append(grid)

    elif q[0] == 2:
        ra = q[1] - 1
        ca = q[2] - 1
        rb = q[3] - 1
        cb = q[4] - 1
        from_grid = grids[ra][ca]
        to_grid = grids[rb][cb]
        if not from_grid.red or not to_grid.red:
            print("No")
            continue
        if from_grid == to_grid:
            print("Yes")
            continue
        d: deque[Grid] = deque()
        d.append(from_grid)
        visited: set[Grid] = set()
        visited.add(from_grid)
        while d:
            grid = d.popleft()
            arrived = False
            for neighbor in grid.neighbors:
                if neighbor in visited:
                    continue
                if neighbor == to_grid:
                    arrived = True
                    break
                d.append(neighbor)
            if arrived:
                break
        if arrived:
            print("Yes")
        else:
            print("No")
