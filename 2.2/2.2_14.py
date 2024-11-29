def main():
    n = list(map(int, input()))
    n.sort()
    nmax = str(n[2]) + str(n[1])
    if n[0] != 0:
        nmin = str(n[0]) + str(n[1])
    else:
        nmin = str(n[1]) + str(n[0])
    print(nmin, nmax)
if __name__ == "__main__":
    main()