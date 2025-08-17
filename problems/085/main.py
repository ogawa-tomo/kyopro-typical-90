import math

K = int(input())

answer = 0

# aはKの三乗根以下である
for a in range(1, math.ceil(math.pow(K, 1 / 3)) + 1):
    target, mod = divmod(K, a)
    if mod != 0:
        continue
    # bはtargetの平方根以下である
    for b in range(a, math.ceil(math.sqrt(target)) + 1):
        # print(a, b)
        q, mod = divmod(target, b)
        if mod == 0 and q >= b:
            # print(a, b, q)
            answer += 1

print(answer)
