def main():
    a = int(input())
    count = 0
    if a == 1:
        count += 1
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            count += 1
    if count == 0:
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()