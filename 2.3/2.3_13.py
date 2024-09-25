def main():
    b = int(input())
    a = [input() for i in range(b)]
    print(sorted(a)[0])
if __name__ == "__main__":
    main()