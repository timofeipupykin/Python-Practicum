def main():
    a = int(input())
    limit = 1
    current = 0
    for i in range(a):
        print(i + 1, end=" ")
        current += 1
        if current == limit:
            print("")
            current = 0
            limit += 1
if __name__ == "__main__":
    main()