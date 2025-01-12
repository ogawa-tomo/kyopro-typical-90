N, Q = map(int, input().split())
A = list(map(int, input().split()))

huben = 0
# E[i]: A[i]-A[i + 1] (i <= N - 2)
E: list[int] = []
for i, a in enumerate(A):
    if i == N - 1:
        break
    E.append(A[i] - A[i + 1])
    huben += abs(E[i])

for _ in range(Q):
    L, R, V = map(int, input().split())
    L -= 1
    R -= 1
    if L > 0:
        before_huben = abs(E[L - 1])
        E[L - 1] -= V
        after_huben = abs(E[L - 1])
        huben += after_huben - before_huben
    if R < N - 1:
        before_huben = abs(E[R])
        E[R] += V
        after_huben = abs(E[R])
        huben += after_huben - before_huben
    print(huben)
