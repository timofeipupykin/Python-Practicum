def main():
    n = int(input())
    count = 0
    for i in range(n):
        check = True
        while (a := input()) != "ВСЁ":
            if a == "зайка" and check:
                count += 1
                check = False
    print(count)
if __name__ == "__main__":
    main()