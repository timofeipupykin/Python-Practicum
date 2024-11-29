def main():
    b = int(input())
    a = int(input())
    c = [i for i in range(1, a * b + 1)]
    stri = ""
    stri1 = []
    count = 0
    for x in c:
        if count % 2 == 0:
            stri += f"{x: >{len(str(max(c)))}}" + " "
            if x % a == 0:
                stri += "\n"
                count += 1
        else:
            stri1.append(" ")
            stri1.append(f"{x: >{len(str(max(c)))}}")
            if x % a == 0:
                stri += "".join(stri1[::-1])
                stri1.clear()
                stri += "\n"
                count += 1
    print(stri)
if __name__ == "__main__":
    main()