N = int(input())


class Node:
    def __init__(self, index: int) -> None:
        self.neighbors: list[Node] = []
        self.selected = False
        self.index = index

    def is_leaf(self):
        return len(self.neighbors) == 1


nodes = [Node(i) for i in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].neighbors.append(nodes[b])
    nodes[b].neighbors.append(nodes[a])

answers: list[Node] = []
for node in nodes:
    if node.is_leaf():
        node.selected = True
        answers.append(node)

if len(answers) >= N // 2:
    print(" ".join([str(answer.index + 1) for answer in answers]))
    exit()

# 単に深さ優先探索をすればいいのでは？
