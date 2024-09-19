a = float(input())
b = float(input())
c = float(input())
if a == b == c == 0:
    print("Infinite solutions")
elif a == b == 0:
    print("No solution")
elif a == 0 and b != 0 and c != 0:
    x1 = -1 * c / b
    print(f"{x1:.2f}")
elif a == c == 0:
    print(0)
else:
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (0 - b - discr ** 0.5) / (2 * a)
        x2 = (0 - b + discr ** 0.5) / (2 * a)
        print(f"{min(x1, x2):.2f} {max(x1, x2):.2f}")
    elif discr == 0:
        x1 = (0 - b) / (2 * a)
        print(f"{x1:.2f}")
    else:
        print("No solution")
if __name__ == "__main__":
    print("2.2_17 completed")