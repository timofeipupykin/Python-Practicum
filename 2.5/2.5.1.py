def main():
    a, b, c = [int(input()) for i in range(3)]
    r = (a ** b) % (a + c)
    print(f"({a} ^ {b}) mod ({a} + {c}) = {r}")
if __name__ == "__main__":
    main()