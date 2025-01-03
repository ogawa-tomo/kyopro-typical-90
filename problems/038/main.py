def GCD(a: int, b: int):
    if b == 0:
        return a
    return GCD(b, a % b)


a, b = map(int, input().split())
answer = a * b // GCD(a, b)
if answer > 10**18:
    print("Large")
else:
    print(answer)
