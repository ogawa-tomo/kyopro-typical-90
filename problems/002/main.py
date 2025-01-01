N = int(input())

if N % 2 == 1:
    exit()


def is_valid(kakkos: list[str]):
    score = 0
    for kakko in kakkos:
        if kakko == "(":
            score += 1
        else:
            score -= 1
            if score < 0:
                return False
    return score == 0


for i in range(1 << N):
    kakkos = []
    for shift in reversed(range(N)):
        if not (i >> shift) & 1:
            kakkos.append("(")
        else:
            kakkos.append(")")
    if is_valid(kakkos):
        print("".join(kakkos))
