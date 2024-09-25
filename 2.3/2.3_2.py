def main():
    a = ""
    b = 0
    while a != "Приехали!":
        a = input()
        b += a.count("зайка")
    print(b)
if __name__ == "__main__":
    main()