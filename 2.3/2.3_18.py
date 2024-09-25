def main():
    a = int(input())
    b = []
    count = 2
    while a != 1:
        if a % count == 0:
            b.append(count)
            a //= count
        else:
            count += 1
    print(*b, sep=" * ")
if __name__ == "__main__":
    main()