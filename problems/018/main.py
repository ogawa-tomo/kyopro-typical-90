import math

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())

for _ in range(Q):
    e = int(input())
    theta = math.pi * e * 2 / T
    y = -(L / 2) * math.sin(theta)
    z = (L / 2) * (1 - math.cos(theta))
    kyori = math.sqrt((Y - y) ** 2 + X**2)
    print(math.degrees(math.atan(z / kyori)))
