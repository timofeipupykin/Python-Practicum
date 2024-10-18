def main():
    n = int(input())
    m = int(input())

    for x in range(n):
        for y in range(m):
            if y % 2 == 0:
                num = y * n + x + 1
            else:
                num = (y + 1) * n - x
            print(f"{num: >{len(str(m * n))}}", end=" ")
        print()
if __name__ == "__main__":
    main()