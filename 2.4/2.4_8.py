def main():
    n = int(input())
    c = []
    for i in range(n):
        a = [i, input()]
        b = input()
        sumb = sum(map(int, b))
        c.append([sumb, a])
    c.sort(reverse=True)
    print(c[0][1][1])
if __name__ == "__main__":
    main()