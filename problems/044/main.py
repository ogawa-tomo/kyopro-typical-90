N, Q = map(int, input().split())
A = list(map(int, input().split()))


class Array:
    def __init__(self, arr: list[int]):
        self.arr = arr
        self.length = len(arr)
        self.current_zero = 0

    def shift(self, x: int):
        self.current_zero = (self.current_zero - x) % self.length

    def actual_index(self, i: int):
        return (self.current_zero + i) % self.length

    def get(self, i: int):
        return self.arr[self.actual_index(i)]

    def set(self, i: int, value: int):
        self.arr[self.actual_index(i)] = value

    def swap(self, x: int, y: int):
        x_value = self.get(x)
        y_value = self.get(y)
        # print(self.arr)
        # print(x, y)
        self.set(x, y_value)
        self.set(y, x_value)
        # print(self.arr)


arr = Array(A)
for _ in range(Q):
    t, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if t == 1:
        arr.swap(x, y)
    elif t == 2:
        arr.shift(1)
    elif t == 3:
        print(arr.get(x))
