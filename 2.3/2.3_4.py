def main():
    a = [int(input()) for _ in range(2)]
    if a[0] <= a[1]:
        for i in range(a[0], a[1] + 1):
            print(i, end=" ")
    else:
        for x in range(a[0], a[1] - 1, -1):
            print(x, end=" ")
if __name__ == "__main__":
    main()