def change(n, y):
    x = ""
    while n > 0:
        x += str(n % y)
        n //= y
    return x[::-1]


def main():
    x = int(input())
    maxsumn = 0
    k = 0
    for i in range(10, 1, -1):
        c_sum = sum(map(int, change(x, i)))
        if c_sum >= maxsumn:
            maxsumn = c_sum
            k = i
    print(k)
if __name__ == "__main__":
    main()