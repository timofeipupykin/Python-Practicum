def main():
    num1, word, num2 = [input() for i in range(3)]
    len_w = len(word)
    count_s = word.count(" ")

    num1 = int(num1)
    num2 = int(num2)

    if len_w % 2 == 0 and count_s >= 1:
        print(num1 + num2)
    elif len_w % 2 == 0 and count_s < 1:
        print(num1 - num2)
    elif len_w % 2 != 0 and count_s >= 1:
        print(num1 * num2)
    else:
        print(num1 // num2)
if __name__ == "__main__":
    main()