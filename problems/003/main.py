from collections import deque
import sys


class City:
    def __init__(self, index: int) -> None:
        self.index = index
        self.neighbors: list[City] = []
        self.distance = sys.maxsize

    def reset_distance(self):
        self.distance = sys.maxsize

    def set_distance(self, distance):
        self.distance = distance

    def is_ditermined_distance(self):
        return self.distance != sys.maxsize


N = int(input())
cities = [City(i) for i in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    city_a = cities[a]
    city_b = cities[b]
    city_a.neighbors.append(city_b)
    city_b.neighbors.append(city_a)


def farthest_city(start_city: City):
    queue: deque[City] = deque()
    queue.append(start_city)
    for city in cities:
        city.reset_distance()
    start_city.set_distance(0)
    farthest_city = start_city

    while queue:
        city = queue.popleft()
        current_distance = city.distance + 1
        for neighbor in city.neighbors:
            if not neighbor.is_ditermined_distance():
                queue.append(neighbor)
                neighbor.set_distance(current_distance)
                if current_distance > farthest_city.distance:
                    farthest_city = neighbor
    return farthest_city


farthest_city_from_city_0 = farthest_city(cities[0])
print(farthest_city(farthest_city_from_city_0).distance + 1)
