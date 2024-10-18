def main():
    n = int(input())
    sumn = 0
    for i in range(n):
        a = input()
        sumn += sum(map(int, a))
    print(sumn)
if __name__ == "__main__":
    main()