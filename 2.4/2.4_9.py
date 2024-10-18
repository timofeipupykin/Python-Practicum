def main():
    n = int(input())
    realnum = [max(map(int, input())) for i in range(n)]
    print(*realnum, sep="")
if __name__ == "__main__":
    main()