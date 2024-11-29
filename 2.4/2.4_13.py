def main():
    b = int(input())
    a = int(input())
    c = [i for i in range(1, a * b + 1)]
    stri = ""
    for i in range(b):
        for x in range(i, len(c), b):
            print(f"{c[x]: >{len(str(max(c)))}}", end=" ")
        print()
if __name__ == "__main__":
    main()