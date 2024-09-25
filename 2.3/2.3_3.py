def main():
    a = [int(input()) for _ in range(2)]
    print(*[i for i in range(a[0], a[1] + 1)])
if __name__ == "__main__":
    main()