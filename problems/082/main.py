L, R = map(int, input().split())
mod = 10**9 + 7


# 1からnまで
def num(n):
    digits = len(str(n))
    result = 0
    for i in range(1, digits):
        result += i * (9 * 10 ** (i - 1)) * (10**i - 1 + 10 ** (i - 1)) // 2
        result %= mod
    result += digits * (n - 10 ** (digits - 1) + 1) * (n + 10 ** (digits - 1)) // 2
    return result % mod


print((num(R) - num(L - 1)) % mod)
