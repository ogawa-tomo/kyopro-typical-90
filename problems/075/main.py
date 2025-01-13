import math

N = int(input())

# Nを素因数分解する
rootN = math.ceil(math.sqrt(N)) + 1
factors: list[int] = []
for i in range(2, rootN):
    while True:
        if N % i != 0:
            break
        factors.append(i)
        N //= i
if N > 1:
    factors.append(N)
# print(factors)

factors_num = len(factors)

i = 0
while True:
    if factors_num <= 2**i:
        print(i)
        exit()
    i += 1
