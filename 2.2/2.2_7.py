import math
n = input()
nlen1 = len(n) // 2
nlen2 = math.ceil(len(n) / 2)
a = n[0:nlen1:]
b = n[nlen2::]
if a == b[::-1]:
    print("YES")
else:
    print("NO")
if __name__ == "__main__":
    print("2.2_7 completed")