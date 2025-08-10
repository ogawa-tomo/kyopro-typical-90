# だいたい合うんだけど3ケースでTLE

from collections import deque
import sys


class Node:
    def __init__(self, is_wall: bool, i: int, j: int):
        # このノードで右（左、上、下）を向くまでの方向転換の最小回数
        self.turn_num_right = sys.maxsize
        self.turn_num_left = sys.maxsize
        self.turn_num_above = sys.maxsize
        self.turn_num_below = sys.maxsize
        self.is_wall = is_wall
        self.i = i
        self.j = j

    def __repr__(self):
        if self.is_wall:
            return "#"
        else:
            return "."


H, W = map(int, input().split())
rs, cs = map(int, input().split())
rs -= 1
cs -= 1
rt, ct = map(int, input().split())
rt -= 1
ct -= 1
grids: list[list[Node]] = []

for i in range(H):
    row = list(input())
    node_row: list[Node] = []
    for j in range(W):
        grid = row[j]
        is_wall = grid == "#"
        node_row.append(Node(is_wall, i, j))

    grids.append(node_row)
# print(grids)

d: deque[Node] = deque()
start_node = grids[rs][cs]
start_node.turn_num_above = 0
start_node.turn_num_below = 0
start_node.turn_num_right = 0
start_node.turn_num_left = 0
d.append(start_node)

while d:
    current_node = d.popleft()
    # 上
    if current_node.i > 0:
        above_node = grids[current_node.i - 1][current_node.j]
        if not above_node.is_wall:
            append = False
            if current_node.turn_num_above + 1 < above_node.turn_num_left:
                above_node.turn_num_left = current_node.turn_num_above + 1
                append = True
            if current_node.turn_num_above + 1 < above_node.turn_num_right:
                above_node.turn_num_right = current_node.turn_num_above + 1
                append = True
            if current_node.turn_num_above < above_node.turn_num_above:
                above_node.turn_num_above = current_node.turn_num_above
                append = True
            if append:
                d.append(above_node)
    # 右
    if current_node.j < W - 1:
        right_node = grids[current_node.i][current_node.j + 1]
        if not right_node.is_wall:
            append = False
            if current_node.turn_num_right < right_node.turn_num_right:
                right_node.turn_num_right = current_node.turn_num_right
                append = True
            if current_node.turn_num_right + 1 < right_node.turn_num_above:
                right_node.turn_num_above = current_node.turn_num_right + 1
                append = True
            if current_node.turn_num_right + 1 < right_node.turn_num_below:
                right_node.turn_num_below = current_node.turn_num_right + 1
                append = True
            if append:
                d.append(right_node)

    # 左
    if current_node.j > 0:
        left_node = grids[current_node.i][current_node.j - 1]
        if not left_node.is_wall:
            append = False
            if current_node.turn_num_left < left_node.turn_num_left:
                left_node.turn_num_left = current_node.turn_num_left
                append = True
            if current_node.turn_num_left + 1 < left_node.turn_num_above:
                left_node.turn_num_above = current_node.turn_num_left + 1
                append = True
            if current_node.turn_num_left + 1 < left_node.turn_num_below:
                left_node.turn_num_below = current_node.turn_num_left + 1
                append = True
            if append:
                d.append(left_node)

    # 下
    if current_node.i < H - 1:
        below_node = grids[current_node.i + 1][current_node.j]
        if not below_node.is_wall:
            append = False
            if current_node.turn_num_below < below_node.turn_num_below:
                below_node.turn_num_below = current_node.turn_num_below
                append = True
            if current_node.turn_num_below + 1 < below_node.turn_num_right:
                below_node.turn_num_right = current_node.turn_num_below + 1
                append = True
            if current_node.turn_num_below + 1 < below_node.turn_num_left:
                below_node.turn_num_left = current_node.turn_num_below + 1
                append = True
            if append:
                d.append(below_node)

goal_node = grids[rt][ct]
print(
    min(
        goal_node.turn_num_below,
        goal_node.turn_num_above,
        goal_node.turn_num_right,
        goal_node.turn_num_left,
    )
)
