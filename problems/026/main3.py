import sys
from typing import Literal

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)
N = int(input())


class Node:
    def __init__(self, index: int) -> None:
        self.neighbors: list[Node] = []
        self.visited = False
        self.index = index

    def __lt__(self, other):
        return self.index < other.index


nodes = [Node(i) for i in range(N)]
reds: list[Node] = []
greens: list[Node] = []

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].neighbors.append(nodes[b])
    nodes[b].neighbors.append(nodes[a])


def dfs(node: Node, current_color: Literal["RED", "GREEN"]):
    if current_color == "RED":
        reds.append(node)
        current_color = "GREEN"
    else:
        greens.append(node)
        current_color = "RED"
    node.visited = True
    for neighbor in node.neighbors:
        if not neighbor.visited:
            dfs(neighbor, current_color)


dfs(nodes[0], "RED")
if len(reds) >= N // 2:
    answers = reds
else:
    answers = greens

print(" ".join([str(answer.index + 1) for answer in answers[: N // 2]]))
