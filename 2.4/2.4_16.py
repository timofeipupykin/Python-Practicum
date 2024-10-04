def main():
    a = int(input())
    b = int(input())
    lenstri = a * b + (a - 1)
    for i in range(a):
        for x in range(1, a + 1):
            print(f"{x * (i + 1): ^{b}}", end="")
            if x != a:
                print("|", end="")
        print()
        if i != a - 1:
            print("-" * lenstri)
if __name__ == "__main__":
    main()