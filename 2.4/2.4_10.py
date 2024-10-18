def main():
    n = int(input())
    print("А Б В")
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            for z in range(1, n + 1):
                if x + y + z == n:
                    print(x, y, z)
if __name__ == "__main__":
    main()