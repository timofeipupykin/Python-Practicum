import itertools as it


n = int(input())
    
digits = []
for i in range(n):
    digits.append(input().split(", "))

u_nums = set(int("".join(comb)) for comb in it.product(*digits))

for number in sorted(u_nums):
    print(number)
