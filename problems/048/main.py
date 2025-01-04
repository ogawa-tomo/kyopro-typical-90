import heapq


class Problem:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b


class AvailablePoint:
    def __init__(self, problem: Problem, value: int):
        self.problem = problem
        self.value = value

    def is_b_point(self):
        return self.value == self.problem.b

    def __lt__(self, other):
        return self.value > other.value

    def __repr__(self):
        return str(self.value)


N, K = map(int, input().split())
# problems: list[Problem] = []
available_points: list[AvailablePoint] = []
for _ in range(N):
    a, b = map(int, input().split())
    problem = Problem(a, b)
    heapq.heappush(available_points, AvailablePoint(problem, problem.b))

# print(available_points)
point = 0
for _ in range(K):
    available_point = heapq.heappop(available_points)
    point += available_point.value
    if available_point.is_b_point():
        heapq.heappush(
            available_points,
            AvailablePoint(
                available_point.problem,
                available_point.problem.a - available_point.problem.b,
            ),
        )
print(point)
