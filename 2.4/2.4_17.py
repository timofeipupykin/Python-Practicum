import math


def check(n):
    nlen1 = len(n) // 2
    nlen2 = math.ceil(len(n) / 2)
    a = n[0:nlen1:]
    b = n[nlen2::]
    if a == b[::-1]:
        return True
    else:
        return False

def main():
    x = int(input())
    count = 0
    for i in range(x):
        k = input()
        if check(k):
            count += 1
    print(count)
if __name__ == "__main__":
    main()