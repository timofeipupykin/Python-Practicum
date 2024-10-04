def main():
    numb = int(input())
    a = [int(input()) for i in range(numb)]
    nod = 0
    for x in range(1, min(a) + 1):
        flag = True
        for i in a:
            if i % x != 0:
                flag = False
        if flag:
            nod = max(nod, x)
    print(nod)
if __name__ == "__main__":
    main()