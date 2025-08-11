import statistics

N = int(input())


class Factory:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def distance(x: float, y: float, factory: Factory):
    return abs(factory.x - x) + abs(factory.y - y)


factories: list[Factory] = []
x_list: list[int] = []
y_list: list[int] = []
for _ in range(N):
    x, y = map(int, input().split())
    factories.append(Factory(x, y))
    x_list.append(x)
    y_list.append(y)

power_x = statistics.median(x_list)
power_y = statistics.median(y_list)
answer = 0
for factory in factories:
    answer += distance(power_x, power_y, factory)
print(int(answer))
