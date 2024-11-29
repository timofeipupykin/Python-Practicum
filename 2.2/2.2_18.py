def main():
    a = int(input())
    b = int(input())
    c = int(input())
    mas = [a, b, c]
    mas.sort()
    if mas[2] ** 2 == mas[0] ** 2 + mas[1] ** 2:
        print("100%")
    elif mas[2] ** 2 > mas[0] ** 2 + mas[1] ** 2:
        print("велика")
    else:
        print("крайне мала")
if __name__ == "__main__":
    main()