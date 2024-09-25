def main():
    a = [int(input()) for i in range(2)]
    nod = 0
    for x in range(1, min(a)):
        if a[0] % x == 0 and a[1] % x == 0:
            nod = max(nod, x)
    print(nod)
if __name__ == "__main__":
    main()