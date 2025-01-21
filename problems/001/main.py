N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))


# 最小のピースがx以上になるように切り分けられるか
def cuttable(x):
    num_pieces = 0
    current_cut_x = 0
    current_index = 0
    while current_index < N:
        if A[current_index] - current_cut_x >= x:
            num_pieces += 1
            current_cut_x = A[current_index]
            if num_pieces >= K + 1:
                return True
        current_index += 1
    if L - current_cut_x >= x:
        num_pieces += 1
    return num_pieces >= K + 1


# 最小のピースがx以上になるように切り分けられるような、最大のxを求める
ok = 0
ng = L
while ng - ok > 1:
    mid = (ok + ng) // 2
    if cuttable(mid):
        ok = mid
    else:
        ng = mid

print(ok)
