import math
def main():
    a = [int(input()) for i in range(2)]
    nok = 0
    for x in range(min(a), math.prod(a) + 1):
        if x % a[0] == 0 and x % a[1] == 0:
            print(x)
            break
if __name__ == "__main__":
    main()