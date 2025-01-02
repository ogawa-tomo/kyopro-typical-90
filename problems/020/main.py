import math

a, b, c = map(int, input().split())

# if math.log2(a) < b * math.log2(c):
#     print("Yes")
# else:
#     print("No")

if a < c**b:
    print("Yes")
else:
    print("No")
