def check(x):
    flag = True
    for c in range(2, int(x ** 0.5) + 1):
        if x % c == 0:
            flag = False
            break
    if flag and x != 1:
        return True
    else:
        return False

def main():
    n = int(input())
    count = 0
    for _ in range(n):
        s = int(input())
        if check(s):
            count += 1
    print(count)
if __name__ == "__main__":
    main()