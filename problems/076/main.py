N = int(input())
A = list(map(int, input().split()))

target = sum(A) / 10

A *= 2
# print(A)
left = 0
right = 0

current_S = A[0]
while True:
    if current_S == target:
        print("Yes")
        exit()
    if current_S < target:
        right += 1
        if right < 2 * N - 1:
            current_S += A[right]
            continue
        print("No")
        exit()
    if current_S > target:
        left += 1
        current_S -= A[left - 1]
        if left > right:
            if right < 2 * N - 1:
                right += 1
                current_S += A[right]
                continue
            print("No")
            exit()
