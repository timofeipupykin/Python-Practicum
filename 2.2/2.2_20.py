def main():
    a = input()
    b = input()
    c = input()
    mas = [a, b, c]
    mas1 = [i for i in mas if "зайка" in i]
    mas1.sort()
    print(mas1[0], len(mas1[0]))
if __name__ == "__main__":
    main()