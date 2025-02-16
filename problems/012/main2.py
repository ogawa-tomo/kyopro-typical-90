from collections import deque
from typing import Union
import sys

sys.setrecursionlimit(1000000)

H, W = map(int, input().split())
Q = int(input())


class Grid:
    def __init__(self, i: int, j: int):
        self.red = False
        self.i = i
        self.j = j
        self.parent: Union[None, Grid] = None
        self.size = 1

    def root(self):
        if self.parent is None:
            return self
        return self.parent.root()

    def __repr__(self):
        return f"({self.i}, {self.j})"


# grids[i][j]: (i, j)が白いならFalse、赤いならTrue
grids: list[list[Grid]] = []
for i in range(H):
    row = []
    for j in range(W):
        row.append(Grid(i, j))
    grids.append(row)


def merge(grid1: Grid, grid2: Grid):
    root1 = grid1.root()
    root2 = grid2.root()
    if root1 == root2:
        return
    if root1.size < root2.size:
        root1.parent = root2
        root2.size += root1.size
    else:
        root2.parent = root1
        root1.size += root2.size


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
            merge(grid, neighbor)
        # 左
        if grid.j > 0 and grids[grid.i][grid.j - 1].red:
            neighbor = grids[grid.i][grid.j - 1]
            merge(grid, neighbor)
        # 右
        if grid.j < W - 1 and grids[grid.i][grid.j + 1].red:
            neighbor = grids[grid.i][grid.j + 1]
            merge(grid, neighbor)
        # 下
        if grid.i < H - 1 and grids[grid.i + 1][grid.j].red:
            neighbor = grids[grid.i + 1][grid.j]
            merge(grid, neighbor)

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
        if from_grid.root() == to_grid.root():
            print("Yes")
        else:
            print("No")
