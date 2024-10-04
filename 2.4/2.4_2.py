def main():
    a = int(input())
    for x in range(1, a + 1):
        for y in range(1, a + 1):
            print(f"{y} * {x} = {x * y}")
if __name__ == "__main__":
    main()