N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

mod = 46
mod_B = [b % mod for b in B]
mod_b_dict = {}
for i in range(mod):
    mod_b_dict[i] = 0
for mod_b in mod_B:
    mod_b_dict[mod_b] += 1
mod_C = [c % mod for c in C]
mod_c_dict = {}
for i in range(mod):
    mod_c_dict[i] = 0
for mod_c in mod_C:
    mod_c_dict[mod_c] += 1

answer = 0
for a in A:
    mod_a = a % mod
    b_plus_c_mod = (mod - mod_a) % mod
    for mod_b in range(mod):
        mod_c = (b_plus_c_mod - mod_b) % mod
        answer += mod_b_dict[mod_b] * mod_c_dict[mod_c]

print(answer)
