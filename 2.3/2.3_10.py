def main():
    x = 0
    y = 0
    while True:
        direc = input()
        if direc == "СТОП":
            break
        num = int(input())
        if direc == "СЕВЕР":
            x += num
        elif direc == "ЮГ":
            x -= num
        elif direc == "ВОСТОК":
            y += num
        elif direc == "ЗАПАД":
            y -= num
    print(x, y, sep="\n")
if __name__ == "__main__":
    main()