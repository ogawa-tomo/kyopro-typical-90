import itertools
import math


class Runner:
    def __init__(self, times: list[int]) -> None:
        self.times = times
        self.hates: list[Runner] = []

    def time(self, block: int):
        return self.times[block]


N = int(input())
runners: list[Runner] = []
# A: list[list[int]] = []
for i in range(N):
    times = list(map(int, input().split()))
    runners.append(Runner(times))

M = int(input())
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    runners[x].hates.append(runners[y])
    runners[y].hates.append(runners[x])

answer = math.inf
for order in itertools.permutations(runners):
    # print(order)
    possible = True
    time = 0
    for i, runner in enumerate(order):
        time += runner.time(i)
        if i == len(order) - 1:
            break
        next_runner = order[i + 1]
        if next_runner in runner.hates:
            possible = False
            break
    if not possible:
        continue
    answer = min(answer, time)

if answer == math.inf:
    print(-1)
else:
    print(answer)
