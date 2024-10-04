def main():
    n = int(input())
    for x in range(n):
        for i in range(3 + x, 0, -1):
            print(f"До старта {i} секунд(ы)")
        print(f"Старт {x + 1}!!!")
if __name__ == "__main__":
    main()