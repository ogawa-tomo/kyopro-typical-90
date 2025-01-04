MOD = 10**9 + 7


# a^bをmodで割った余りを返す
def mod_power(a, b, mod):
    answer = 1
    while b > 0:
        # i回目のループで、bが2^iの成分を持っていれば、掛け算をする
        if b & 1:
            answer = (answer * a) % mod
        # i回目のループでは、a^(2^i)をかける（0回目: a^1, 1回目: a^2, 2回目: a^4, ...）
        a = a * a % mod
        b >>= 1
    return answer


# aの階乗をmodで割った余りを返す
def mod_factrial(a, mod):
    answer = 1
    for i in range(1, a + 1):
        answer *= i
        answer %= mod
    return answer


# nCrをmodで割った余りを返す
def mod_combination(n, r, mod):
    n_fact = mod_factrial(n, mod)
    r_fact = mod_factrial(r, mod)
    n_r_fact = mod_factrial(n - r, mod)
    bunshi = r_fact * n_r_fact % mod

    return (n_fact * mod_power(bunshi, mod - 2, mod)) % mod


N, L = map(int, input().split())

answer = 0
l_max = N // L  # Lを使える回数の最大値
for l_num in range(l_max + 1):
    one_num = N - L * l_num
    answer += mod_combination(l_num + one_num, l_num, MOD)

print(answer % MOD)
