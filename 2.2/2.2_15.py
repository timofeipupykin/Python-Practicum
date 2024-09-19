a = input()
b = input()
c = list(map(int, a + b))
c.sort()
n = (c[1] + c[2]) % 10
print(str(c[3]) + str(n) + str(c[0]))
if __name__ == "__main__":
    print("2.2_15 completed")