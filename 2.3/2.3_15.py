def main():
    count = 0
    a = int(input())
    for i in range(a):
        b = input()
        count += b.count("зайка")
    print(count)
if __name__ == "__main__":
    main()