H, W = map(int, input().split())

A: list[list[int]] = []
for _ in range(H):
    row = list(map(int, input().split()))
    A.append(row)
B: list[list[int]] = []
for _ in range(H):
    row = list(map(int, input().split()))
    B.append(row)
# print(A, B)

num = 0
for x in range(H - 1):
    for y in range(W - 1):
        diff = B[x][y] - A[x][y]
        A[x][y] += diff
        A[x + 1][y] += diff
        A[x][y + 1] += diff
        A[x + 1][y + 1] += diff
        num += abs(diff)

for x in range(H):
    for y in range(W):
        if A[x][y] != B[x][y]:
            print("No")
            exit()
print("Yes")
print(num)
