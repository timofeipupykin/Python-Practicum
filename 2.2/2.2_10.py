def main():
    a = input()
    n1 = int(a[1]) + int(a[2])
    n2 = int(a[1]) + int(a[0])
    n3 = str(max(n2, n1)) + str(min(n2, n1))
    print(n3)
if __name__ == "__main__":
    main()