def main():
    l_h = 0
    flag = True
    num = 0
    n = int(input())
    for i in range(n):
        b = int(input())
        c_h = b % 256
        r = (b // 256) % 256
        m = b // 256 ** 2
        n_h = (37 * (m + r + l_h)) % 256
        if n_h != c_h or n_h >= 100:
            if flag:
                num = i
                flag = False
        l_h = c_h
    if flag:
        print(-1)
    else:
        print(num)
if __name__ == "__main__":
    main()