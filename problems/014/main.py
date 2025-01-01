N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

distance = 0
for i in range(N):
    distance += abs(A[i] - B[i])
print(distance)
