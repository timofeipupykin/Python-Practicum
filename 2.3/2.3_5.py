def main():
    b = 0
    while True:
        a = float(input())
        if a >= 500:
            b += a * 0.9
        elif a == 0:
            print(b)
            break
        else:
            b += a
if __name__ == "__main__":
    main()