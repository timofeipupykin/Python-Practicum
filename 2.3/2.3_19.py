def main():
    a = 1
    b = 1001
    print((a + b) // 2)
    while (c := input()) != "Угадал!":
        if c == "Больше":
            a = (a + b) // 2
        elif c == "Меньше":
            b = (a + b) // 2
        print((a + b) // 2)
if __name__ == "__main__":
    main()