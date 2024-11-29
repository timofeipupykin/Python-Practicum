def main():
    b = int(input())
    a = int(input())
    c = [i for i in range(1, a * b + 1)]
    for x in c:
        print(f"{x: >{len(str(max(c)))}}", end=" ")
        if x % a == 0:
            print()
if __name__ == "__main__":
    main()