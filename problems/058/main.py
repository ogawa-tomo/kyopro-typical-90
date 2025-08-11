# numを十進法で表したとき各桁の数字を足した値
def sum_decimal(num: int):
    target = num
    sum = 0
    for i in range(5):
        d = 10 ** (4 - i)
        q, mod = divmod(target, d)
        sum += q
        target = mod
    return sum


def button_result(num: int):
    return (num + sum_decimal(num)) % 10**5


N, K = map(int, input().split())
num = N
# first_ittr[num]: 数値numが最初に登場したときのイテレーション回数
first_ittr: list[int | None] = [None] * 10**5
cycle = 0
first_ittr_num = 0
for i in range(K):
    first_ittr_index = first_ittr[num]
    if first_ittr_index is None:
        first_ittr[num] = i
    else:
        cycle = i - first_ittr_index
        first_ittr_num = first_ittr_index
        break
    num = button_result(num)

if cycle == 0:
    print(num)
    exit()

actual_ittr = first_ittr_num + (K - first_ittr_num) % cycle
num = N
for _ in range(actual_ittr):
    num = button_result(num)
print(num)
