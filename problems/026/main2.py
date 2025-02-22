import sys

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

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].neighbors.append(nodes[b])
    nodes[b].neighbors.append(nodes[a])

answers: list[Node] = []


def dfs(node: Node, even: bool):
    if even:
        answers.append(node)
    even = not even
    node.visited = True
    for neighbor in node.neighbors:
        if not neighbor.visited:
            dfs(neighbor, even)


dfs(nodes[0], True)
answers.sort()

print(" ".join([str(answer.index + 1) for answer in answers[: N // 2]]))
# print(" ".join([str(answer.index + 1) for answer in answers]))
