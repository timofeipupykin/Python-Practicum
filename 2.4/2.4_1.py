def main():
    a = int(input())
    for x in range(1, a + 1):
        for y in range(1, a + 1):
            if y % a == 0:
                print(x * y, end="\n")
            else:
                print(x * y, end=" ")
if __name__ == "__main__":
    main()