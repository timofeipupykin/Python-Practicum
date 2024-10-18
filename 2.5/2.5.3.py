def main():
    n, m, d = [int(input()) for i in range(3)]

    print(*[x for x in range(n, m + 1, d)], sep=" - ", end=" - ")
    print(*[x1 for x1 in range(m, n - 1, -d)], sep=" - ")
if __name__ == "__main__":
    main()