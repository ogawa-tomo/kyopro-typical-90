import math

K = int(input())


# 約数列挙
k_divisors: list[int] = []
sqrt_k = math.sqrt(K)
for i in range(1, math.floor(math.sqrt(K)) + 1):
    q, mod = divmod(K, i)
    if mod != 0:
        continue
    k_divisors.append(i)
    if q != i:
        k_divisors.append(q)

k_divisors.sort()
# print(k_divisors)

answer = 0

for i in range(len(k_divisors)):
    for j in range(i, len(k_divisors)):
        a = k_divisors[i]
        b = k_divisors[j]
        c, mod = divmod(K, a * b)
        if mod != 0:
            continue
        if c < b:
            continue
        answer += 1

print(answer)
