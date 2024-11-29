def main():
    limit = int(input())
    count = 0
    width = 1
    max_len = 0
    while count <= limit:
        stri_len = 0
        for x in range(width):
            count += 1
            if count <= limit:
                stri_len += len(str(count))
            if x < width - 1 and count < limit:
                stri_len += 1
        max_len = max(max_len, stri_len)
        width += 1
    count = 0
    width = 1
    while count <= limit:
        stri = ""
        for i in range(width):
            count += 1
            if count <= limit:
                stri += str(count)
            if i < width - 1 and count < limit:
                stri += " "
        width += 1
        print(f"{stri: ^{max_len}}")
if __name__ == "__main__":
    main()