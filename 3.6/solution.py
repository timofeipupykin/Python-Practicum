lines = [input().split("&") for _ in range(int(input()))]

for i in lines:
    line = ""
    start = int(i[0])
    end = int(i[1])
    for letter in i[2][start::2]:
        if end > 0:
            line += letter
            end -= 1
        else:
            break
    print(line)