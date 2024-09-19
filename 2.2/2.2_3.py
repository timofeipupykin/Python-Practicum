pety = int(input())
vasy = int(input())
toly = int(input())
if toly == max(pety, vasy, toly):
    print("Толя")
elif vasy == max(pety, vasy, toly):
    print("Вася")
else:
    print("Петя")
if __name__ == "__main__":
    print("2.2_3 completed")