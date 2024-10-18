def main():
    n = int(input())
    mins = []
    for _ in range(n):
        count = 0
        nums = 0
        while (a := input()) != "end":
            nums += int(a)
            count += 1
        if count != 0:
            mins.append(nums / count)
    print(f"{min(mins):.2f}")
if __name__ == "__main__":
    main()