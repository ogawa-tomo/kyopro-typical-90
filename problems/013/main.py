import heapq
import sys

max_distance = sys.maxsize


class Node:
    def __init__(self, index: int) -> None:
        self.index = index
        self.distance = max_distance
        self.links: list[Link] = []
        self.finalized = False

    def __repr__(self):
        return str(self.distance)


class Link:
    def __init__(self, distance: int, to_node: Node):
        self.distance = distance
        self.to_node = to_node


class QueueObject:
    def __init__(self, node: Node):
        self.node = node
        self.distance = node.distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __repr__(self):
        return str(self.distance)


def dijkstra(start_node: Node):
    q: list[QueueObject] = []
    start_node.distance = 0

    heapq.heappush(q, QueueObject(start_node))
    while q:
        queue_object = heapq.heappop(q)
        node = queue_object.node

        if node.finalized:
            continue
        node.finalized = True

        for link in node.links:
            distance = node.distance + link.distance
            if distance < link.to_node.distance:
                link.to_node.distance = distance
                heapq.heappush(q, QueueObject(link.to_node))


N, M = map(int, input().split())

# 0からKまでの距離を格納
nodes1: list[Node] = [Node(i) for i in range(N)]
# KからN-1までの距離を格納
nodes2: list[Node] = [Node(i) for i in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    node1_1 = nodes1[a]
    node1_2 = nodes1[b]
    node1_1.links.append(Link(c, node1_2))
    node1_2.links.append(Link(c, node1_1))
    node2_1 = nodes2[a]
    node2_2 = nodes2[b]
    node2_1.links.append(Link(c, node2_2))
    node2_2.links.append(Link(c, node2_1))

dijkstra(nodes1[0])
dijkstra(nodes2[N - 1])

for i in range(N):
    print(nodes1[i].distance + nodes2[i].distance)
