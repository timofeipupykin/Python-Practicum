def main():
    pety = int(input())
    vasy = int(input())
    toly = int(input())
    n = [[pety, "Петя"], [vasy, "Вася"], [toly, "Толя"]]
    n.sort()
    print(f"{n[2][1]: ^24}")
    print(f"{n[1][1]: ^8}{'': >16}")
    print(f"{'': >16}{n[0][1]: ^8}")
    print(f"{'II': ^8}{'I': ^8}{'III': ^8}")
if __name__ == "__main__":
    main()