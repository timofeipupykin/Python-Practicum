def main():
    pety = int(input())
    vasy = int(input())
    toly = int(input())
    a = [[pety, "Петя"], [vasy, "Вася"], [toly, "Толя"]]
    a.sort()
    print(f"1. {a[2][1]}")
    print(f"2. {a[1][1]}")
    print(f"3. {a[0][1]}")
if __name__ == "__main__":
    main()