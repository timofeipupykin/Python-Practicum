def main():
    a = int(input())
    r = len(str((a + 1) // 2))
    for i in range(a):
        for x in range(a):
            print(f"{min(i + 1, x + 1, a - i, a - x): >{r}}", end=" ")
        print("")
if __name__ == "__main__":
    main()