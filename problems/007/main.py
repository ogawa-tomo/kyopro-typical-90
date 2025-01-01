N = int(input())
A = list(map(int, input().split()))
A.sort()
# print(A)
Q = int(input())
for _ in range(Q):
    b = int(input())
    ok = -1
    ng = N
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if A[mid] <= b:
            ok = mid
        else:
            ng = mid
    # print(b, ok, ng)
    if ok == -1:
        print(A[0] - b)
    elif ng == N:
        print(b - A[N - 1])
    else:
        print(min(b - A[ok], A[ok + 1] - b))
